from sma import SMA
from ema import EMA
import pandas as pd
from matplotlib import pyplot as plt

# returns MACD = SMA(df,t1) - SMA(df,t2) as well as EMA(MACD,9) in a tuple
def MACD(df,t1=12,t2=26):
    if t1 > t2:
        tmp = t1
        t1 = t2
        t2 = tmp
    sma1 = SMA(df,t1)
    sma2 = SMA(df,t2)
    temp = pd.Series(sma1-sma2,index = df.index)
    signal = EMA(temp[t2:],9)
    return temp, signal

"""
df = pd.read_csv('NHPC.csv')
df = df.set_index('Date')
df['MACD'], df['MACD_Signal'] = MACD(df['Close'],2,4)
#df['MACD_Signal'] = EMA(df['MACD'][26:],9)
print(df['MACD_Signal'])
#plt.plot(df['Close'],'blue')
plt.plot(df['MACD'],'black')
plt.plot(df['MACD_Signal'],'red')
plt.show()
"""
