from yahooquery import Ticker
from yahooquery import Screener
import pandas as pd

# トヨタ自動車(7203.T)の銘柄シンボルを指定して、Tickerオブジェクトを作成する
ticker_num = '7203.T'
ticker_data = Ticker(ticker_num)

