import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')


# 导入数据
df = pd.read_csv('./data/starbucks_store_worldwide.csv')

# 绘制排名前五的国家店铺量
# # 准备数据
# data1 = df.groupby(by='Country').count()['Brand'].sort_values(ascending=False)[:10]
#
# _x = data1.index
# _y = data1.values
#
# # 画图
# plt.figure(figsize=(20, 8), dpi=80)

# plt.bar(range(len(_x)), _y)
#
# plt.xticks(range(len(_x)), _x)
#
# plt.show()

# 绘制中国前50个城市的店铺数量
df = df[df['Country'] == 'CN']
data1 = df.groupby(by='City').count()['Brand'].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20, 8), dpi=90)

plt.bar(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x, fontproperties=my_font)

plt.show()
