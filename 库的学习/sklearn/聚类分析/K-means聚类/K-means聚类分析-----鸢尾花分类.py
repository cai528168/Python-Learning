from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
data = iris.data
n = len(data)
k = 3

# 1、选中心
center = data[:k, :]
center_new = np.zeros([k, data.shape[1]])
dist = np.zeros([n, k+1])

while True:
    # 2、求距离
    for i in range(n):
        for j in range(k):
            dist[i, j] = np.sqrt(sum((data[i, :] - center[j, :]) ** 2))
        # 3、归类（dist[i,j]是指两个点之间的距离）
        dist[i, k] = np.argmin(dist[i, :k])

    # 4、求新类中心
    for i in range(k):
        index = dist[:, k] == i
        center_new[i, :] = data[index, :].mean(axis=0)

    # 5、判定结束
    if np.all(center == center_new):
        break
    else:
        center = center_new
print(dist)


