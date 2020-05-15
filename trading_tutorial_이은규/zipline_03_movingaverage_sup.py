"""
골든크로스/데드크로스 시점에서만 매수/매도가 이뤄지도록 보완
"""
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 29)
data = web.DataReader("AAPL", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')
    context.hold = False    # 주식 보유 여부에 대한 정보를 저장하는 용도의 변수. 시뮬레이션 초기화 시점에서는 주식을 보유하지 않고 있기 때문에 False

def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return

    buy = False     # 해당 거래일 매수 여부
    sell = False    # 해당 거래일 매도 여부

    ma5 = data.history(context.sym, 'price', 5, '1d').mean()
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()

    # 골든크로스 발생 시 100주 매수
    if ma5 > ma20 and context.hold == False:
        order_target(context.sym, 100)
        context.hold = True
        buy = True
    # 데드크로스 발생 시 100주 매도
    elif ma5 < ma20 and context.hold == True:
        order_target(context.sym, -100)
        context.hold = False
        sell = True

    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20, buy=buy, sell=sell)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result.portfolio_value)
plt.plot(result.index, result.portfolio_value)
plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

plt.plot(result.index, result.ma5)
plt.plot(result.index, result.ma20)
plt.legend(loc='best')
plt.plot(result.ix[result.buy == True].index, result.ma5[result.buy == True], '^')      # 매수 시점 ▲
plt.plot(result.ix[result.sell == True].index, result.ma5[result.sell == True], 'v')    # 매도 시점 ▼

plt.show()