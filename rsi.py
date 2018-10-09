import pandas as pd
import matplotlib.pyplot as plt
from ema import EMA
def RSI(df,n):
    gain = pd.Series(index=df.index)
    loss = pd.Series(index=df.index)
    for i in range(1,len(df)):
        diff = df['Close'][i] - df['Close'][i-1]
        if diff > 0:
            gain[i] = diff
            loss[i] = 0.0
        elif diff < 0:
            loss[i] = -1*diff
            gain[i] = 0.0
        else:
            loss[i] = 0
            gain[i] = 0
    avg_gain = pd.Series(gain.rolling(n).sum()/n)
    avg_loss = pd.Series(loss.rolling(n).sum()/n)
    rs_series = avg_gain / avg_loss ;
    RSI = 100 - (100/(1+rs_series))
    return RSI

"""
df = pd.read_csv('NHPC.csv')
df = df.set_index('Date')
df['RSI'] = RSI(df,5)
plt.plot(df['RSI'])
plt.show()
"""
