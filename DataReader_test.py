import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2020,12,1)
end = datetime.datetime(2021,2,11)

gs = web.DataReader("078930.KS","yahoo")
plt.plot(gs.index,gs['Adj Close'])
plt.show()