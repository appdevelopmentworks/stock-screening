import pandas as pd
import datetime
import logging

logging.basicConfig(level=logging.INFO)
save_dir = './stockdata/'
base_url = 'https://finance.yahoo.co.jp/stocks/ranking/listingDate?market=all&term=daily&page='
#27ページ取り込み(50*26=1300件)
intPage = 26

#データフレーム生成
df = pd.DataFrame()
#取り込み
for i in range(1, intPage + 1):
    #走査するURLの組み立て
    url = base_url + str(i)
    try:
        #読み込んで０番目（データ入っている）の表を連結していく
        dft = pd.read_html(url)
        df = pd.concat([df, dft[0]])
    except ValueError as ex:
        logging.error(ex)

#インデックスを順位に変更
df = df.reset_index()
df.set_index('順位')

#'TPM','名証','札幌','福証','東証'
intCnt = 0
kubuns = ['東証','名証','札','福','TPM']
code = []
sname = []
sijyou = []

#名称・コード・市場の内容を分割し配列に入れる
for datam in df['名称・コード・市場'].to_list():
  for kubun in kubuns:
    idxnum = datam.find(kubun)
    if idxnum > 0:
      code.append(datam[idxnum-4:idxnum])
      sname.append(datam[:idxnum-4])
      sijyou.append(datam[idxnum:-3])
      intCnt = intCnt +1
#配列をシリーズに追加
df['コード'] = code
df['名称'] = sname
df['市場'] = sijyou

#---,',',百万円を置き換え
df['時価総額'] = [datam.replace('百万円','').replace(',','').replace('---','0') for datam in df['時価総額(百万円)'].to_list()]
#数値型に変換
df['時価総額'] = df['時価総額'].astype(int)
#下５文字（15:00）と','を削除
df['取引値'] = [datam[:-5].replace(',','') for datam in df['取引値'].to_list()]
#float型に変換
df['取引値'] = df['取引値'].astype(float)
#日付型に変換
df['上場年月日'] = pd.to_datetime(df['上場年月日'])
#列の並び替え
df = df.reindex(columns=['順位', 'コード', '名称', '市場', '時価総額', '上場年月日', '取引値', '決算年月'])
#CSVに書き出し
today = datetime.datetime.now()
filename = save_dir + str(today.date()).replace('-','') + '上場年度順.csv'
df.to_csv(filename)
