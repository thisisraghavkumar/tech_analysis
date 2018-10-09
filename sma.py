import pandas as pd
from matplotlib import pyplot as plt

#returns a series of n-period SMA values for pd.Series df 
def SMA(df,n):
    sma = pd.Series(df.rolling(window=n).mean())
    return sma


"""
df = pd.read_csv('NHPC.csv', encoding='utf-8')
df = df.set_index('Date')
sma26 = SMA(df,'Close',26)
sma12 = SMA(df,'Close',12)
sma9 =  SMA(df,'Close',9)
MACD = sma12-sma26
df['base'] = 0
plt.plot(MACD,color='b')
plt.plot(df['base'],color='r')
plt.plot([0])
plt.show()
"""
