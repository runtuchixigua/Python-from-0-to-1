import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error # 计算均方误差
from sklearn.model_selection import train_test_split

# pip uninstall scikit-learn
# pip install scikit-learn==1.1.1 -i https://pypi.douban.com/simple

# 1 准备数据x y(增加上噪声)
# x = np.random.uniform(-3, 3, size=100)
# 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)
# 2 实例化线性回归模型LinearRegression
# 3 训练模型 .fit(x.reshape(-1, 1), y)
# 4 模型预测
# 5 计算均方误差 mean_squared_error
# 6 画图  .scatter(x, y)/ .plot(x, y_predict, color='r')

# 数据是抛物线非线性的, 用线性模型去拟合. 所以模型会欠拟合
def dm01_模型欠拟合():
    # 1 准备数据x y(增加上噪声)
    np.random.seed(666)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2 实例化线性回归模型
    estimator = LinearRegression()

    # 3 训练模型
    X = x.reshape(-1, 1)
    estimator.fit(X, y)

    # 4 模型预测
    y_predict = estimator.predict(X)

    # 5 计算均方误差
    myret = mean_squared_error(y, y_predict)
    print('myret-->', myret)

    # 6 画图
    plt.scatter(x, y)
    plt.plot(x, y_predict, color='r')
    plt.show()


# 增加一列数据 格式见x1\x2前后变化
def dm02_hstack():
    x1 = np.array(
        [[80, 86],
         [82, 80],
         [85, 78],
         [90, 90]])

    newcol = np.array([[1],
                       [2],
                       [3],
                       [4]])
    x2 = np.hstack((newcol, x1))
    print('x1-->\n', x1)
    print('x2-->\n', x2)

    ''' 
    x1-->
    [[80 86]
    [82 80]
    [85 78]
    [90 90]]
    x2-->
    [[ 1 80 86]
    [ 2 82 80]
    [ 3 85 78]
    [ 4 90 90]]
    '''
    pass


# 线性回归这里的线性是指权重参数w1 w2 wn是一个常数 1次幂
# 但是线性回归可以模拟出来曲线原因是: 我们给模型送入的数据,x, x^2, x^3 我们画函数曲线的时候
# 画的是  y = w1x + w2 * x^2  + w3 * x^3 + b
# 所以 线性回归方程可以模拟出来曲线! 是很强大

# 1 给模型喂的数据增加二次项 X2 = np.hstack([X, X ** 2])
# 2 画图时 需要对x进行排序, 取x排序后对应的y值
# plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
def dm02_模型ok():
    # 1 准备数据x y(增加上噪声)
    np.random.seed(666)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2 实例化线性回归模型
    estimator = LinearRegression()

    # 3 训练模型
    X = x.reshape(-1, 1)
    # print('X.shape-->', X.shape)
    X2 = np.hstack([X, X ** 2]) # 数据增加二次项
    # print('X2.shape-->', X2.shape)
    # print('X2.shape-->', X2)
    estimator.fit(X2, y)

    # 4 模型预测
    y_predict = estimator.predict(X2)

    # 5 计算均方误差
    myret = mean_squared_error(y, y_predict)
    print('myret-->', myret)

    # print('np.sort(x)-->', np.sort(x)) # 对x数据排序
    # print('np.argsort(x)-->', np.argsort(x))  # 对x排序然后返回排序后的索引
    # print('y_predict[np.argsort(x)]-->', y_predict[np.argsort(x)])  # 找到对应的y

    # 6 画图
    plt.scatter(x, y)
    # plt.plot(x, y_predict, color='r')
    # 画图时 需要对x进行排序, 取x排序后对应的y值
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()


# 再次加入高次项，绘制图像，观察均方误差结果
# X3 = np.hstack([X, X**2, X**3, X**4, X**5, X**6, X**7, X**8, X**9, X**10])
def dm03_模型过拟合():
    # 1 准备数据x y(增加上噪声)
    np.random.seed(666)
    x = np.random.uniform(-3, 3, size=100)
    y = 0.5 * x ** 2 + x + 2 + np.random.normal(0, 1, size=100)

    # 2 实例化线性回归模型
    estimator = LinearRegression()

    # 3 训练模型
    X = x.reshape(-1, 1)
    # print('X.shape-->', X.shape)
    X3 = np.hstack([X, X**2, X**3, X**4, X**5, X**6, X**7, X**8, X**9, X**10])  # 数据多个高次项
    # print('X2.shape-->', X2.shape)
    # print('X2.shape-->', X2)
    estimator.fit(X3, y)

    # 4 模型预测
    y_predict = estimator.predict(X3)

    # 5 计算均方误差
    myret = mean_squared_error(y, y_predict)
    print('myret-->', myret)

    # print('np.sort(x)-->', np.sort(x)) # 对x数据排序 plt.plot()要求x从小到大的顺序输入
    # print('np.argsort(x)-->', np.argsort(x))  # 对x排序然后返回排序后的坐标
    # print('y_predict[np.argsort(x)]-->', y_predict[np.argsort(x)])  # 找到对应的y

    # 6 画图
    plt.scatter(x, y)
    # plt.plot(x, y_predict, color='r')
    # 画图时输入的x数据: 要求是从小到大
    plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
    plt.show()
    pass


if __name__ == '__main__':
    # dm01_模型欠拟合()
    # dm02_hstack()
    # dm02_模型ok()
    dm03_模型过拟合()
    print('通过代码认识过拟合欠拟合 End')



