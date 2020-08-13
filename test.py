
import pandas as pd
import arrow
date = arrow.utcnow().format('YYYY-MM-DD')
fileName = 'J:\\我的坚果云\\时计-20-08-12.xlsx'
df = pd.read_excel(fileName,'时计')
df['日期'] = pd.to_datetime(df['日期'],format="%Y-%m-%d")
df1 = df[(df.状态 == '✔')&(df.日期==date)]
df2 = df1.loc[:,['类型','用时']]
df2['用时'] =  [int(x.replace('min','').strip()) for x in df2['用时']]
df3 = df2.groupby(['类型']).sum().reset_index()
df3 = df3.sort_values(by='用时')
print(df3)

