# from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge,RidgeCV
import pandas as pd
import numpy as np

# 正规方程
#1获取数据 load_boston()
#2数据集划分 train_test_split#2
#3特征工程-标准化 standardScaler
#4机器学习-线性回归(正规方程)LinearRegression
#5模型评估 mean_squared_error(y_test,5y_predict)
def linear_model1():
    # 1获取数据 load_boston()

    # 加载波士顿房屋数据集
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    # 数据准备
    X = data
    y = target
    print(X, y)
    # 2数据集划分 train_test_split#2
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # 3特征工程-标准化 standardScaler
    # 4机器学习-线性回归(正规方程)LinearRegression
    # 5模型评估 mean_squared_error(y_test,5y_predict)
    pass

if __name__ == '__main__':
    linear_model1()
    print('End')