from matplotlib import pyplot as plt
from matplotlib import font_manager

"""
应用场景：
  1.数量统计
  2.频率统计(市场饱和度)
"""

# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')


a = ['猩球崛起3：终极之战', '郭刻尔克', '蜘蛛侠：英雄归来', '战狼2']
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14]  # 防止重叠放在旁边所以设置0.2相当于左移动0.2个单位
x_16 = [i+0.2*2 for i in x_14]

bar_width = 0.2  # 不能大于0.3 或0.4会重叠图形

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.bar(x_15, b_15, width=bar_width, label='9月14日')
plt.bar(range(len(a)), b_14, width=bar_width, label='9月15日')
plt.bar(x_16, b_16, width=bar_width, label='9月16日')

# 设置图例
plt.legend(prop=my_font)

# 设置x轴刻度
plt.xticks(x_15, a, fontproperties=my_font)

# 保存图像
plt.savefig('./多个条形图统计.png')
plt.show()
