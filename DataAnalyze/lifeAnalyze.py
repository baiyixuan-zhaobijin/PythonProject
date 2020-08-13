import pandas as pd
import matplotlib.pyplot as plt
import common
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
plt.rcParams['font.sans-serif']=['SimHei']
title = '总计用时：'+ common.display_time(sum(df3['用时'])*60)
plt.title(label=title)
x_data = df3['类型']
y_data = df3['用时']
type = input()
if(type == '2'):
    plt.rcParams['axes.unicode_minus'] = False
    plt.barh(range(x_data.count()), y_data, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
    plt.yticks(range(x_data.count()), x_data)
    plt.xlabel("用时")
    for x, y in enumerate(y_data):
        plt.text(y + 0.2, x - 0.1, '%s' % y)
elif(type == '1'):
    plt.pie(y_data,labels=x_data,autopct='%1.1f%%',shadow=False,startangle=150)
    plt.legend(loc="upper right",fontsize=10,bbox_to_anchor=(1.3,1.15),borderaxespad=0.3)
elif(type == '3'):
   common.autolabel(plt.bar(range(len(y_data)), y_data, color='rgb', tick_label=x_data))
plt.show() 