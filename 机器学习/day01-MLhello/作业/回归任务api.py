from sklearn.linear_model import LinearRegression

def dm01_线性回归api():
    # 1 准备数据 平时成绩 期末成绩 最终成绩
    x = [[80, 86], [82, 80], [85, 78], [90, 90], [86, 82], [82, 90], [78, 80], [92, 94]]
    y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]
    # 2 实例化 线性回归模型
    estimator = LinearRegression()
    # 3 模型训练
    estimator.fit(x, y)
    # 4 打印 线性回归模型参数 coef_ intercept_
    print(estimator.coef_)
    print(estimator.intercept_)
    # 5 模型预测
    y_pred = estimator.predict([[80, 86]])
    print(y_pred)
if __name__ == '__main__':
    dm01_线性回归api()