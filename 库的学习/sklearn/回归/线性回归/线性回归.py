from sklearn.linear_model import LinearRegression

# 构建一个线性模型
clf = LinearRegression()
'''
模型
y = 0.5*x1 + 0.5*x2
'''
# 模型训练(必须是二维结构)
clf.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
# 模型调用
pre = clf.predict([[3, 3]])
print(pre)
# 模型系数
clf_num = clf.coef_
# 模型截距项
clf_y = clf.intercept_
