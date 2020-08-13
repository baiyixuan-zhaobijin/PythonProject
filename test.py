
import pandas as pd
import arrow
fileName = 'J:\\我的坚果云\\时计-20-08-12.xlsx'
df = pd.read_excel(fileName,'时计')
df['日期'] = pd.to_datetime(df['日期'],format="%Y-%m-%d")
print(df[(df.状态=='✔')&(df.日期=='2020-08-13')])
date = arrow.utcnow().format('YYYY-MM-DD')
print(date)
