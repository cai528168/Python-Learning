import matplotlib.pyplot as plt
import numpy as np

us_file_path = 'numpy数据处理阶段/US_video_data_numbers.csv'
uk_file_path = 'numpy数据处理阶段/GB_video_data_numbers.csv'

# 确定文件路径并对数据进行转换
t_us = np.loadtxt(us_file_path, delimiter=',', dtype='int')
t_uk = np.loadtxt(uk_file_path, delimiter=',', dtype='int')

# 取评论数据
t_us_comments = t_us[:, -1]

# 选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

print(t_us_comments.max(), t_us_comments.min())

d = 50

bin_nums = (t_us_comments.max() - t_us_comments.min())//d

# 绘图
plt.figure(figsize=(20, 8), dpi=80)

plt.hist(t_us_comments, bin_nums)

plt.show()
