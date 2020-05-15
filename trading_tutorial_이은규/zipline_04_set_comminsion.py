"""
Zipline은 수수료를 따로 설정하지 않으면 기본값으로 주당 0.03달러를 사용
Zipline 모듈은 기본적으로 달러를 기준으로 동작하는데 유가증권시장/코스닥시장은 원 단위
-> 유가증권시장/코스닥시장의 데이터를 사용하는 경우 Zipline 모듈의 값도 원 단위로 간주
"""
import pandas_datareader.data as web
import datetime
from zipline.api import order, order_target, record, symbol
from zipline.algorithm import TradingAlgorithm
from zipline.api import set_commission, commission
from zipline.utils.factory import create_simulation_parameters
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 1, 31)
data = web.DataReader("078930.KS", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ['GS']
data = data.tz_localize('UTC')

def initialize(context):
    context.i = 0
    context.sym = symbol('GS')
    set_commission(commission.PerDollar(cost=0.00165))  # 매수/매도 시 수수료 0.165% 발생 -> 총 0.33%의 비용 발생
    # PerDollar는 '달러' 기준이지만 그냥 '원' 기준이라고 생각하면 됨 -> 1원당 0.00165원의 수수료 발생

def handle_data(context, data):
    # order_target(context.sym, 1)
    order(context.sym, 1)


# capital_base: 초기 투자 금액 설정
algo = TradingAlgorithm(sim_params=create_simulation_parameters(capital_base=100000), initialize=initialize, handle_data=handle_data)
result = algo.run(data)

print(result[['starting_cash', 'ending_cash', 'ending_value']])