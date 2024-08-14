import numpy as np
t1 = np.arange(12).reshape(3, 4)
t2 = np.arange(8).reshape(2, 4)
t3 = np.arange(6).reshape(3, 2)
print(t1)
print(t2)
print(t3)

# 竖直拼接
t4 = np.vstack((t1, t2))
print(t3)

# 水平拼接
t5 = np.hstack((t1, t3))
print(t4)

