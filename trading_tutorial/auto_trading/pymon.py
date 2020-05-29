import sys
from PyQt5.QtWidgets import *
import Kiwoom
import time
from pandas import DataFrame
import datetime

MARKET_KOSPI   = 0
MARKET_KOSDAQ  = 10

class PyMon:
    def __init__(self):
        self.kiwoom = Kiwoom.Kiwoom()
        self.kiwoom.comm_connect()
        self.get_code_list()

    # 유가증권시장과 코스닥시장의 종목코드 리스트
    def get_code_list(self):
        self.kospi_codes = self.kiwoom.get_code_list_by_market(MARKET_KOSPI)
        self.kosdaq_codes = self.kiwoom.get_code_list_by_market(MARKET_KOSDAQ)

    # 오늘 날짜를 시작으로 과거 거래일별로 시가, 고가, 저가, 종가, 거래량을 가져오는 메서드
    def get_ohlcv(self, code, start):
        self.kiwoom.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}

        self.kiwoom.set_input_value("종목코드", code)
        self.kiwoom.set_input_value("기준일자", start)
        self.kiwoom.set_input_value("수정주가구분", 1)
        self.kiwoom.comm_rq_data("opt10081_req", "opt10081", 0, "0101")
        time.sleep(0.2)     # TR을 요청할 때 0.2초 간격을 주기 위해 time 모듈을 사용

        df = DataFrame(self.kiwoom.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'],
                       index=self.kiwoom.ohlcv['date'])
        return df

    def check_speedy_rising_volume(self, code):
        """
        급등주 포착 알고리즘
        : 특정 거래일의 거래량이 이전 시점의 평균 거래량보다 1,000% 이상 급증하는 종목을 매수
        : 급등주면 True, 아니면 False 반환

        - 이전 시점의 평균 거래량: 특정 거래일 이전의 20일(거래일 기준) 동안의 평균 거래량
        - 거래량 급증: 특정 거래일의 거래량이 평균 거래량보다 1,000% 초과
        - 위의 정의는 '저자의 정의'일 뿐, 알고리즘 구현은 다르게 해도 됨
        """
        today = datetime.datetime.today().strftime("%Y%m%d")
        df = self.get_ohlcv(code, today)
        volumes = df['volume']

        # 조회 시작일을 기준으로 이전 20일간 거래량의 평균을 계산해야 하므로 총 21일 치의 데이터가 필요
        # 상장된지 21일 미만이면 데이터가 충분치 않을 수 있으므로 거름
        if len(volumes) < 21:
            return False

        sum_vol20 = 0   # 일별 거래량 누적
        today_vol = 0   # 조회 시작일의 거래량

        for i, vol in enumerate(volumes):
            if i == 0:
                today_vol = vol
            elif 1 <= i <= 20:
                sum_vol20 += vol
            else:   # 21일치 넘어가면 break
                break

        avg_vol20 = sum_vol20 / 20
        if today_vol > avg_vol20 * 10:
            return True

    def update_buy_list(self, buy_list):
        f = open("buy_list.txt", "wt")
        for code in buy_list:
            f.writelines("매수;", code, ";시장가;10;0;매수전")      # 예시를 단순화하기 위해 10주씩으로 설정했지만 이런 부분들은 나중에 수정
        f.close()

    def run(self):
        buy_list = []
        num = len(self.kosdaq_codes)

        for i, code in enumerate(self.kosdaq_codes):
            print(i, '/', num)
            if self.check_speedy_rising_volume(code):
                print("급등주:", code)
                buy_list.append(code)

        self.update_buy_list(buy_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    pymon.run()