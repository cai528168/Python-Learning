import numpy as np

us_file_path = 'numpy数据处理阶段/US_video_data_numbers.csv'
uk_file_path = 'numpy数据处理阶段/GB_video_data_numbers.csv'

# 确定文件路径并对数据进行转换
us_data = np.loadtxt(us_file_path, delimiter=',', dtype='int')
uk_data = np.loadtxt(uk_file_path, delimiter=',', dtype='int')

# 添加国家信息
# 构造全为0的数据
zero_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)

# 分别添加一列全为0,1的数组
us_data = np.hstack((us_data, zero_data))
uk_data = np.hstack((uk_data, ones_data))

# 拼接两组数据
final_data = np.vstack((us_data, uk_data))
print(final_data)


