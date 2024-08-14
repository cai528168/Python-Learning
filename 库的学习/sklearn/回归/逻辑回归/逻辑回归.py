import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  # 进行数据集拆分
from sklearn.metrics import classification_report

data = pd.read_csv('LogisticRegression.csv')
data_tr, data_te, label_tr, label_te = train_test_split(data.iloc[:, 1:], data['admit'], test_size=0.2)
clf = LogisticRegression()
# 模型的训练
clf.fit(data_tr, label_tr)
# 模型的输出
pre = clf.predict(data_te)
report = classification_report(label_te, pre)
print(clf.coef_)
print(report)
# 效果不理想需要对数据进行预处理或更换模型 进行优化
