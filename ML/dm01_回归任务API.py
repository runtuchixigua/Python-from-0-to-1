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
    y_pred = estimator.predict([[90, 80]])
    print(y_pred)
    pass


import joblib
# 模型保存
# 模型加载
def dm02_线性回归api_保存和加载():
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
    y_pred = estimator.predict([[90, 80]])
    print(y_pred)
    # 模型保存
    joblib.dump(estimator, "./data/mymodel1.bin")
    # 模型加载
    estimator2 = joblib.load("./data/mymodel1.bin")
    y_pred2 = estimator2.predict([[80, 70]])
    print(y_pred2)
    pass


if __name__ == '__main__':
    # dm01_线性回归api()
    dm02_线性回归api_保存和加载()
    print("线性回归api End")
