#! /usr/bin/env python

# Dates and times.
import datetime as dt

# Yahoo Finance data.
import yfinance as yf

# Get data.
df = yf.download(['MSFT', 'AAPL', 'GOOG'], period='5d', interval='1h')

# Current date and time.
now = dt.datetime.now()

# File name.
filename = "../data/" + now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save data as CSV.
df.to_csv(filename)
