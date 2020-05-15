import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
# zipline: 알고리즘 트레이딩 라이브러리로서 백테스팅 기능을 제공(https://github.com/quantopian/zipline)
from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

# data
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 19)
data = web.DataReader("AAPL", "yahoo", start, end)  # 애플에 대한 데이터

# 백테스팅에는 수정 종가만 사용되므로 DataFrame 객체에서 해당 칼럼만 가져오고 칼럼의 이름도 'AAPL'로 변경
data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

# Zipline 백테스팅 시뮬레이터는 시뮬레이션을 수행하기 전에 항상 initialize 함수를 호출
def initialize(context):
    """
    시뮬레이션에 사용할 초기 투자 금액이나 거래 수수료와 같은 값들을 설정
    """
    pass

# Zipline 시뮬레이터는 시뮬레이션을 수행하는 동안 거래일마다 handle_data를 호출
def handle_data(context, data):
    """
    실제 거래 알고리즘 구현
    """
    order(symbol('AAPL'), 1)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)     # 일별 매수 알고리즘 시뮬레이션 결과 바인딩

plt.plot(result.index, result.portfolio_value)  # portfolio_value: 보유 현금과 주식 평가 금액을 합산한 금액
plt.show()