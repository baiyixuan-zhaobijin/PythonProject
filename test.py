
import pandas as pd
fileName = 'J:\\我的坚果云\\时计-20-08-12.xlsx'
df = pd.read_excel(fileName,'时计')
print(df[(df.状态=='✔')&(df.日期=='20-08-12')])