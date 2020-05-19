# -*- coding: utf-8 -*-

import datetime
import time
import logging

import pandas as pd
import pythoncom
import win32com
import win32event

from tslib import xing
from tslib.xing import XING_RES_BLOCKS
import settings
from tslib.xing.res import parser

__author__ = 'Moon Kwon Kim'

logger = logging.getLogger(__name__)


class XAQueryEvents(object):

    READY = 0
    SUCCEEDED = 1
    FAILED = 999
    status = READY

    @classmethod
    def OnReceiveData(cls, szTrCode):
        logger.debug("OnReceiveData: %s" % str(szTrCode))
        XAQueryEvents.status = XAQueryEvents.SUCCEEDED

    @classmethod
    def OnReceiveMessage(cls, bIsSystemError, nMessageCode, szMessage):
        logger.debug("OnReceiveMessage: %s %s %s" % (bIsSystemError, nMessageCode.encode('utf-8'), szMessage.encode('utf-8')))

    @classmethod
    def wait(cls, res_name=None):
        XAQueryEvents.status = XAQueryEvents.READY
        prev = time.time()
        while XAQueryEvents.status == XAQueryEvents.READY:
            pythoncom.PumpWaitingMessages()
            curr = time.time()
            if curr-prev > 10:
                XAQueryEvents.status = XAQueryEvents.FAILED
                return


class XAQuery(object):

    @classmethod
    def query(cls, res_name, in_block, is_service=False, force_continue=False):
        """
        Send a query with input InBlock items and receive results from the Xing trading system.
        :param res_name: resource name
        주식현재가(시세)조회: t1102OutBlock
        주식챠트(틱/n틱): t8411OutBlock, t8411OutBlock1
        주식챠트(N분): t8412OutBlock, t8412OutBlock1
        주식챠트(일주월): t8413OutBlock, t8413OutBlock1
        신고/신저가: t1442InBlock, t1442OutBlock, t1442OutBlock1
        ...
        :param in_block: InBlock items which vary depends on the resource
        :return: a dict of DataFrames; Each DataFrame is an OutBlock.
        """

        tr = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEvents)
        tr.LoadFromResFile("%s%s.res" % (xing.XING_RES_PATH, res_name))

        # Set InBlock
        # The name of InBlock is formed by concatenating the resource name and 'InBlock'.
        if is_service:
            in_block_name = None
        else:
            in_block_name = [k for k in XING_RES_BLOCKS if k.startswith('%sInBlock' % res_name)]
            if len(in_block_name) > 0:
                in_block_name = in_block_name[0]
            else:
                raise Exception("No in-blocks.")
            # Set each InBlock item in the input, in_block, for query.
            for k, v in in_block.items():
                tr.SetFieldData(in_block_name, k, 0, v)

        # Prepare OutBlocks
        # Retrieve OutBlock names from the resource file and store them as a list.
        out_block_name_list = [k for k in XING_RES_BLOCKS if k.startswith('%sOutBlock' % res_name)]
        # If there is no OutBlock, there is no need to query. Hence, raise an exception.
        if len(out_block_name_list) == 0:
            raise Exception("No out-blocks.")
        # Check if there is OutBlockOccurs.
        is_occurs = True if len(out_block_name_list) > 1 else False
        # Sort the OutBlock list by names
        out_block_name_list.sort()

        # Request
        # Send a request with the InBlock items.
        if is_service:
            ret = tr.RequestService(res_name, in_block)
        else:
            ret = tr.Request(False)
        # If the return value is less than 0, an error occurred.
        # As the query was failed, return None.
        if ret < 0: # error
            return None
        # Wait for the query process is done.
        XAQueryEvents.wait()
        if XAQueryEvents.status != XAQueryEvents.SUCCEEDED:
            return None

        # Handle OutBlock and OutBlock Occurs
        out_block_list = {}

        while(True):
            # Handle OutBlock
            if not out_block_name_list[0] in out_block_list:
                out_block_list[out_block_name_list[0]] = []
            out_block = {k: tr.GetFieldData(out_block_name_list[0], k, 0) for k in XING_RES_BLOCKS[out_block_name_list[0]][1]}
            out_block_list[out_block_name_list[0]].append(out_block)
            # Check if there are results for OutBlockOccurs.
            if not is_occurs:
                break

            # Handle OutBlock Occurs
            for name in out_block_name_list[1:]:
                # Decompress
                size = 0
                if 'comp_yn' in in_block and in_block['comp_yn'] == 'Y':
                    size = tr.Decompress(name)
                    if size == 0:
                        break

            # Get OutBlock Occurs
            cnt = tr.GetBlockCount(name)
            if cnt == 0:
                break

            out_block_occurs = [{k: tr.GetFieldData(name, k, i) for k in XING_RES_BLOCKS[name][1]} for i in
                                range(cnt)]
            if not name in out_block_list:
                out_block_list[name] = out_block_occurs
            else:
                out_block_list[name].extend(out_block_occurs)

            # Escape if service request
            if is_service:
                break

            if not force_continue:
                # Handle Continuous Request
                cts_list =  [k for k in XING_RES_BLOCKS[in_block_name][1] if k.startswith('cts_') or k == "idx"]
                is_diff = False

                if len(cts_list) > 0:
                    if len(out_block_list[out_block_name_list[0]]) > 0:
                        prev = out_block_list[out_block_name_list[0]][-1]
                        for cts_name in cts_list:
                            if prev[cts_name] == "" or out_block[cts_name] == "":
                                continue
                            if prev[cts_name] == out_block[cts_name]:
                                # To do more
                                is_diff = True
                                break
                    else:
                        # First continuous request
                        is_diff = True
                if not is_diff:
                    # Nothing to do more
                    break

                # Set attributes for a continuous request
                for cts_name in cts_list:
                    tr.SetFieldData(in_block_name, cts_name, 0, out_block[cts_name])

            # Do a continuous request
            if tr.IsNext:
                ret = tr.Request(True)
                if ret < 0: # error
                    break
                else:
                    XAQueryEvents.wait()
                    if XAQueryEvents.status != XAQueryEvents.SUCCEEDED:
                        break
            else:
                break

        # Convert to pandas DataFrame
        for k, v in out_block_list.items():
            out_block_list[k] = cls._sort(pd.DataFrame(v))
        return out_block_list

    @classmethod
    def _sort(cls, data):
        # Sorting by date and time
        if 'date' in data and 'time' in data:
            data = data.sort_values(['date', 'time'])
        elif 'date' in data:
            data = data.sort_values('date')
        elif 'time' in data:
            data = data.sort_values('time')
        data = data.reset_index(drop=True)
        return data

    @classmethod
    def get_chart(cls, code, tick_unit="min", ncnt=30, sdate=None, edate=None):
        if sdate is None:
            sdate = '00000000'
        if edate is None:
            today = datetime.date.today().strftime(settings.FORMAT_DATE)
            # yesterday = (datetime.date.today()-datetime.timedelta(days=1)).strftime(settings.FORMAT_DATE)
            # thatday = datetime.datetime(2015, 11, 9).strftime(settings.FORMAT_DATE)
            edate = today

        in_block = {
            'shcode': code,
            'qrycnt': 2000,
            'comp_yn': 'Y',
            'sdate': sdate,
            'edate': edate
        }

        gubun = None
        if tick_unit == "tick":
            res_name = 't8411'
            in_block['nday'] = 0
            in_block['ncnt'] = ncnt
        elif tick_unit == "min":
            res_name = 't8412'
            in_block['nday'] = 0
            in_block['ncnt'] = ncnt
        elif tick_unit == "day":
            res_name = 't8413'
            in_block["gubun"] = 2
        elif tick_unit == "week":
            res_name = 't8413'
            in_block["gubun"] = 3
        elif tick_unit == "month":
            res_name = 't8413'
            in_block["gubun"] = 4

        # Query and receive chart
        d = XAQuery.query(res_name, in_block)
        if d is None:
            return None

        # For chart, OutBlockOccurs is the only needed data.
        # Just return the Occurs data.
        bname = '%sOutBlock1' % res_name
        if bname in d:
            d = d[bname]
            d['open'] = d['open'].astype(int)
            d['close'] = d['close'].astype(int)
            d['high'] = d['high'].astype(int)
            d['low'] = d['low'].astype(int)
            d['jdiff_vol'] = d['jdiff_vol'].astype(int)
            d['jongchk'] = d['jongchk'].astype(int)
            if 'sign' in d:
                d['sign'] = d['sign'].astype(int)
            return d
        return None


if __name__ == '__main__':
    import sys, os
    import pandas as pd
    from auth import Auth
    from tslib.xing.session import XASession
    from tslib.xing.query import XAQuery
    from tslib.xing.real import XAReal

    (id, pw, cert) = Auth.load()
    ts_session = XASession.login(id, pw, cert)
    #
    # highvolume_in_block = {
    #     'gubun': 0 # 0: all, 1: KOSPI, 2: KOSDAQ
    # }
    # highvolume_data = XAQuery.query('t1452', highvolume_in_block)
    # highvolume_data['t1452OutBlock1']['volume'] = highvolume_data['t1452OutBlock1']['volume'].astype(int)
    # highvolume_data['t1452OutBlock1']['volume'] = highvolume_data['t1452OutBlock1']['volume'].astype(int)
    # highvolume_data['t1452OutBlock1'] = highvolume_data['t1452OutBlock1'].sort_values(["volume"], ascending=[False])
    # pd.set_option('display.max_rows', len(highvolume_data['t1452OutBlock1']))
    # print(highvolume_data['t1452OutBlock1'])
    #
    newhigh_cospi_inblock = {
        'gubun': 1,
        'type1': 0,
        'type2': 3,
        'type3': 0
    }
    newhigh_cospi_data = XAQuery.query('t1442', newhigh_cospi_inblock)
    if 't1442OutBlock1' in newhigh_cospi_data:
        print(newhigh_cospi_data['t1442OutBlock1'])
