import pandas as pd

# 导入数据
df = pd.read_csv('./data/starbucks_store_worldwide.csv')
print(df.info())

# 使用国家进行分类
grouped = df.groupby(by='Country')
# 可以进行遍历
# for i, j in grouped:
#     print(i)
#     print(j)
#     print('*'*100)

# 调用聚合的方法 可以特指一个指标
# country_count = grouped['Brand'].count()
# print(country_count['US'])
# print(country_count['CN'])

# 统计中国每个省份的国家店铺数量
# china_data = df[df['Country'] =='CN']
# grouped = china_data.groupby(by='State/Province').count()['Brand']
# print(grouped)

# 对多个条件进行分组聚合 返回的是Series类型
grouped = df['Brand'].groupby(by=[df['Country'], df['State/Province']]).count()
# print(grouped)

# 数据按照多个条件分组返回DataFrame
grouped = df[['Brand']].groupby(by=[df['Country'], df['State/Province']]).count()

