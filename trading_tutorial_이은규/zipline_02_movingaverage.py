"""
주가 이동평균선을 이용하는 대표적인 기술적 분석 지표
- 골든 크로스(golden cross)
    - 단기 이동평균선이 중·장기 이동평균선을 아래에서 위로 상향 돌파하면서 생기는 교차점
    - 최근 주가의 흐름이 강세로 접어들었음을 의미

- 데드 크로스(dead cross)
    - 단기 이동평균선이 중·장기 이동평균선을 위에서 아래로 하향 돌파하면서 생기는 교차점
    - 최근 주가의 흐름이 약세로 접어들었음을 의미

- 단기 이동평균선(5일) + 중장기 이동평균선(20일) or (20일) + (60일)
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

#plt.plot(data.index, data['Adj Close'])
#plt.show()

data = data[['Adj Close']]
data.columns = ['AAPL']
data = data.tz_localize('UTC')

#print(data.head())

def initialize(context):
    """
    백테스트의 초기화를 담당
    :param context: 네임스페이스로서 백테스트를 수행할 때 계속해서 유지해야 할 변수를 저장하는 용도로 사용
    """
    context.i = 0                   # 거래일 수를 계산하는 데 사용
    context.sym = symbol('AAPL')    # 참조할 데이터에 대한 심볼을 저장

def handle_data(context, data):
    """
    백테스트 시뮬레이션 동안 거래일마다 호출되는 함수
    :param context: TradingAlgorithm 클래스의 인스턴스
    :param data: BarData 클래스의 인스턴스
    """
    context.i += 1
    if context.i < 20:
        return

    # BarData 클래스의 history 메소드: 일정 기간의 데이터를 얻을 수 있음
    ma5 = data.history(context.sym, 'price', 5, '1d').mean()    #  5일 주가 이동 평균값
    ma20 = data.history(context.sym, 'price', 20, '1d').mean()  # 20일 주가 이동 평균값

    # 5일 주가 이동 평균값이 20일 주가 이동 평균값보다 큰 상태일 때 1주를 매수하고, 반대면 1주를 매도
    if ma5 > ma20:
        order_target(context.sym, 1)
    else:
        order_target(context.sym, -1)

    # record(): 5일 이동 평균값, 20일 이동 평균값을 저장 -> 향후 전략을 검증하거나 코드를 디버깅할 때 활용
    record(AAPL=data.current(context.sym, "price"), ma5=ma5, ma20=ma20)

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
result = algo.run(data)

result[['ma5', 'ma20']].plot()
plt.show()

print(result['portfolio_value'])
result['portfolio_value'].plot()
plt.gca().get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()