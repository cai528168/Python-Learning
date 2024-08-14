import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

IMDB_Movie_data = pd.read_csv('./data/IMDB-Movie-Data.csv')

print(IMDB_Movie_data['Genre'])

# 统计分类的列表
temp_list = IMDB_Movie_data['Genre'].str.split(',').tolist()

Genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zeros_IMDB_Movie_data = pd.DataFrame(np.zeros((IMDB_Movie_data.shape[0], len(Genre_list))), columns=Genre_list)
# print(zeros_IMDB_Movie_data)

# 给每个电影出现分类的位置赋值1
for i in range(IMDB_Movie_data.shape[0]):
    # zeros_IMDB_Movie.loc[0, ['Sci-fi', 'Mucical']] = 1
    zeros_IMDB_Movie_data.loc[i, temp_list[i]] = 1

print(zeros_IMDB_Movie_data.head(3))

# 统计每个分类的电影的数量和
genre_count = zeros_IMDB_Movie_data.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values

# 画图
# plt.figure(figsize=(20, 8), dpi=80)
# plt.bar(range(len(_x)), _y, width=0.4)
# plt.xticks(range(len(_x)), _x)
# plt.show()

df1 = pd.DataFrame(np.ones((2, 4)), index=['A', 'B'], columns=list('abcd'))
df2 = pd.DataFrame(np.ones((3, 3)), index=['A', 'B', 'C'], columns=list('xyz'))

# 合并两个数据 join （按照行索引进行操作）
# 以df1为基准
df3 = df1.join(df2)
print(df3)
# 以df2为基准
df3 = df2.join(df1)
print(df3)

df4 = pd.DataFrame(np.zeros((3, 3)), columns=list('fax'))
df4.loc[1, 'a'] = 1
# 按列进行内连接 默认情况下取交集内连接 merge只会合并连接相同的列 即（按照列索引进行操作）
df3 = df1.merge(df4, on='a')
print(df3)

df4 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('fax'))
df3 = df1.merge(df4, on='a')
print(df3)
# 按列进行外连接 将没有的部分补充成nan
df3 = df1.merge(df4, on='a', how='outer')
print(df3)
# 按列进行左连接 以df1为准df1什么样就什么样
df3 = df1.merge(df4, on='a', how='left')
print(df3)
# 按列进行右连接 以df4为准df4什么样就什么样
df3 = df1.merge(df4, on=['a'], how='right')
print(df3)




