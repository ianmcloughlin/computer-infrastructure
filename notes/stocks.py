#! /usr/bin/env python

# Dates and times.
import datetime as dt

# Yahoo Finance data.
import yfinance as yf

# Get historical data for multiple tickers at once.
df = yf.download('MSFT AAPL GOOG NVDA', period='1mo')

# Get the current date and time.
now = dt.datetime.now()

# File name.
filename = "data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save data to file.
df.to_csv(filename)