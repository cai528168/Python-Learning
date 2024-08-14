import random

import numpy as np

# 创建一个数组得到ndarray的类型
t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

# 其他创建数组的方式
t2 = np.array(range(10))
print(t2)

# numpy特有的方法（和上面array方法一致）
t3 = np.arange(4, 10, 2)
print(t3)

# 得到该数据的类型（若不指定按电脑位数来即int64）
print(t3.dtype)

# 设置数组的类型
t4 = np.array(range(1, 4), dtype='int8')
print(t4)
print(t4.dtype)

# numpy中的bool类型
t5 = np.array([1, 1, 1, 0, 1], dtype=bool)
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype('int64')
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# 取后两位为小数
t8 = np.round(t7, 2)
print(t8)

# 创建一个全为0的数组
t9 = np.ones((3, 4))

# 创建一个全为1的数组
t10 = np.zeros((3, 4))

# 创建一个对角线为1的正方形数组
t11 = np.eye(3)

# 找到一个数组的最大最小值及其位置
t12 = np.arange(12).reshape((3, 4))
print(t12.max())
print(t12.min())

# 每一列最大值的位置
t13 = np.eye(3)
print(np.argmax(t13, axis=0))

t13[t13 == 1] = -1
print(np.argmin(t13, axis=1))


