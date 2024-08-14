from matplotlib import pyplot as plt
from matplotlib import font_manager
"""

应用场景
a.应用于不同纬度之间的内在关联关系
b.观察数据的离散聚合程度

"""


# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')

y_3 = [63.42198883, 63.99689106, 66.82325643, 73.37920569, 73.33796589, 96.82662972, 129.028057, 177.9573495, 260.3077064, 291.2051232, 316.9023038, 341.0330135, 365.8834997, 453.6447553, 484.8923411, 493.3482526, 576.5202944, 602.6941674, 575.5444664, 587.5003261, 576.9600656, 659.6891648, 618.4158304, 727.1076034, 664.3914015, 665.3914015, 666.3914015, 667.3914015, 668.3914015, 669.3914015]
y_10 = [56.45920792, 56.4893566, 60.10871213, 63.19225077, 67.75441017, 76.54552093, 93.44756555, 107.24222, 123.3483074, 137.946682, 141.6428604, 141.4464775, 38.33399152, 119.4822161, 37.84351726, 170.4491214, 175.4829295, 175.9533895, 161.5454375, 163.5292045, 155.4783825, 143.2348569, 171.4860575, 167.4385481, 164.892901, 165.892901, 166.892901, 167.892901, 168.892901, 169.892901]

x_3 = range(1, 31)
x_10 = range(50, 80)

# 设置图形大小
plt.figure(figsize=(20, 10), dpi=80)

# 绘制图像
plt.scatter(x_3, y_3, label='3月份')
plt.scatter(x_10, y_10, label='10月份')

# 添加图例
plt.legend(loc='upper left', prop=my_font)

# 调整x轴的刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ['3月{}日'.format(i)for i in x_3]
_xtick_labels += ['10月{}日'.format(i-50)for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.xlabel('时间', fontproperties=my_font, fontsize=20)
plt.ylabel('温度', fontproperties=my_font, fontsize=20)
plt.title('两个月份温度情况', fontproperties=my_font, fontsize=20)

# 保存图像
plt.savefig('./散点图')

# 展示
plt.show()


