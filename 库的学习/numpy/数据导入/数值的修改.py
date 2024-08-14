import numpy as np

t1 = np.arange(24)
t1 = t1.reshape((4, 6))
print(t1)

# 判断矩阵内部结构大小
print(t1 < 10)
# 取t1中小于10并让其等于3
t1[t1 < 10] = 3
print(t1)
t1[t1 > 20] = 4
print(t1)

# numpy的三元运算符 小于10替换成0, 大于10替换成10
t2 = np.where(t1 < 10, 0, 10)
print(t2)

# 裁剪矩阵留下想要的部分
# 把矩阵小于10的替换为10，大于18的替换成18
t3 = t1.clip(10, 18)
print(t3)

# 对矩阵元素赋值
t1 = t1.astype(float)
t1[3, 3] = np.nan
print(t1)

