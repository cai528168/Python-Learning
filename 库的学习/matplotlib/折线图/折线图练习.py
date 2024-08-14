import matplotlib.pyplot as plt
from matplotlib import pyplot as np
from matplotlib import font_manager
# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')

x = range(10, 30)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 11]
y2 = [1, 3, 21, 2, 3, 5, 1, 12, 2, 5, 5, 2, 2, 1, 1, 2, 4, 12, 3,1]

# 设置图像
plt.Figure(figsize=(80, 2), dpi=80)

# 设置x轴上的数据
_xtick_labels = ['{}岁'.format(i)for i in x]
plt.xticks(list(x)[::2], _xtick_labels[::2], rotation=45, fontproperties=my_font,)


# 绘制图像
plt.plot(x, y1, label='小明', color='yellow', linestyle='--', linewidth=1, alpha=0.5)
plt.plot(x, y2, label='小程', color='green', linestyle='--', linewidth=1, alpha=0.5)

# 添加线的图例(只能在这里加上x、y的label)
plt.legend(prop=my_font, loc='upper left')

# 设置图例
plt.title('年龄段交npy数量', fontproperties=my_font)
plt.xlabel('年龄', fontproperties=my_font)
plt.ylabel('数量 单位：人数', fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.4)

# 保存图像
plt.savefig('./练习图')

# 显示图像
plt.show()
