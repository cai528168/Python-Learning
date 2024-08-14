# 高斯朴素贝叶斯 如果有先验概率就写入【数组】 若无会自动计算

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

iris = load_iris()

data_tr, data_te, label_tr, label_te = train_test_split(iris.data, iris.target, test_size=0.2)

clf = GaussianNB()

# 模型的训练
clf.fit(data_tr, label_tr)

# 模型的预测
pre = clf.predict(data_te)
# 模型在测试集样本上的预测精度
print(sum(pre == label_te)/len(pre))

print(iris)