import pandas as pd

# 自主创建时间序列数据
# freq指的是统计频率 D-天数 M-月份
data_time = pd.date_range(start='20171230', end='20180131', freq='D')

# periods指的是统计范围
data_months = pd.date_range(start='20171230', periods=10, freq='M')

# 将数据series转换为时间类型并给定固定的格式
# df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='')



