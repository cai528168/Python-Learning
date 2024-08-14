import pandas时间序列方法 as pd
from matplotlib import pyplot as plt
import numpy as np


IMDB_Movie_data = pd.read_csv('./data/IMDB-Movie-Data.csv')
# print(IMDB_Movie_data.info())
# print(IMDB_Movie_data.head(1))

# rating,runtime查看分布情况
# 选择图像直方图
# 准备数据
runtime_data = IMDB_Movie_data['Runtime (Minutes)'].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

d = 5

# 计算组距
num_bin = (max_runtime - min_runtime)//d

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=80)
plt.hist(runtime_data, num_bin)

# 设置x轴的刻度
# plt.xticks(range(min_runtime, max_runtime + d, d))
#
# plt.show()

# 获取平均评分
print(IMDB_Movie_data['Rating'].mean())

# 导演的人数
print(len(set(IMDB_Movie_data['Director'].tolist())))
print(len(IMDB_Movie_data['Director'].unique()))

# 获取演员的人数
temp_actors_list = IMDB_Movie_data['Actors'].str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_num = len(set(actors_list))
print(actors_num)




