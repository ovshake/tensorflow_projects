import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

style.use("ggplot")
# start = dt.datetime(2000,1,1)
# end = dt.datetime(2016,12,31)
# df = web.DataReader('TSLA','google',start,end)
# # print(df.head(100))
# df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv',parse_dates=True, index_col=0)
# print(df.head())
# df.plot()
# plt.show()
# df['Open'].plot()
# plt.show()
# print(df[['Open','High']].head(10000).plot())
# plt.show()
df['100ma'] = df['Close'].rolling(window=100,min_periods=0).mean()
df_ohlc = df['Close'].resample('10D').ohlc()
df_vol = df['Volume'].resample('10D').sum()
df_ohlc.reset_index(inplace=True)
df_ohlc["Date"] = df_ohlc['Date'].map(mdates.date2num)

print(df_ohlc.head())
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1, colspan=1, sharex = ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1,df_ohlc.values,width=1, colorup='g')
ax2.fill_between(df_vol.index.map(mdates.date2num), df_vol.values, 0)
# ax1.plot(df.index, df['Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
plt.show()


