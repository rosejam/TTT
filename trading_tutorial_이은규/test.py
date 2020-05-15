import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker
from zipline.api import order_target, record, symbol
from zipline.algorithm import TradingAlgorithm

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 3, 29)
data = web.DataReader("AAPL", "yahoo", start, end)

#plt.plot(data.index, data['Adj Close'])
#plt.show()

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

#print(data.head())

def initialize(context):
    context.i = 0
    context.sym = symbol('AAPL')

def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return

    ma5 = data.history(context.sym, 'price', 5, '1d').mean()
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()

    if ma5 > ma20:
        order_target(context.sym, 1)
    else:
        order_target(context.sym, -1)

    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result['portfolio_value'])
result['portfolio_value'].plot()
plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()