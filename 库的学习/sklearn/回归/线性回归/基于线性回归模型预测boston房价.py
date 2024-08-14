from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston  # 获取boston房价数据集
import matplotlib.pyplot as plt

# 实例化
boston = load_boston()
x = boston.data[:, 5:6]
clf = LinearRegression()
# 如果只取一个6无法成为二维结构 训练模型
clf.fit(x, boston.target)
# clf.coef_  # 回归系数
# 模型输出
y_pre = clf.predict(x)

# 样本实际分布
plt.scatter(x, boston.target)
# 绘制拟合曲线
plt.plot(x, y_pre, color='red')
plt.show()

