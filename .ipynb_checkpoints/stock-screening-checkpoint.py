import yfinance as yf

import yahoo_fin.stock_info as si 

stock = yf.Ticker("9107.T")

#print(stock.financials)
#print(stock.earnings_dates.columns)
#print(stock.history_metadata)
#print(stock.history_metadata['regularMarketPrice'])

#print(stock.ticker)


usstock = si.tickers_sp500()
stockearn = si.get_earnings("MO")

print(usstock)
