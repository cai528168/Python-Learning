import numpy as np
import matplotlib.pyplot as plt

us_file_path = 'numpy数据处理阶段/US_video_data_numbers.csv'
uk_file_path = 'numpy数据处理阶段/GB_video_data_numbers.csv'

# 确定文件路径并对数据进行转换
t_us = np.loadtxt(us_file_path, delimiter=',', dtype='int')
t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype='int')

# 选择喜欢数比50万小的数据
t_uk = t_uk[t_uk[:, 1] <= 500000]

t_uk_comment = t_uk[:, -1]
t_uk_like = t_uk[:, 1]

plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(t_uk_like, t_uk_comment)

plt.show()
