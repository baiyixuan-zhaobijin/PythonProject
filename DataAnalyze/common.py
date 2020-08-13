import matplotlib.pyplot  as plt
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