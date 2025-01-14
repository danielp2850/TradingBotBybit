import pandas_ta as ta
import pandas as pd
from backtesting import Backtest
from backtesting import Strategy
from backtesting.lib import crossover, barssince
from backtesting.test import GOOG

# Klines is the candles of some symbol (up to 1500 candles). Dataframe, last elem has [-1] index
def klines(symbol):
    try:
        resp = session.get_kline(
            category='linear',
            symbol=symbol,
            interval=timeframe,
            limit=500
        )['result']['list']
        resp = pd.DataFrame(resp)
        resp.columns = ['Time', 'Open', 'High',
                        'Low', 'Close', 'Volume', 'Turnover']
        resp = resp.set_index('Time')
        resp = resp.astype(float)
        resp = resp[::-1]
        return resp
    except Exception as err:
        print(err)

# Bollinger Bands strategy
def bollinger_bands_signal(symbol):
    kl = klines(symbol)
    bb = ta.volatility.BollingerBands(kl.Close)
    kl['bb_high'] = bb.bollinger_hband()
    kl['bb_low'] = bb.bollinger_lband()
    kl['bb_mid'] = bb.bollinger_mavg()

    if kl.Close.iloc[-1] < kl.bb_low.iloc[-1] and kl.Close.iloc[-2] >= kl.bb_low.iloc[-2]:
        return 'up'
    if kl.Close.iloc[-1] > kl.bb_high.iloc[-1] and kl.Close.iloc[-2] <= kl.bb_high.iloc[-2]:
        return 'down'
    else:
        return 'none'
    

class RsiOscillator(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # All initial calculations
    def init(self):
        self.daily_rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)

    def next(self):

        price = self.data.Close[-1]

        if self.daily_rsi[-1] > self.upper_bound and barssince(self.daily_rsi < self.upper_bound == 3):
            self.position.close()

        elif crossover(self.lower_bound, self.daily_rsi):
            self.buy()



bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)
stats = bt.run()

# print(stats['_trades'].to_string())

bt.plot()