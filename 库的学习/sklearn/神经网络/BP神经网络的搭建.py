import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):  # 网络激活函数
    return 1 / (1 + np.exp(-x))


data_tr = pd.read_csv('BPdata_tr.txt')  # 训练集样本
data_te = pd.read_csv('BPdata_te.txt')  # 测试集样本

n = len(data_tr)
yita = 1.5  # 学习速率
# 网络结构的搭建
out_in = np.array([0.0, 0, 0, 0, -1])  # 输出层的输入

w_mid = np.zeros([3, 4])  # 隐层神经元的权值&阈值
w_out = np.zeros([5])  # 输出层神经元的权值&阈值

delta_w_out = np.zeros([5])  # 输出层权值&阈值的修正量
delta_w_mid = np.zeros([3, 4])  # 中间层权值&和阈值的修正量
Err = []

# 训练的次数
for j in range(100):
    error = []
    # 读取多个样本进行训练
    for it in range(n):
        net_in = np.array([data_tr.iloc[it, 0], data_tr.iloc[it, 1], -1])  # 网络输入
        real = data_tr.iloc[it, 2]
        for i in range(4):
            out_in[i] = sigmoid(sum(net_in * w_mid[:, i]))  # 从输入到隐层的传输过程

        res = sigmoid(sum(out_in * w_out))  # 模型的预测值
        error.append(abs(real - res))  # 得到误差项

        # print(it, '个样本的模型输出：', res, 'real:', real)

        delta_w_out = yita * res * (1 - res) * (real - res) * out_in  # 输出层权值的修正量
        delta_w_out[4] = -yita * res * (1 - res) * (real - res)  # 输出值阈值的修正量

        w_out = w_out + delta_w_out  # 实现更新

        # 隐含层的修正
        for i in range(4):
            # 中间层神经元的权值修正量
            delta_w_mid[:, i] = yita * out_in[i] * (1 - out_in[i]) * w_out[i] * res * (1 - res) * (real - res) * net_in
            # 中间值阈值的修正量
            delta_w_mid[2:, i] = -yita * out_in[i] * (1 - out_in[i]) * w_out[i] * res * (1 - res) * (real - res)
        w_mid = w_mid + delta_w_mid  # 实现更新
    Err.append(np.mean(error))

plt.plot(Err)
plt.show()
plt.close()


# 将测试集样本放入训练好的网络中去
error_te = []
for it in range(len(data_te)):
    net_in = np.array([data_te.iloc[it, 0], data_te.iloc[it, 1], -1])  # 网络输入
    real = data_te.iloc[it, 2]
    for i in range(4):
        out_in[i] = sigmoid(sum(net_in * w_mid[:, i]))  # 从输入到隐层的传输过程
    res = sigmoid(sum(out_in * w_out))   # 模型预测值
    error_te.append(abs(real-res))
plt.plot(error_te)
plt.show()
# 计算模型的误差平均值（测试样本上的切不是训练集）
np.mean(error_te)

