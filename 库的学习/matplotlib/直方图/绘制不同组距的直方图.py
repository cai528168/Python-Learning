# 无法使用hist方法, 条形图的方法进行绘制
from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [236, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]

print(len(interval), len(width), len(quantity))

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(quantity)), quantity, width=1)  # 防止距离不一致导致图像丑

# 设置x轴的刻度
_x = [i-0.5 for i in range(13)]
_xtick_label = interval + [150]
plt.xticks(_x, _xtick_label)

plt.grid(alpha=0.4)

plt.show()
