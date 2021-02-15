
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2020,1,15)
end = datetime.datetime(2021,2,15)

gs = web.DataReader("078930.KS","yahoo",start,end)

ma5 = gs["Adj Close"].rolling(window=5).mean()
ma20 = gs["Adj Close"].rolling(window=20).mean()
ma60 = gs["Adj Close"].rolling(window=60).mean()
ma120 = gs["Adj Close"].rolling(window=120).mean()
gs.insert(len(gs.columns),"MA5",ma5)
gs.insert(len(gs.columns),"MA20",ma20)
gs.insert(len(gs.columns),"MA60",ma60)
gs.insert(len(gs.columns),"MA120",ma120)

plt.plot(gs.index,gs['MA5'], label="MA5")
plt.plot(gs.index,gs['MA20'], label="MA20")
plt.plot(gs.index,gs['MA60'], label="MA60")
plt.plot(gs.index,gs['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()
type(plt)