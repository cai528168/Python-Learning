import numpy as np

us_file_path = 'numpy数据处理阶段/US_video_data_numbers.csv'
uk_file_path = 'numpy数据处理阶段/GB_video_data_numbers.csv'

# 确定文件路径并对数据进行转换
t1 = np.loadtxt(us_file_path, delimiter=',', dtype='int')
t2 = np.loadtxt(uk_file_path, delimiter=',', dtype='int')
print(t1)
#
# 取行
print(t1[2])

# 取连续多行
print(t1[2:])

# 取不连续的多行
print(t1[[2, 8, 10]])

# 取列
# print(t1[1, :])
# print(t1[2:, :])
# print(t1[[2, 1, 3], :])
print(t1[:, 0])

# 取连续的多列
print(t1[:, 2:])

# 取不连续的多列
print(t1[:, [0, 2]])

# 取多行多列
# 取第三行，第四列的值
print(t1[2, 3])

# 取三到五行，第二列到第四列的结果
# 去的是行和列交叉点的位置
b = t1[2:5, 1:4]
print(b)

# 取多个不相邻的点 必须一一对应
c = t1[[0, 2, 3], [0, 1, 2]]
print(c)
