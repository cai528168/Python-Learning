import numpy as np

print(np.nan == np.nan)

t2 = np.array([[3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3], [12, 13, 14, 15, 16, 17], [18, 19, 20, np.nan, 20, 20]])

t2[:, 0] = 0

# 统计不为0的位置数
num = np.count_nonzero(t2)
print(num)

# 统计NAN数---*****NAN以后得计算会一直显示NAN
num_not = np.count_nonzero(t2 != t2)
print(num_not)
nan_judge = np.isnan(t2)
print(np.count_nonzero(np.isnan(t2)))

# 将NAN的值以均值进行替换
t1 = np.arange(12).reshape((3, 4)).astype('float')
# 将第第一行第三列以后得数据替换为NAN
t1[1, 2:] = np.nan


def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 当前这一列
        nan_num = np.count_nonzero(temp_col != temp_col)
        if nan_num != 0:  # 不为0说明当前一列中有nan
            temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列不为nan的array

            # 选中当前nan的位置并将值赋给不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype('float')
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)
