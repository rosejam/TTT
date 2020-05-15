import pandas_datareader.data as web
import matplotlib.pyplot as plt

gs = web.DataReader("078930.KS", "yahoo")

print(gs)

print(gs.info())
print(gs.index)

plt.plot(gs['Adj Close'])
plt.show()

plt.plot(gs.index, gs['Adj Close'])
plt.show()
