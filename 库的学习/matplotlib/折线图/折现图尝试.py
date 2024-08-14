from matplotlib import pyplot as plt

# 创建figure类,实例化图像
fig = plt.figure(figsize=(20, 8), dpi=80)  # dpi让图片变清晰

# 设置x轴变量
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 传入x轴、y轴数据绘图
plt.plot(x, y)

# 设置x轴的刻度
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::2])
plt.yticks(range(min(y), max(y)+1))

# 保存图片
plt.savefig('./sig_size.png')  # 可以保存为svg矢量格式放大不会失帧

# 展示图形
plt.show()





