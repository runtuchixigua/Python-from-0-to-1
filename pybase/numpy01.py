import numpy as np

# np1 = np.arange(10, dtype=float)
# print(np1)

# 创建具有规则递增值的数组
# np2 = np.arange(2, 3, 0.1)
# print(np2)
#
# 将创建具有指定数量元素的数组，并且在指定的开始和结束值之间均匀分布
# np3 = np.linspace(0, 10, 5, retstep=True)
# print(np3)

# 定义了一个 2D 单位矩阵。i=j（行索引和列索引相等）的元素为 1，其余为 0
# np4 = np.eye(3)
# print(np4)

# 可以定义一个对角线上具有给定值的正方形 2D 数组或如果给定一个 2D 数组，则返回一个仅为对角线元素的 1D 数组。
# np5 = np.diag([1, 2, 3])
# print(np5)
#
# v = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# np6 = np.diag(v)
# print(np6)
#
# np7 = np.vander(np.linspace(0, 1, 5), 2)
# print(np7)
#
# # 输出x的递减幂
# np8 = np.vander([1, 2, 3, 4], 3)
# print(np8)

# # ndarray 创建函数，例如 numpy.ones、numpy.zeros 和 random 根据所需的形状定义数组
# np10 = np.zeros((2, 3, 2))
# print(np10)
#
# from numpy.random import default_rng
#
# np11 = default_rng(42).random((2, 3))
# print(np11)

# np12 = np.indices((2, 3))
# print(np12)
# [[[0 0 0]
#   [1 1 1]]
#
#  [[0 1 2]
#   [0 1 2]]]


# # 您创建了一个变量 b，它查看 a 的前 2 个元素。当您向 b 中添加 1 时，您将通过向 a[:2] 中添加 1 获得相同的结果。
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# b = a[:2].copy()
# b += 1
# print(b)


# data1 = [1, 2, 3, 4, 5]
# data2 = [1, 2, 3, 4, 5]
# data3 = np.array(data1 + data2)
# data5 = np.array([data1 + data2])
# data6 = np.array([data1, data2])
# data4 = data1 + data2
# print(data4)
# print(data3)
# print(data5)
# print(data6)
# data7 = data6.reshape((5, 2))
# print(data7)


# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# data_array = np.array(data)
# print("没有转置数组之前数组为：")
# print(data)
# print("转置数组之后数组为：")
# print(data_array.T)


# data = np.array([1,2,3])
# print(data.ndim)


# import numpy as np
#
# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
# result = array1 + array2
# print(result)
#
# result = array1 * array2
# print(result)


import numpy as np

data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]
data3 = [11, 12, 13, 14, 15]
data4 = [16, 17, 18, 19, 20]
data5 = [21, 22, 23, 24, 25]
data6 = [26, 27, 28, 29, 30]
data = np.array([[data1, data2, data3], [data4, data5, data6]])
print(data)
print('-' * 10)
print(data[0:2, 0:2, 0])
# print(data[:, ])
# print('-' * 10)
# print(data[:, :, 0:2])
# print('-' * 10)
# print(data[:, 0:2, 1])
# print('-' * 10)
# print(data[:, 1:2, :])
# print('-' * 10)
# print(data[:,1])
