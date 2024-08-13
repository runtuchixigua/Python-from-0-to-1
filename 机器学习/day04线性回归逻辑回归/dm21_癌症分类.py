# from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd


# 1 获取数据 info
# 2 基本数据处理
# 2.1 缺失值处理 .replace(to_replace="?", value=np.NaN) / data.dropna()
# 2.2 确定特征值,目标值x, y / data.iloc[:, 1:-1], data["Class"]
# 2.3 分割数据
# 3 特征工程(标准化) train_test_split
# 4 机器学习(逻辑回归) LogisticRegression
# 5 模型评估 .predict() .socre()
def dm01_LogisticRegression():
    # 1 获取数据
    data = pd.read_csv('./breast-cancer-wisconsin.csv')
    data.info()

    # 2 基本数据处理
    # 2.1 缺失值处理
    data = data.replace(to_replace="?", value=np.NaN)
    data = data.dropna()
    # 2.2 确定特征值,目标值
    x = data.iloc[:, 1:-1]
    print('x.head()-->\n', x.head())
    y = data["Class"]
    print('y.head()-->\n', y.head())
    # 2.3 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 3 特征工程(标准化)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4 机器学习(逻辑回归)
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)

    # 5 模型评估
    y_predict = estimator.predict(x_test)
    print('y_predict-->', y_predict)

    accuracy = estimator.score(x_test, y_test)
    print('accuracy-->', accuracy)


# 帮助文档
def dm02_多分类():
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    X, y = load_iris(return_X_y=True)
    # print('X-->', X)
    # print('y-->', y)
    estimator = LogisticRegression()
    # estimator = LogisticRegression(solver='saga' , random_state=0)
    # estimator = LogisticRegression(solver='liblinear' , random_state=0)
    estimator.fit(X, y)
    print('estimator.classes_-->', estimator.classes_)
    y_pred = estimator.predict(X[:, :])
    print('y_pred-->', y_pred)

    y_pred = estimator.predict_proba(X[0:5, :])
    print('y_pred-->', y_pred)

    acc = estimator.score(X, y)
    print('acc-->', acc)



if __name__ == '__main__':
    dm01_LogisticRegression()
    # dm02_多分类()
    print('逻辑回归分类 End')




#
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
#                    'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
#                    'Normal Nucleoli', 'Mitoses', 'Class']
#
#
# # 如果不加name
# def dm01_LogisticRegression():
#     data = pd.read_csv(
#         "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data")
#     data.head(3)
#
#     print('data-->\n', data)
#     pass
#
#
# def dm02_LogisticRegression():
#     data = pd.read_csv(
#         "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
#         names=names)
#     data.head(3)
#
#     print('data-->', data)
#     data.to_csv(path_or_buf='./mycsv', index=False)
#     pass
#
#
# # 文件的读
# def dm03_LogisticRegression():
#     data = pd.read_csv(filepath_or_buffer='./mycsv')
#
#     print(data.head(2))
#     # print('data-->', data)
#     pass


# def dm02_LogisticRegression():
#     # 1.获取数据
#     names = ['Sample code number',
#              'Clump Thickness',
#              'Uniformity of Cell Size',
#              'Uniformity of Cell Shape',
#              'Marginal Adhesion',
#              'Single Epithelial Cell Size',
#              'Bare Nuclei',
#              'Bland Chromatin',
#              'Normal Nucleoli',
#              'Mitoses',
#              'Class']
#
#     data = pd.read_csv(
#         "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
#         names=names)
#     data.head()
#
#     # 2.基本数据处理
#     # 2.1 缺失值处理
#     data = data.replace(to_replace="?", value=np.NaN)
#     data = data.dropna()
#     # 2.2 确定特征值,目标值
#     x = data.iloc[:, 1:-1]
#     x.head()
#     y = data["Class"]
#     y.head()
#     # 2.3 分割数据
#     x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)
#
#     # 3.特征工程(标准化)
#     transfer = StandardScaler()
#     x_train = transfer.fit_transform(x_train)
#     x_test = transfer.transform(x_test)
#
#     # 4.机器学习(逻辑回归)
#     estimator = LogisticRegression(solver='liblinear')
#     estimator.fit(x_train, y_train)
#
#     # 5.模型评估
#     y_predict = estimator.predict(x_test)
#     print('y_predict-->', y_predict)
#
#     accuracy = estimator.score(x_test, y_test)
#     print('accuracy-->', accuracy)
#     pass