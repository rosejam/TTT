# -*- coding: utf-8 -*-

import logging

import pythoncom
import win32com

from tslib import xing
from tslib.xing import XING_RES_BLOCKS
import settings

__author__ = 'Moon Kwon Kim'

logger = logging.getLogger(__name__)


class XAReal(object):

    def __init__(self):
        self.is_running = False

    def start(self, res_name, in_block, cb, postfix=""):


        class XARealEvents(object):

            READY = 0
            SUCCEEDED = 1
            FAILED = 999
            status = READY

            def OnReceiveRealData(self, szTrCode):
                logger.debug("OnReceiveRealData: %s" % str(szTrCode))
                XARealEvents.status = XARealEvents.SUCCEEDED

            def OnReceiveLinkData(self, szLinkName, szData, szFilter):
                pass


        try:
            pythoncom.CoInitialize()
        except pythoncom.com_error:
            # already initialized.
            pass

        tr = win32com.client.DispatchWithEvents("XA_DataSet.XAReal.1", XARealEvents)
        tr.LoadFromResFile("%s%s.res" % (xing.XING_RES_PATH, res_name))

        for k, v in in_block.items():
            tr.SetFieldData('InBlock', k, v)

        out_block_name_list = [k for k in XING_RES_BLOCKS if k.startswith('%sOutBlock' % res_name)]
        if len(out_block_name_list) == 0:
            raise Exception("No out blocks.")

        tr.AdviseRealData()
        self.is_running = True
        while self.is_running:
            pythoncom.PumpWaitingMessages()
            if XARealEvents.status == XARealEvents.SUCCEEDED:
                XARealEvents.status = XARealEvents.READY
                data = {k: tr.GetFieldData("OutBlock", k) for k in xing.XING_RES_BLOCKS["%sOutBlock" % res_name][1]}
                cb(data)

    def stop(self):
        self.is_running = False
