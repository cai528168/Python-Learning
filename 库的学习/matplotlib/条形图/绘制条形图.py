from matplotlib import pyplot as plt
from matplotlib import font_manager

# 设置中文字体
my_font = font_manager.FontProperties(fname='/system/Library/Fonts/PingFang.ttc')

# 导入数据
x = ['钢铁侠', '功夫熊猫', '喜羊羊与灰太狼', '英雄联盟', '王者荣耀', '饥饿营销', '生化危机', '活死人军团', '哥斯拉', '流浪地球']
y = [54.32, 43.2, 40.2, 36.88, 34.28, 30.1, 29.87, 26.37, 21.53, 20.11]

# 设置图形大小
plt.figure(figsize=(20, 15), dpi=80)

# 绘制条形图
plt.bar(range(len(x)), y, width=0.3)

# 设置字符串到x轴
plt.xticks(range(len(x)), x, fontproperties=my_font, rotation=45)

# 设置图例
plt.xlabel('电影名称', fontproperties=my_font, fontsize=20)
plt.ylabel('票房 单位 (亿元)', fontproperties=my_font, fontsize=20)
plt.title('前十电影票房', fontproperties=my_font, fontsize=20)
plt.grid(alpha=0.4)

# 保存图像
plt.savefig('./条形图.png')

plt.show()