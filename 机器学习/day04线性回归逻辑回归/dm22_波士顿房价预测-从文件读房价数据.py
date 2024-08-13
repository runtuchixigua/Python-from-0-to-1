# import warnings
# warnings.warn('ignore', category=FutureWarning)

from sklearn.datasets import load_boston                # 数据
from sklearn.preprocessing import StandardScaler        # 特征处理
from sklearn.model_selection import train_test_split    # 数据集划分
from sklearn.linear_model import LinearRegression       # 正规方程的回归模型
from sklearn.linear_model import SGDRegressor           # 梯度下降的回归模型
from sklearn.metrics import mean_squared_error          # 均方误差评估
from sklearn.linear_model import Ridge, RidgeCV         # 岭回归
import pandas as pd


# 正规方程
# 1 获取数据 load_boston()
# 2 数据集划分 train_test_split
# 3 特征工程-标准化 StandardScaler
# 4 机器学习-线性回归(正规方程) LinearRegression
# 5 模型评估 mean_squared_error(y_test, y_predict)
def linear_model1_读csv文件():
    # 1 获取数据 load_boston()
    mydata = load_boston()
    mydata_pd = pd.read_csv(filepath_or_buffer='./波士顿房价xy.csv')
    # print('mydata_pd-->', mydata_pd)
    myx = mydata_pd.values[:, 0:-1]
    myy = mydata_pd.values[:, -1]

    # 2 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(myx, myy, random_state=22, test_size=0.2)
    print('x_train.shape-->', x_train.shape, x_test.shape, y_train.shape, y_test.shape)

    # 3 特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4 机器学习-线性回归(正规方程)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    # 5 模型评估 mean_squared_error(y_test, y_predict)
    y_pred = estimator.predict(x_test)
    myerrval = mean_squared_error(y_test, y_pred)
    print('myerrval-->', myerrval)


# 正规方程
# 1 获取数据 load_boston()
# 2 数据集划分 train_test_split
# 3 特征工程-标准化 StandardScaler
# 4 机器学习-线性回归(正规方程) LinearRegression
# 5 模型评估 mean_squared_error(y_test, y_predict)
def linear_model1():
    # 1 获取数据
    mydata = load_boston()
    print('mydata-->', mydata)

    # 2 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(mydata.data, mydata.target, random_state=22)

    # 3 特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4 机器学习-线性回归(正规方程)
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)

    # 5 模型评估 # 获取模型系数
    y_predict = estimator.predict(x_test)
    print("预测值为:\n", y_predict)
    print("模型的权重系数为:\n", estimator.coef_)
    print("模型的偏置为:\n", estimator.intercept_)

    # 5.2 评价 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)


# 梯度下降方式
# 1 获取数据 load_boston()
# 2 数据集划分 train_test_split
# 3 特征工程-标准化 StandardScaler
# 4 机器学习-线性回归(梯度下降) SGDRegressor
# 5 模型评估 mean_squared_error(y_test, y_predict)
def linear_model2():
    # 1.获取数据
    mydata = load_boston()

    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(mydata.data, mydata.target, random_state=22)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4.机器学习-线性回归(正规方程)
    estimator = SGDRegressor()
    # estimator = SGDRegressor(max_iter=1000, learning_rate="constant", eta0=0.001)
    # estimator = SGDRegressor(max_iter=1000, learning_rate="constant", eta0=1)
    estimator.fit(x_train, y_train)

    # 5.模型评估 # 5.1 获取模型参数
    y_predict = estimator.predict(x_test)
    # print("预测值为:\n", y_predict)
    print("模型的权重系数为:\n", estimator.coef_)
    print("模型的偏置为:\n", estimator.intercept_)

    # 5.2 评价 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)
    return None


# 岭回归方式
# 1 获取数据 load_boston()
# 2 数据集划分 train_test_split
# 3 特征工程-标准化 StandardScaler
# 4 机器学习-线性回归(岭回归) Ridge(alpha=1)
# 5 模型评估 mean_squared_error(y_test, y_predict)
def linear_model3():
    # 1.获取数据
    mydata = load_boston()

    # 2.数据集划分
    x_train, x_test, y_train, y_test = train_test_split(mydata.data, mydata.target, random_state=22)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4.机器学习-线性回归(正规方程)
    # estimator = Ridge(alpha=1)
    estimator = RidgeCV(alphas=(0.1, 1.0, 10.0))
    estimator.fit(x_train, y_train)

    # 5.模型评估 # 5.1 获取系数等值
    y_predict = estimator.predict(x_test)
    # print("预测值为:\n", y_predict)
    print("模型的权重系数为:\n", estimator.coef_)
    print("模型的偏置为:\n", estimator.intercept_)

    # 5.2 评价 均方误差
    error = mean_squared_error(y_test, y_predict)
    print("误差为:\n", error)


if __name__ == '__main__':
    # linear_model1_读csv文件()
    # linear_model1()
    # linear_model2()
    linear_model3()
    print('不同的线性回归方程 End')