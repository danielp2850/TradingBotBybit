import pandas as pd
import pandas_ta as ta
import yfinance as yf
from lightweight_charts import Chart

def calculate_sma(df, period: int = 50):
    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': df['close'].rolling(window=period).mean()
    }).dropna()

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

    chart.set(df)

    # add sma line
    line = chart.create_line('SMA 50')
    sma_data = calculate_sma(df, period=50)
    line.set(sma_data)

    # chart.watermark(tickers[0])
    
    chart.show(block=True)