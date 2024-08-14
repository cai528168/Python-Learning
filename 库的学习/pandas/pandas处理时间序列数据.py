import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('./911.csv')

# 预览数据
print(df.head(10))
print(df.info())

# 统计不同类型的紧急情况次数
# 获取分类情况
# print(df['title'].str.split(': '))
temp_list = df['title'].str.split(': ').tolist()
cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros(df.shape[0], len(cate_list)), columns=cate_list)

# 赋值
# for cate in cate_list:
#     zeros_df[df['title'].str.contains(cate)] = 1
#     break

for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[0]] = 1

sum_ret = zeros_df.sum(axis=0)

# 统计不同月份不同类型的紧急情况次数
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)), columns=['cate'])
print(df.groupby(by='cate').count()['title'])

# 将时间高频转换为低频 可统计平均值，可统计个数
# t.resample('M').mean(), t.resample('10D').count()

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# 统计出911数据中不同月份不同类型的电话次数的变化情况
temp_list = df['list'].str.split(':').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

# 替换以上数据
df.set_index('timeStamp', inplace=True)

# 设置添加列表示推荐
print(df.groupby(by='cate').count()['title'])

# 分组
for group_name, group_data in df.groupby(by='cate'):
    # 对不同的分类都进行绘图
    # 统计出911数据中不同月份电话次数
    count_by_month = df.resample('M').count()['title']
    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime('%Y%m%d') for i in _x]

    plt.figure(figsize=(20, 8), dpi=80)

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc='best')
plt.show()
