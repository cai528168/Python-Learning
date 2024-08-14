import pandas时间序列方法 as pd
import numpy as np

# 读取excel数据
df = pd.read_csv('./data/USvideos.csv')

# 对行列进行排序 ascending=False 取倒序
# df = df.sort_index(axis=1, ascending=False)
# print(df)
# 对元素进行排序
# df = df.sort_values(by='date')
# print(df)

# 取出index查看
index = df.index

# 取出columns查看
columns = df.columns

# 取出values进行查看
values = df.values

# 取出shape进行查看
shape = df.shape

# 取出df的纬度
ndim = df.ndim

# DataFrame查询
# 显示前几行
head = df.head(5)

# 显示后几行
tail = df.tail(5)

# 展示df的概述
info = df.info

# 对DataFrame进行描述
description = df.describe()

# 取出具体的行或列
# -- 方括号写数组,表示行,对行进行操作
# -- 写字符串表示的去列索引,对列进行操作
# -- 同时取行与列,loc[],iloc[]
level = df[:20]
views = df['views']
# print(level)
# print(views)

# 通过标签提取
t = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
t_loc = t.loc['a', 'Z']
# 取整行
t_index = t.loc['a']
# 取整列 分开的多行多列使用列表隔开[]
t_columns = t.loc[:, 'Y']
print(t_loc)

# 通过位置提取
t_loc = t.iloc[1, 2]
print(t_loc)
# 行列取法同上

# 对透视表进行赋值
t.iloc[1, 2] = np.nan
# print(t)


