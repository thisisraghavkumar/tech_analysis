from sma import SMA
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def EMA(df,n):
    temp_sma = SMA(df,n)
    sma = temp_sma.iloc[n-1]
    mul = 2/(n+1)
    tmp = []
    for i in range(0,len(df)):
        if i>=n:
            tmp.append((df[i]-tmp[i-1])*mul + tmp[i-1])
        elif i == n-1:
            tmp.append(sma)
        else:
            tmp.append(np.nan)
    tmp = pd.Series(np.array(tmp),index=df.index)
    return tmp

"""
df = pd.read_csv('NHPC.csv', encoding='utf-8')
df = df.set_index('Date')
sma = SMA(df['Close'],9)
ema = EMA(df['Close'],9)
df['SMA'] = sma
df['EMA'] = ema

print(df[['SMA','EMA']])
print("EMA : "+str(ema.index))
print("SMA : "+str(sma.index))

plt.plot(df['Close'],'r')
plt.plot(df['SMA'],'g')
plt.plot(df['EMA'],'b')
plt.show()
    
"""
