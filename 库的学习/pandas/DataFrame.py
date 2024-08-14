import pandas as pd
import numpy as np

# 加载一个DataFrame
data = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(data)

# 修改DataFrame中的索引
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list('abc'), columns=list('WXYZ'))
print(data)

# DataFrame 传入字典 少的一部分会使用NAN代替
d1 = {'name': ['Curry', 'James'], 'age': [12, 13], 'level': ['super star', 'super star']}
data_Basketball_player = pd.DataFrame(d1)
print(data_Basketball_player)


