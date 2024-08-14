import pandas时间序列方法 as pd
from matplotlib import pyplot as plt

books_data = pd.read_csv('./data/books.csv')

# print(books_data.info())

data1 = books_data[pd.notnull(books_data['original_publication_year'])]

grouped1 = data1.groupby(by='original_publication_year').count()['title']

# 不同年份平均评分
grouped2 = data1['average_rating'].groupby(by=data1['original_publication_year']).mean()

_x = grouped2.index
_y = grouped2.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y)

plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)

plt.show()