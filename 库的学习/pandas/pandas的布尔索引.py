import pandas时间序列方法 as pd
import numpy as np

# 读取excel数据
df = pd.read_csv('./data/USvideos.csv')
# print(df)
# 对数据进行条件选择
# 对基本数值选择
df_choice_fig = df[(800 < df['dislikes']) | (df['dislikes'] < 1000)]
# print(df_choice_fig)
# 对字符串长度选择
df_choice_str = df[(9 < df['video_id'].str.len()) & (df['dislikes'] < 1000)]
# print(df_choice_str)

# 对字符串中进行分割
tags_split = df['tags'].str.split('|').tolist()
# print(tags_split)

# pandas对缺失数据的处理
t = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list('abc'), columns=list('WXYZ') )
t.loc['b':'c', ['W', 'X']] = np.nan

# 判断nan是否存在 is/not
t_isnan = pd.isnull(t)

# 处理W中的nan删掉
t_notnull = t[pd.notnull(t['W'])]
# # 删除全部为nan的行
# t = t.dropna(axis=0, how='all')
# # 删除只要一个为nan的行
# t = t.dropna(axis=0, how='any')

# 填充nan 针对每一行进行填充
t['W'] = t['W'].fillna(t['W'].mean())

t['W'][1] = np.nan

# 处理为0的数据 nan不参与运算
t[t == 0] = np.nan

print(t)

