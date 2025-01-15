import pandas as pd
import pandas_ta as ta
import yfinance as yf
from lightweight_charts import Chart

if __name__ == '__main__':
    
    chart = Chart()

    tickers = ["BTC-USD", "XRP-USD", "EURUSD=X"]
    
    ts = yf.Ticker(tickers[0])
    df = ts.history(period="1mo", interval="5m")

    # this library expects lowercase columns for date, open, high, low, close, volume
    df = df.drop(['Dividends', 'Stock Splits'], axis=1).reset_index()
    df.columns = df.columns.str.lower()
    df.rename(columns={'datetime': 'date'}, inplace=True)
    print(df.head)

    # prepare indicator values
    sma = df.ta.sma(length=20).to_frame()
    sma = sma.reset_index()
    sma = sma.rename(columns={"Date": "time", "SMA_20": "value"})
    sma = sma.dropna()
    print(sma)

    chart.set(df)

    # add sma line
    line = chart.create_line()    
    line.set(sma)

    # chart.watermark(tickers[0])
    
    chart.show(block=True)