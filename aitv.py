import pandas as pd
import yfinance as yf
from lightweight_charts import Chart

def calculate_sma(df, period: int = 50):
    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': df['close'].rolling(window=period).mean()
    }).dropna()

def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return pd.DataFrame({
        'time': df['date'],
        'RSI': rsi
    }).dropna()

if __name__ == '__main__':
    chart = Chart()
    tickers = ["BTC-USD", "XRP-USD", "EURUSD=X"]
    
    ts = yf.Ticker(tickers[0])
    df = ts.history(period="1mo", interval="5m")
    
    # Preprocess data
    df = df.drop(['Dividends', 'Stock Splits'], axis=1).reset_index()
    df.columns = df.columns.str.lower()
    df.rename(columns={'datetime': 'date'}, inplace=True)
    print(df.head())  # Fixed print statement
    
    # Set main chart with price data
    chart.set(df)
    
    # Add SMA to main chart
    sma_line = chart.create_line('SMA 50')
    sma_data = calculate_sma(df, period=50)
    sma_line.set(sma_data)
    
    # Create RSI subchart
    rsi_subchart = chart.create_subchart(position='bottom', height=0.3)
    rsi_line = rsi_subchart.create_line('RSI')
    rsi_data = calculate_rsi(df)
    rsi_line.set(rsi_data)
    
    # Show chart
    chart.show(block=True)