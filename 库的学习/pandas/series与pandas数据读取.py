import pandas as pd
from pymongo import MongoClient

# 创建一个带索引的数组 可以确定index范围
t1 = pd.Series([1, 2, 31, 12, 3, 4]).astype(float)
# print(t1)
# 修改索引类型
t2 = pd.Series([1, 23, 2, 2, 1], index=list('adcde'))
# print(t2)

# 给定一个字典 字典键就是对应的索引
temp_dict = {'name': 'James', 'age': 20, 'level':'super star'}
t3 = pd.Series(temp_dict)
# print(t3)

# 取连续或不连续数据
# print(t3[:2])
# print(t3[[1, 2]])
# print(t3[['age', 'name']])

# 查看index内容
t = t3.index
# print(t)

# 查看元素
p = t3.values
# print(p)

# 读取excel数据
df = pd.read_csv('./data/USvideos.csv')
# 读取mysql数据
# dp = pd.read_sql(sql_sentence,connection)
# 读取mongo数据



