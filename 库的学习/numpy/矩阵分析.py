import numpy as np
# *** reshape元组的符号可以省去

t1 = np.arange(12)

# 查看矩阵形状
print(t1.shape)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2.shape)

t3 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
print(t3.shape)

# 修改并保存矩阵
t1 = t1.reshape((3, 4))
print(t1)

# 第一个指的是分块矩阵块数 后面两个数描述矩阵形状
t4 = np.arange(24).reshape((2, 3, 4))
print(t4)
t4 = t4.reshape(4, 6)
print(t4)

# 将多维数据按行进行展开 展开成一维数据
t5 = t4.reshape((t4.shape[0]*t4.shape[1],))
t6 = t4.flatten()
print(f't5方式展开后为：{t5}')
print(f't6方式展开后为：{t6}')

# 矩阵广播机制（加减乘除上一个数时矩阵每一个元素加减乘除该数）
print(t1 + 1)
print(t1 - 1)
print(t1/2)
print(t1*2)

# 计算错误也不会影响结果输出
# print(t1/0)

t7 = np.arange(100, 124).reshape(4, 6)

# 矩阵相乘
t8 = t4*t7
print(t8)

# 矩阵相除
t9 = t4/t7
print(t9)

# （广播原则）矩阵相加减（行相同时减去行或列一行或列且个数相同时减去列） **行列不同时无法进行计算
t10 = np.arange(0, 6)
print(t4-t10)

# 实现数组的转置
t2 = np.arange(24).reshape((4, 6))
# 实现转置的三种方法
t2 = t2.transpose()
# t2 = t2.T
# t2 = t2.swapaxes(1, 0)
print(t2)

