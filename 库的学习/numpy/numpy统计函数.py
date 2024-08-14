import numpy as np

# 使用sum统计总数
t3 = np.arange(12).reshape((3, 4))
print(np.sum(t3))

# 统计行列的总和
print(np.sum(t3, axis=0))
print(np.sum(t3, axis=1))

# 统计均值
print(np.mean(t3, axis=0))
print(np.median(t3, axis=0))

# 找到一个数组的最大最小值及其位置
print(t3.max())
print(t3.min())

# 每一列最大小值的位置
t13 = np.eye(3)
print(np.argmax(t13, axis=0))

t13[t13 == 1] = -1
print(np.argmin(t13, axis=1))

# 求极值
print(np.ptp(t3, axis=1))

# 求标准差
print(np.std(t3, axis=None))
