
# coding: utf-8

# In[4]:

get_ipython().system('pip install nsepy')


# In[49]:

import datetime


# In[5]:

from nsepy import get_history


# In[14]:

get_ipython().set_next_input('df = get_history');get_ipython().magic('pinfo get_history')


# In[ ]:

df = get_history


# In[ ]:

df = get_history


# In[22]:

df = get_history(symbol='SBIN', start = datetime.date(2014,1,1), end = datetime.date(2019,5,27))


# In[53]:

df.head()


# In[68]:

df[datetime.date(2015,1,1):]['Close'].plot()


# In[35]:

df.to_csv('SBIN.csv')


# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

df = pd.read_csv('SBIN.csv')


# In[4]:

df = df.reset_index()


# In[5]:

df['Date'] = pd.to_datetime(df['Date'])


# In[35]:

df = df.set_index('Date')


# In[9]:

df = df[datetime.date(2014,11,21):]


# Adding some features

# In[70]:

df['day_range'] = df['High'] - df['Low']
df['net_change'] = df['Close'] - df['Prev Close']
df['pcnt_chg'] = df['Close']/df['Prev Close']
df['day_range_pcnt_chg'] = df['day_range']/ df['Prev Close']


# In[73]:

df.Open.values, df.Volume.values


# In[90]:

np.corrcoef(df.Open.values,df.Volume.values)[0,1]


# In[92]:

df['open_vol_corr_10'] = df['Open'].rolling(10).corr(df['Volume'])


# In[93]:

import matplotlib as plt


# In[108]:

fig, ax1 = plt.pyplot.subplots()
plt.pyplot.plot(df['Close'], label = 'Close')
ax2 = ax1.twinx()
ax2.plot(df['open_vol_corr_10'], label = 'alpha', color = 'tab:red' )
plt.pyplot.figure(figsize= (20,100))


# In[10]:

df[datetime.date(2016,4,1):datetime.date(2016,5,1)]


# In[116]:

#whenever 'open_vol_corr_10' changes sign, the stock sees a reversion, a positive coorelation indicates a buy signal in price


# In[12]:

from matplotlib.finance import candlestick_ohlc


# In[6]:

df.head()


# In[7]:

import matplotlib.dates as mdates


# In[8]:

import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc


# In[73]:

import matplotlib.ticker as mticker


# In[79]:

date = df.Date.values


# In[87]:

fig = plt.figure()
f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=6, colspan=4)
candlestick_ohlc(f1, df1.values,width=1/len(df1)*0.6, colorup='k', colordown='r', alpha=0.75)


ax2 = plt.subplot2grid((5,4), (4,0), sharex=f1, rowspan=1, colspan=4)
ax2.bar(range(len(date)), df.Volume.values)
ax2.axes.yaxis.set_ticklabels([])
plt.ylabel('Volume')
ax2.grid(True)
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)
    
f1.xaxis.set_major_locator(mticker.MaxNLocator(10))
f1.xaxis.set_major_formatter(Jackarow('%Y-%m-%d'))
plt.show()


# In[9]:

df1 = df[['Date','Open', 'High', 'Low', 'Close', 'Volume']][-10:]


# In[10]:

df1["Date"] = df1["Date"].apply(mdates.date2num)


# In[60]:

f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=10, colspan=8)
candlestick_ohlc(f1, df1.values,width=1/len(df1)*0.6, colorup='g', colordown='r', alpha=0.75)
plt.axis('off')
fig1 = plt.gcf()
plt.show()
fig1.savefig("test.png", dpi = 100)


# In[26]:

df['Close_t3'] = df['Close'].shift(-3)


# In[30]:

df['pcnt_chg_t3'] = round(df['Close_t3'] /df['Close'] - 1,2)


# In[59]:

df['pcnt_chg_t3'].value_counts()


# In[44]:

a = df[df['pcnt_chg_t3'] >= 0.03 ].index[1]


# In[54]:

df[a -datetime.timedelta(days=20):a].shape


# In[ ]:



