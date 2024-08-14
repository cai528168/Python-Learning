from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()  # 导入鸢尾花数据
data_tr, data_te, label_tr, label_te = train_test_split(iris.data, iris.target, test_size=0.2)  # 对数据集拆分专家样本集合

model = KNeighborsClassifier(n_neighbors=3)  # 构建模型
model.fit(data_tr, label_tr)
pre = model.predict(data_te)  # 模型训练
score = model.score(data_te, label_te)  # 模型在测试集上的精度
print(score)
