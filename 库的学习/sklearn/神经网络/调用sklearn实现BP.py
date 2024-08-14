import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor  # 连续的回归，离散的分类

data_tr = pd.read_csv('BPdata_tr.txt')  # 训练集样本
data_te = pd.read_csv('BPdata_te.txt')  # 测试集样本

# 构建模型
model = MLPRegressor(hidden_layer_sizes=(10,), random_state=10, max_iter=800, learning_rate_init=0.1)

# 模型训练
model.fit(data_tr.iloc[:, :2], data_tr.iloc[:, 2])

# 模型预测
pre = model.predict(data_te.iloc[:, :2])

# 模型预测误差
error = np.abs(pre-data_te.iloc[:, 2]).mean()
print(error)
