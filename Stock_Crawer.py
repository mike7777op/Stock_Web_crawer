import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data

#設定爬蟲股票代號
# sid = '0050'

def stock_crawler(sid):
    #設定爬蟲時間
    start = datetime.datetime.now() - datetime.timedelta(days=180)
    end = datetime.date.today()

    #----------pandas_datareader套件教學--------------------------
    #導入pandas_datareader


    # 與yahoo請求，套件路徑因版本不同
    pd.core.common.is_list_like = pd.api.types.is_list_like 

    # 取得股票資料
    stock_dr = data.get_data_yahoo(sid+'.TW', start, end)
    st = stock_dr.tail(10)
    # print(type(st))
    return st

#線型圖，收盤價、5日均線、20日均線、60日均線
# stock_dr['Adj Close'].plot(figsize=(16, 8))
# stock_dr['Adj Close'].rolling(window=5).mean().plot(figsize=(16, 8), label='5_Day_Mean')
# stock_dr['Adj Close'].rolling(window=20).mean().plot(figsize=(16, 8), label='20_Day_Mean')
# stock_dr['Adj Close'].rolling(window=60).mean().plot(figsize=(16, 8), label='60_Day_Mean')

# #顯示側標
# plt.legend(loc='upper right', shadow=True, fontsize='x-large')

# #顯示標題
# plt.title(sid+'_datareader')

def main():
    sid = str(input("請輸入證券代號:"))
    tt = stock_crawler(sid)
    # print(type(tt))
    tt = tt.loc["2021-12-30",["High", "Low", "Open", "Close"]]
    tt = tt.tolist()
    print(tt[3])

if __name__ == "__main__":
    main()
