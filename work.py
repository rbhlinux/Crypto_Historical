import requests
import pandas as pd
import math

api_url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=BTC&market=USD&interval=15min&outputsize=full&apikey=HCT1N30HAZYV8V1G'
df = requests.get(api_url).json()

df = pd.DataFrame(df['Time Series Crypto (15min)']).T
def twozeros(floatt):
    format_float = "{:.2f}".format(floatt)
    return format_float

lopen = []
lclose = []
llow = []
lhigh = []
list_dbhl = []
list_perc = []

for i in df.columns:
    df[i] = df[i].astype(float)
dfopen = df['1. open']
dfhigh = df['2. high']
dflow = df['3. low']
dfclose = df['4. close']
dfclose2 = df['4. close']

####
#DF close percen diff
dfclose2 = dfclose2.diff()
dfclose2 = dfclose2.fillna(0)

#####
for i in range(0,len(df)):
    open1 = dfopen[i]
    high = dfhigh[i]
    low = dflow[i]
    close = dfclose[i]
    diff = high -low
    perc = (diff/low)*100
    diff = twozeros(diff)
    perc = str(twozeros(perc) + "%")
    
    lhigh.append(high)
    llow.append(low)
    lopen.append(open1)
    lclose.append(close)
    list_dbhl.append(diff)
    list_perc.append(perc)
    


df1 =pd.concat([df,dfclose2],ignore_index=True,sort=False,axis=1)

df_dbhl = pd.DataFrame(list_dbhl,index=df1.index)
df_perc = pd.DataFrame(list_perc,index=df1.index)

df2 =pd.concat([df1,df_dbhl,df_perc],ignore_index=True,sort=False,axis=1)
columnnames = ["Open","High","Low","Close","Volume","DBClose","DBHL","PCHL"]
df2.columns = columnnames
print(df2)
df2.to_csv('C:\\Users\\ansible\\Documents\\test.csv', sep='\t', encoding='utf-8')
