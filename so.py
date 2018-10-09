from sma import SMA
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def SO(df,n):
    high = -1.0
    low = 1000000.0
    K = pd.Series(index=df.index)
    D = pd.Series(index=df.index)
    K[:] = np.nan
    D[:] = np.nan
    for i in range(n-1,len(df)):
        low = np.amin(df['Low'][i-n-1:i+1])
        high = np.amax(df['High'][i-n-1:i+1])
        K[df.index[i]] = (df["Close"][i]-low)/(high-low) * 100
    D = SMA(K[n-1:],3)
    return K,D

df = pd.read_csv("NHPC.csv")
df = df.set_index("Date")

df['K'], df['D'] = SO(df,10)
print(df[['K','D']])
plt.plot(df['K'],'black')
plt.plot(df['D'],'r')
plt.show()
