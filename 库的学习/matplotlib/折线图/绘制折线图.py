from matplotlib import pyplot as plt
from random import randint
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')

# 设置数据
y = [randint(20, 35)for i in range(120)]
x = range(0, 120)

plt.figure(figsize=(20, 8), dpi=80)

# 绘制图像
# 设置线条样式 label-名称 color-颜色 linestyle-线条格式 linewidth-线条长度 alpha-透明度
plt.plot(x, y, label='小明', color='yellow', linestyle='--', linewidth=5, alpha=0.5)

# 调整x轴的刻度
# 转换为列表方便显示步长为10
_xtick_labels = ['10点{}分'.format(i)for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]

# 取步长数字和字符串进行一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)  # rotation旋转90度

# 添加描述信息
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度 单位(C)', fontproperties=my_font)
plt.title('10点到12点气温情况', fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.4)

# 保存图像
plt.savefig('./T.png')

# 展示图像
plt.show()

