import os
import time

import win32com.client
from pywinauto import application
import psutil

import constants
import util


class Creon:
    def __init__(self):
        self.obj_CpUtil_CpCodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
        self.obj_CpUtil_CpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
        self.obj_CpSysDib_StockChart = win32com.client.Dispatch('CpSysDib.StockChart')
        self.obj_CpTrade_CpTdUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')
        self.obj_CpSysDib_MarketEye = win32com.client.Dispatch('CpSysDib.MarketEye')

        # 종목별 공매도 추이
        # https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=227&page=1&searchString=CpSysDib.CpSvr7238&p=8841&v=8643&m=9505
        self.obj_CpSysDib_CpSvr7238 = win32com.client.Dispatch('CpSysDib.CpSvr7238')
        
        # 계좌별 매도 가능수량
        # https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=172&page=1&searchString=CpTrade.CpTdNew5331B&p=8841&v=8643&m=9505
        self.obj_CpTrade_CpTdNew5331B = win32com.client.Dispatch('CpTrade.CpTdNew5331B')

        # 계좌별 매수 가능금액/수량
        # https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=171&page=3&searchString=%EA%B3%84%EC%A2%8C&p=8841&v=8643&m=9505
        self.obj_CpTrade_CpTdNew5331A = win32com.client.Dispatch('CpTrade.CpTdNew5331A')

    def connect(self, id_, pwd, pwdcert, trycnt=300):
        if not self.connected():
            self.disconnect()
            app = application.Application()
            app.start(
                'C:\\CREON\\STARTER\\coStarter.exe /prj:cp /id:{id} /pwd:{pwd} /pwdcert:{pwdcert} /autostart'.format(
                    id=id_, pwd=pwd, pwdcert=pwdcert
                )
            )
        
        cnt = 0
        while not self.connected():
            if cnt > trycnt:
                return False
            time.sleep(1)
            cnt += 1
        
        return True

    def connected(self):
        plist = [p.name() for p in psutil.process_iter()]
        if "DibServer.exe" in plist and "CpStart.exe" in plist:
            return self.obj_CpUtil_CpCybos.IsConnect != 0
        return False

    def disconnect(self):
        os.system('taskkill /IM coStarter* /F /T')
        os.system('taskkill /IM CpStart* /F /T')
        os.system('taskkill /IM DibServer* /F /T')
        os.system('wmic process where "name like \'%coStarter%\'" call terminate')
        os.system('wmic process where "name like \'%CpStart%\'" call terminate')
        os.system('wmic process where "name like \'%DibServer%\'" call terminate')
        self.obj_CpUtil_CpCybos.PlusDisconnect()
        return True

    def wait(self):
        remain_time = self.obj_CpUtil_CpCybos.LimitRequestRemainTime
        remain_count = self.obj_CpUtil_CpCybos.GetLimitRemainCount(1)
        if remain_count <= 3:
            time.sleep(remain_time / 1000)

    def get_stockcodes(self, code):
        """
        code: kospi=1, kosdaq=2
        market codes:
            typedefenum{
            [helpstring("구분없음")]CPC_MARKET_NULL= 0, 
            [helpstring("거래소")]   CPC_MARKET_KOSPI= 1, 
            [helpstring("코스닥")]   CPC_MARKET_KOSDAQ= 2, 
            [helpstring("K-OTC")] CPC_MARKET_FREEBOARD= 3, 
            [helpstring("KRX")]       CPC_MARKET_KRX= 4,
            [helpstring("KONEX")] CPC_MARKET_KONEX= 5,
            }CPE_MARKET_KIND; 
        """
        if code in [constants.MARKET_CODE_KOSPI, constants.MARKET_CODE_KOSDAQ]:
            res = self.obj_CpUtil_CpCodeMgr.GetStockListByMarket(code)
            return res
        else:
            return None

    def get_stockstatus(self, code):
        """
        code 에해당하는주식상태를반환한다

        code : 주식코드
        return :
        typedefenum {
        [helpstring("정상")]   CPC_CONTROL_NONE   = 0,
        [helpstring("주의")]   CPC_CONTROL_ATTENTION= 1,
        [helpstring("경고")]   CPC_CONTROL_WARNING= 2,
        [helpstring("위험예고")]CPC_CONTROL_DANGER_NOTICE= 3,
        [helpstring("위험")]   CPC_CONTROL_DANGER= 4,
        }CPE_CONTROL_KIND;
        typedefenum   {
        [helpstring("일반종목")]CPC_SUPERVISION_NONE= 0,
        [helpstring("관리")]   CPC_SUPERVISION_NORMAL= 1,
        }CPE_SUPERVISION_KIND;
        typedefenum   {
        [helpstring("정상")]   CPC_STOCK_STATUS_NORMAL= 0,
        [helpstring("거래정지")]CPC_STOCK_STATUS_STOP= 1,
        [helpstring("거래중단")]CPC_STOCK_STATUS_BREAK= 2,
        }CPE_SUPERVISION_KIND;
        """
        if not code.startswith('A'):
            code = 'A' + code
        return {
            'control': self.obj_CpUtil_CpCodeMgr.GetStockControlKind(code),
            'supervision': self.obj_CpUtil_CpCodeMgr.GetStockSupervisionKind(code),
            'status': self.obj_CpUtil_CpCodeMgr.GetStockStatusKind(code),
        }

    def get_stockfeatures(self, code):
        """
        https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=11&page=1&searchString=%EA%B1%B0%EB%9E%98%EC%A0%95%EC%A7%80&p=8841&v=8643&m=9505
        """
        if not code.startswith('A'):
            code = 'A' + code
        stock = {
            'name': self.obj_CpUtil_CpCodeMgr.CodeToName(code),
            'marginrate': self.obj_CpUtil_CpCodeMgr.GetStockMarginRate(code),
            'unit': self.obj_CpUtil_CpCodeMgr.GetStockMemeMin(code),
            'industry': self.obj_CpUtil_CpCodeMgr.GetStockIndustryCode(code),
            'market': self.obj_CpUtil_CpCodeMgr.GetStockMarketKind(code),
            'control': self.obj_CpUtil_CpCodeMgr.GetStockControlKind(code),
            'supervision': self.obj_CpUtil_CpCodeMgr.GetStockSupervisionKind(code),
            'status': self.obj_CpUtil_CpCodeMgr.GetStockStatusKind(code),
            'capital': self.obj_CpUtil_CpCodeMgr.GetStockCapital(code),
            'fiscalmonth': self.obj_CpUtil_CpCodeMgr.GetStockFiscalMonth(code),
            'groupcode': self.obj_CpUtil_CpCodeMgr.GetStockGroupCode(code),
            'kospi200kind': self.obj_CpUtil_CpCodeMgr.GetStockKospi200Kind(code),
            'section': self.obj_CpUtil_CpCodeMgr.GetStockSectionKind(code),
            'off': self.obj_CpUtil_CpCodeMgr.GetStockLacKind(code),
            'listeddate': self.obj_CpUtil_CpCodeMgr.GetStockListedDate(code),
            'maxprice': self.obj_CpUtil_CpCodeMgr.GetStockMaxPrice(code),
            'minprice': self.obj_CpUtil_CpCodeMgr.GetStockMinPrice(code),
            'ydopen': self.obj_CpUtil_CpCodeMgr.GetStockYdOpenPrice(code),
            'ydhigh': self.obj_CpUtil_CpCodeMgr.GetStockYdHighPrice(code),
            'ydlow': self.obj_CpUtil_CpCodeMgr.GetStockYdLowPrice(code),
            'ydclose': self.obj_CpUtil_CpCodeMgr.GetStockYdClosePrice(code),
            'creditenabled': self.obj_CpUtil_CpCodeMgr.IsStockCreditEnable(code),
            'parpricechangetype': self.obj_CpUtil_CpCodeMgr.GetStockParPriceChageType(code),
            'spac': self.obj_CpUtil_CpCodeMgr.IsSPAC(code),
            'biglisting': self.obj_CpUtil_CpCodeMgr.IsBigListingStock(code),
            'groupname': self.obj_CpUtil_CpCodeMgr.GetGroupName(code),
            'industryname': self.obj_CpUtil_CpCodeMgr.GetIndustryName(code),
            'membername': self.obj_CpUtil_CpCodeMgr.GetMemberName(code),
        }

        _fields = [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 116, 118, 120, 123, 124, 125, 127, 156]
        _keys = ['PER', '시간외매수잔량', '시간외매도잔량', 'EPS', '자본금', '액면가', '배당률', '배당수익률', '부채비율', '유보율', '자기자본이익률', '매출액증가율', '경상이익증가율', '순이익증가율', '투자심리', 'VR', '5일회전율', '4일종가합', '9일종가합', '매출액', '경상이익', '당기순이익', 'BPS', '영업이익증가율', '영업이익', '매출액영업이익률', '매출액경상이익률', '이자보상비율', '분기BPS', '분기매출액증가율', '분기영업이액증가율', '분기경상이익증가율', '분기순이익증가율', '분기매출액', '분기영업이익', '분기경상이익', '분기당기순이익', '분개매출액영업이익률', '분기매출액경상이익률', '분기ROE', '분기이자보상비율', '분기유보율', '분기부채비율', '프로그램순매수', '당일외국인순매수', '당일기관순매수', 'SPS', 'CFPS', 'EBITDA', '공매도수량', '당일개인순매수']
        self.obj_CpSysDib_MarketEye.SetInputValue(0, _fields)
        self.obj_CpSysDib_MarketEye.SetInputValue(1, code)
        self.obj_CpSysDib_MarketEye.BlockRequest()

        cnt_field = self.obj_CpSysDib_MarketEye.GetHeaderValue(0)
        if cnt_field > 0:
            for i in range(cnt_field):
                stock[_keys[i]] = self.obj_CpSysDib_MarketEye.GetDataValue(i, 0)
        return stock

    def get_chart(self, code, target='A', unit='D', n=None, date_from=None, date_to=None):
        """
        https://money2.creontrade.com/e5/mboard/ptype_basic/HTS_Plus_Helper/DW_Basic_Read_Page.aspx?boardseq=284&seq=102&page=1&searchString=StockChart&p=8841&v=8643&m=9505
        "전일대비"는 제공하지 않으므로 직접 계산해야 함
        target: 'A', 'U' == 종목, 업종
        unit: 'D', 'W', 'M', 'm', 'T' == day, week, month, min, tick
        return <dict>dict_chart
        """
        _fields = []
        _keys = []
        if unit == 'm':
            _fields = [0, 1, 2, 3, 4, 5, 6, 8, 9, 37]
            _keys = ['date', 'time', 'open', 'high', 'low', 'close', 'diff', 'volume', 'price', 'diffsign']
        else:
            _fields = [0, 2, 3, 4, 5, 6, 8, 9, 37]
            _keys = ['date', 'open', 'high', 'low', 'close', 'diff', 'volume', 'price', 'diffsign']

        if date_to is None:
            date_to = util.get_str_today()

        self.obj_CpSysDib_StockChart.SetInputValue(0, target+code) # 주식코드: A, 업종코드: U
        if n is not None:
            self.obj_CpSysDib_StockChart.SetInputValue(1, ord('2'))  # 0: ?, 1: 기간, 2: 개수
            self.obj_CpSysDib_StockChart.SetInputValue(4, n)  # 요청 개수
        if date_from is not None or date_to is not None:
            if date_from is not None and date_to is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(1, ord('1'))  # 0: ?, 1: 기간, 2: 개수
            if date_from is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(3, date_from)  # 시작일
            if date_to is not None:
                self.obj_CpSysDib_StockChart.SetInputValue(2, date_to)  # 종료일
        self.obj_CpSysDib_StockChart.SetInputValue(5, _fields)  # 필드
        self.obj_CpSysDib_StockChart.SetInputValue(6, ord(unit))
        self.obj_CpSysDib_StockChart.SetInputValue(9, ord('1')) # 0: 무수정주가, 1: 수정주가

        def req(prev_result):
            self.obj_CpSysDib_StockChart.BlockRequest()

            status = self.obj_CpSysDib_StockChart.GetDibStatus()
            msg = self.obj_CpSysDib_StockChart.GetDibMsg1()
            if status != 0:
                return None

            cnt = self.obj_CpSysDib_StockChart.GetHeaderValue(3)
            list_item = []
            for i in range(cnt):
                dict_item = {k: self.obj_CpSysDib_StockChart.GetDataValue(j, cnt-1-i) for j, k in enumerate(_keys)}
                
                # type conversion
                dict_item['diffsign'] = chr(dict_item['diffsign'])
                for k in ['open', 'high', 'low', 'close', 'diff']:
                    dict_item[k] = float(dict_item[k])
                for k in ['volume', 'price']:
                    dict_item[k] = int(dict_item[k])

                # additional fields
                dict_item['diffratio'] = (dict_item['diff'] / (dict_item['close'] - dict_item['diff'])) * 100
                list_item.append(dict_item)
            return list_item

        # 연속조회 처리
        result = req([])
        while self.obj_CpSysDib_StockChart.Continue:
            self.wait()
            _list_item = req(result)
            if len(_list_item) > 0:
                result = _list_item + result
                if n is not None and n <= len(result):
                    break
            else:
                break
        return result

    def get_shortstockselling(self, code, n=None):
        """
        종목별공매도추이
        """
        if not self.connected():
            return None
        _fields = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        _keys = ['date', 'close', 'diff', 'diffratio', 'volume', 'short_volume', 'short_ratio', 'short_amount', 'avg_price', 'avg_price_ratio']

        self.obj_CpSysDib_CpSvr7238.SetInputValue(0, 'A'+code) 
        
        def req(prev_result):
            self.obj_CpSysDib_CpSvr7238.BlockRequest()

            status = self.obj_CpSysDib_CpSvr7238.GetDibStatus()
            msg = self.obj_CpSysDib_CpSvr7238.GetDibMsg1()
            if status != 0:
                return None

            cnt = self.obj_CpSysDib_CpSvr7238.GetHeaderValue(0)
            list_item = []
            for i in range(cnt):
                dict_item = {k: self.obj_CpSysDib_CpSvr7238.GetDataValue(j, cnt-1-i) for j, k in enumerate(_keys)}
                list_item.append(dict_item)
            return list_item

        # 연속조회 처리
        result = req([])
        while self.obj_CpSysDib_CpSvr7238.Continue:
            self.wait()
            _list_item = req(result)
            if len(_list_item) > 0:
                result = _list_item + result
                if n is not None and n <= len(result):
                    break
            else:
                break
        return result

    def get_balance(self, account):
        """
        매수가능금액
        """
        self.obj_CpTrade_CpTdUtil.TradeInit()
        self.obj_CpTrade_CpTdNew5331A.SetInputValue(0, account)
        self.obj_CpTrade_CpTdNew5331A.BlockRequest()
        v = self.obj_CpTrade_CpTdNew5331A.GetHeaderValue(10)
        return v

    def get_holdingstocks(self, account):
        """
        보유종목
        """
        self.obj_CpTrade_CpTdUtil.TradeInit()
        self.obj_CpTrade_CpTdNew5331B.SetInputValue(0, account)
        self.obj_CpTrade_CpTdNew5331B.SetInputValue(3, ord('1')) # 1: 주식, 2: 채권
        self.obj_CpTrade_CpTdNew5331B.BlockRequest()
        cnt = self.obj_CpTrade_CpTdNew5331B.GetHeaderValue(0)
        res = []
        for i in range(cnt):
            item = {
                'code': self.obj_CpTrade_CpTdNew5331B.GetDataValue(0, i),
                'name': self.obj_CpTrade_CpTdNew5331B.GetDataValue(1, i),
                'holdnum': self.obj_CpTrade_CpTdNew5331B.GetDataValue(6, i),
                'buy_yesterday': self.obj_CpTrade_CpTdNew5331B.GetDataValue(7, i),
                'sell_yesterday': self.obj_CpTrade_CpTdNew5331B.GetDataValue(8, i),
                'buy_today': self.obj_CpTrade_CpTdNew5331B.GetDataValue(10, i),
                'sell_today': self.obj_CpTrade_CpTdNew5331B.GetDataValue(11, i),
            }
            res.append(item)
        return res