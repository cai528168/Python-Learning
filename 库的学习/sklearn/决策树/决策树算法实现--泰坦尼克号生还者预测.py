import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report
import graphviz
data = pd.read_csv('titanic_data.csv')

# 数据预处理
# 删除PassengerId列
data.drop('PassengerId', axis=1, inplace=True)

# 将离散化数据性别处理为连续性数据即0、1代替性别表示
data.loc[data['Sex'] == 'male', 'Sex'] = 1
data.loc[data['Sex'] == 'female', 'Sex'] = 0

# 将缺失的年龄进行填充（inplace直接在本上数据上进行修改而不重新生成新的数据）
data.fillna(data['Age'].mean(), inplace=True)

# 模型的构建与预测

# 构建决策树模型
Dtc = DecisionTreeClassifier(max_depth=5, random_state=8)
# 模型训练
Dtc.fit(data.iloc[:, 1:], data['Survived'])
# 模型预测
pre = Dtc.predict(data.iloc[:, 1:])
# 判断模型精度
# print(pre == data['Survived'])
print(classification_report(data['Survived'], pre))

# 决策树可视化
dot_data = export_graphviz(Dtc, feature_names=['Pclass', 'Sex', 'Age'], class_names='Survived')
graph = graphviz.Source(dot_data)
graph.view()

