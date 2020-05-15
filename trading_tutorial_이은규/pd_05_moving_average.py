import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# start와 end를 직접 입력
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
print(gs.head())

ma5 = gs['Adj Close'].rolling(window=5).mean()
print(ma5.tail(10))

new_gs = gs[gs['Volume'] != 0]
print(new_gs.tail(5))

ma5 = new_gs['Adj Close'].rolling(window=5).mean()      # 5일 이동평균
# DF.insert(추가될 컬럼 위치, 컬럼 이름, 데이터)
new_gs.insert(len(new_gs.columns), "MA5", ma5)

ma20 = new_gs['Adj Close'].rolling(window=20).mean()    # 20일 이동평균
ma60 = new_gs['Adj Close'].rolling(window=60).mean()    # 60일 이동평균
ma120 = new_gs['Adj Close'].rolling(window=120).mean()  # 120일 이동평균

new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

print(new_gs)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()
