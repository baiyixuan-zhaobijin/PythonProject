import pandas as pd
import matplotlib.pyplot  as plt
import datetime
intervals = (
    ('周', 604800),  # 60 * 60 * 24 * 7
    ('天', 86400),    # 60 * 60 * 24
    ('小时', 3600),    # 60 * 60
    ('分', 60),
    ('秒', 1),
    )

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])

# 显示高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

fileName = 'J:\\我的坚果云\\时计-20-08-12.xlsx'
df = pd.read_excel(fileName,'时计')
df1 = df[(df.状态 == '✔')&(df.日期>='20-08-12')]
df2 = df1.loc[:,['类型','用时']]
df2['用时'] =  [int(x.replace('min','').strip()) for x in df2['用时']]
df3 = df2.groupby(['类型']).sum().reset_index()
plt.rcParams['font.sans-serif']=['SimHei']
plt.title(label='总计用时：'+ display_time(sum(df3['用时'])*60))
x_data = df3['类型']
y_data = df3['用时']
autolabel(plt.bar(range(len(y_data)), y_data, color='rgb', tick_label=x_data))
plt.legend()
plt.show()