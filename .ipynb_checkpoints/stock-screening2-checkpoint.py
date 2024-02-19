# ライブラリを読み込む
from yahooquery import Ticker
from yahooquery import Screener
import pandas as pd

# トヨタ自動車(7203.T)の銘柄シンボルを指定して、Tickerオブジェクトを作成する
ticker_num = '7203.T'
ticker_data = Ticker(ticker_num)

# 貸借対照表を取得する
# 取得したデータはDataframe形式
ticker_balance_sheet = ticker_data.balance_sheet()
ticker_balance_sheet.to_csv('balance_sheet.csv')

# キャッシュ・フローを取得する
# 取得したデータはDataframe形式
ticker_cash_flow = ticker_data.cash_flow()
ticker_cash_flow.to_csv('cash_flow.csv')

# 損益計算書を取得する
# 取得したデータはDataframe形式
ticker_income_statement = ticker_data.income_statement()
ticker_income_statement.to_csv('income_statement.csv')

# 評価指標を取得する
# 取得したデータはDataframe形式
ticker_valuation_measures = ticker_data.valuation_measures
ticker_valuation_measures.to_csv('valuation_measures.csv')

# 財務情報を取得する
# 取得したデータは辞書形式
# Dataframe形式に変換してCSVに保存する
ticker_financial_data = ticker_data.financial_data
df_Series_ticker_financial_data = {}
for k, v in ticker_financial_data.items():
    df_Series_ticker_financial_data = pd.Series(v)

df_ticker_financial_data = pd.DataFrame(df_Series_ticker_financial_data)
df_ticker_financial_data.T.to_csv('financial_data.csv')

# 条件を満たす銘柄を抽出する
# most_actives:最も取引が活発な銘柄
# day_gainers:当日の上昇率
# 5:それぞれの条件の上位5銘柄
# 取得したデータは辞書形式
# Dataframe形式に変換してCSVに保存する
s = Screener()
s_get_screeners = s.get_screeners(['most_actives', 'day_gainers'], 5)
df_Series_s_get_screeners = {}
for k, v in s_get_screeners.items():
    df_Series_s_get_screeners = pd.Series(v)

df_s_get_screeners = pd.DataFrame(df_Series_s_get_screeners)
df_s_get_screeners.T.to_csv('screeners.csv')
