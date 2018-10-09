import pandas as pd
from sma import SMA
import matplotlib.pyplot as plt

def CCI(df,n):
    tp = (df['High']+df['Low']+df['Close'])/3
    tp_sma = SMA(tp,n)
    md = 0.0
    tmp = tp-tp_sma
    ret = pd.Series(index = df.index)
    for i in range(n-1,len(tp_sma)):
        md = 0.0
        for j in range(0,n):
            md = md+abs(tp[i-j]-tp_sma[i])
        md = md/n
        ret[i] = tmp[i]/(0.015*md)
    return ret

df = pd.read_csv('NHPC.csv')
df = df.set_index('Date')

cci = CCI(df,20)
print(cci)

plt.plot(cci)
plt.show()
    
