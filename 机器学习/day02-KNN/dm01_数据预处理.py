'''
def dm02_MinMaxScaler():
data1 = np.array ([[1.70, 67, 1.5, 1],
                     [1.71, 80, 0.8, 2],
                     [1.75, 70, 1.5, 1],
                     [1.76, 68, 1.2, 1],
                     [1.80, 80, 1.8, 1],
                     [1.81, 90, 0.6, 2]])
    # 1 注意: 只对特征值进行归一化
    data2 = data1[:,0:-1]
    print('\n转换前的数据data-->\n', data2)

    # 2 实例化MinMaxScaler对象
    transfer = MinMaxScaler(feature_range=(0, 1))

    # 3 注意 单独fit()求每一列特征的最大值 最小值
    transfer.fit(data2)
    data = transfer.transform(data2)
    print('\n转换后的数据data-->\n', data)

    # data3 采用data2的最大值和最小值进行转换
    data3 = np.array([[1.77, 68, 1.2]])
    data = transfer.transform(data3)
    print('\n转换后的数据data-->\n', data)
'''

from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np


def dm01_数据归一化():
    data1 = np.array([[1.70, 67, 1.5, 1],
                      [1.71, 80, 0.8, 2],
                      [1.75, 70, 1.5, 1],
                      [1.76, 68, 1.2, 1],
                      [1.80, 80, 1.8, 1],
                      [1.81, 90, 0.6, 2]])
    # 1 注意: 只对特征值进行归一化
    data2 = data1[:, 0:-1]
    # 2 实例化MinMaxScaler对象
    transfer = MinMaxScaler()
    # 3 注意 单独fit()求每一列特征的最大值 最小值
    # data3 采用data2的最大值和最小值进行转换
    data3 = transfer.fit_transform(data2)
    print(data3)
    pass


def dm02_数据归一化():
    data1 = np.array([[1.70, 67, 1.5, 1],
                      [1.71, 80, 0.8, 2],
                      [1.75, 70, 1.5, 1],
                      [1.76, 68, 1.2, 1],
                      [1.80, 80, 1.8, 1],
                      [1.81, 90, 0.6, 2]])
    # 1 注意: 只对特征值进行归一化
    data2 = data1[:, 0:-1]
    # 2 实例化MinMaxScaler对象
    transfer = MinMaxScaler()
    # 3 注意 单独fit()求每一列特征的最大值 最小值
    # data3 采用data2的最大值和最小值进行转换
    data3 = transfer.fit_transform(data2)
    print(data3)
    data4 = transfer.transform(np.array([[1.77, 68, 1.2]]))
    print(data4)
    pass


'''
from sklearn.preprocessing import StandardScaler
def dm03_StandardScaler():      # 对特征值进行标准化
    data1 = np.array([
                      [1.70,   67,   1.5,   1],
                      [1.71,   80,   0.8,   2],
                      [1.75,   70,   1.5,   1],
                      [1.76,   68,   1.2,   1],
                      [1.80,   80,   1.8,   1],
                      [1.81,   90,   0.6,   2]])
    # 1 注意: 只对特征值进行标准化
    data2 = data1[:, 0:-1]
    print('\n转换前的数据data-->\n', data2)

    # 2 实例化StandardScaler对象
    transfer = StandardScaler()

    # 3 调用fit和transform函数训练模型 转换数据
    data3 = transfer.fit_transform(data2)
    # transfer.fit(data2)      # 单独使用fit函数, transform
    # data3 = transfer.transform(data2)
    print('\n转换后的数据data-->\n', data3)

    # 4 打印每1列数据的均值和标准差
    print('transfer.mean_-->', transfer.mean_)
    print('transfer.var_-->', transfer.var_)

'''
def dm03_数据标准化():
    data1 = np.array([[1.70, 67, 1.5, 1],
                      [1.71, 80, 0.8, 2],
                      [1.75, 70, 1.5, 1],
                      [1.76, 68, 1.2, 1],
                      [1.80, 80, 1.8, 1],
                      [1.81, 90, 0.6, 2]])
    data2 = data1[:, 0:-1]
    # 2 实例化StandardScaler对象
    transfer = StandardScaler()
    # 3 调用fit和transform函数训练模型 转换数据
    transfer.fit(data2)
    # 4 打印每1列数据的均值和标准差
    print(transfer.mean_)
    print(transfer.var_)

    pass


if __name__ == '__main__':
    # dm01_数据归一化()
    # dm02_数据归一化()
    dm03_数据标准化()
    print('dm01_数据预处理 End')

