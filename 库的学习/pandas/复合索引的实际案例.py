import pandas as pd

a = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': list('hjklmno')})

b = a.set_index(['c', 'd'])
print(b)

# 需要先取出列后再分开取
c = b['a']
# 只取one
d = c['one']
print(d)
# 取ones同时取j
d = c['one']['j']
print(d)

# 若从内层开始取需要再变回来再取
# b = a.set_index(['d', 'c'])
# c = b['a']
# 交换复合索引
# c = c.swaplevel()
# d = c['one']
# print(d)
