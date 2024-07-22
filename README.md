# Trading Bot

A Python-based trading bot that uses the Bybit API to execute trading strategies based on technical indicators. This bot performs automated trading on Bybit's derivatives market using predefined strategies.

## Features

- **Real-time Trading**: Executes trades based on technical indicators like RSI and Williams %R.
- **Order Management**: Places market orders with configurable take-profit and stop-loss.
- **Position Management**: Monitors open positions and available balance.
- **Performance Tracking**: Retrieves and displays historical profit and loss data.

## Requirements

- Python 3.7+
- `pybit` library for Bybit API integration
- `pandas` for data manipulation
- `ta` for technical analysis indicators

You can install the required libraries using:

```bash
pip install pybit pandas ta


Configuration
API Keys: Store your Bybit API keys in a keys.py file. This file should contain the following variables:

python
Copy code
api = 'YOUR_API_KEY'
secret = 'YOUR_API_SECRET'
Environment Setup: Add the keys.py file to .gitignore to ensure it is not pushed to version control.

Add the following line to your .gitignore file:

plaintext
Copy code
keys.py
Usage
Setup API: Ensure your Bybit API keys are correctly configured in keys.py.

Run the Script: Execute the script using Python:

bash
Copy code
python trading_bot.py
Monitor Output: The bot will output trading actions and performance metrics to the terminal.

Strategies
RSI Strategy: Utilizes the Relative Strength Index (RSI) to generate buy/sell signals.
Williams %R Strategy: Uses the Williams %R indicator to generate buy/sell signals.
Configuration Parameters
tp (Take Profit): Percentage gain to take profit. Default is 0.012 (1.2%).
sl (Stop Loss): Percentage loss to stop loss. Default is 0.009 (0.9%).
timeframe: Time interval for candles in minutes. Default is 15 minutes.
mode: Margin mode (1 for Isolated, 0 for Cross). Default is 1.
leverage: Leverage used for trading. Default is 10.
qty: Amount of USDT to trade per order. Default is 50.
Security
API Keys: Ensure API keys are kept private and not exposed in version control.
Sensitive Information: Regularly review and rotate API keys for enhanced security.
```
