from sklearn.metrics import precision_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris  # 导入鸢尾花数据集
from sklearn.svm import SVC  # 导入支持向量机算法

y_true = [1, 0, 1, 1, 0]  # 样本实际值
y_pred = [1, 0, 1, 0, 0]  # 样本预测值

# 查准率
res = precision_score(y_true, y_pred, average=None)
# 输出结果为正例与反例的查准率
print(res)
# 混淆矩阵
matrix = confusion_matrix(y_true, y_pred)
# print(matrix)
# 更为详细的有关模型性能的报告
report = classification_report(y_true, y_pred)
# print(report)

iris = load_iris()
# 构建一个支持向量机模型
clf = SVC(kernel='linear', C=1)
# 进行交叉验证cv=5进行5次
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)