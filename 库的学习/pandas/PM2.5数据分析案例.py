import matplotlib.pyplot as plt
import pandas as pd
file_path = './PM2.5data/BeijingPM20100101_20151231.csv'

date = pd.read_csv(file_path)

print(date.info())

# 将字符段转换为时间戳类型
period = pd.PeriodIndex(year=date['year'], month=date['month'], day=date['day'], hour=date['hour'], freq='h')
date['datetime'] = period

# 把datetime设置为索引
date.set_index('datetime', inplace=True)

# 进行降采样
df = date.resample('7D').mean()

# 处理缺失数据，删除缺失数据
data = df['PM_US Post'].dropna()

# 画图
_x = data.index
_y = data.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y)

plt.xticks(range(0, len(_x), 20), list(_x)[::20])

plt.show()