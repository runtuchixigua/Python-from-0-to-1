import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error # 计算均方误差
from sklearn.model_selection import train_test_split


from sklearn.linear_model import Lasso
def dm04_模型过拟合_L1正则化():
    # 1 准备数据x y(增加上噪声)
    np.random.seed(666)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2 实例化L1正则化模型 做实验:alpha惩罚力度越来越大k值越来越小,反而会欠拟合
    # normalize是否对数据正则化
    # estimator = Lasso(alpha=0.005, normalize=True)
    # estimator = Lasso(alpha=0.02, normalize=True)
    estimator = Lasso(alpha=0.1, normalize=True)

    # 3 训练模型
    X = x.reshape(-1, 1)
    X3 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])  # 数据增加二次项
    estimator.fit(X3, y)
    print('estimator.coef_', estimator.coef_)

    # 4 模型预测
    y_predict = estimator.predict(X3)

    # 5 计算均方误差
    myret = mean_squared_error(y, y_predict)
    print('myret-->', myret)

    # 6 画图
    plt.scatter(x, y)
    # 画图时输入的x数据: 要求是从小到大
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()


from sklearn.linear_model import Ridge
def dm05_模型过拟合_L2正则化():
    # 1 准备数据x y(增加上噪声)
    np.random.seed(666)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2 实例化L2正则化模型
    # 正则化力度越大也是容易产生欠拟合, 特征值会越来越小但是不会变成0
    # estimator = Ridge(alpha=0.005, normalize=True)
    # estimator = Ridge(alpha=0.02, normalize=True)
    estimator = Ridge(alpha=10, normalize=True)

    # 3 训练模型
    X = x.reshape(-1, 1)
    X3 = np.hstack([X, X ** 2, X ** 3, X ** 4, X ** 5, X ** 6, X ** 7, X ** 8, X ** 9, X ** 10])  # 数据增加二次项
    estimator.fit(X3, y)
    print('estimator.coef_', estimator.coef_)

    # 4 模型预测
    y_predict = estimator.predict(X3)

    # 5 计算均方误差
    myret = mean_squared_error(y, y_predict)
    print('myret-->', myret)

    # 6 画图
    plt.scatter(x, y)
    # 画图时输入的x数据: 要求是从小到大
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()


if __name__ == '__main__':
    # dm04_模型过拟合_L1正则化()
    dm05_模型过拟合_L2正则化()

    print('通过代码认识过拟合欠拟合 End')



