import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.datasets import load_iris

# 加载鸢尾花数据集，并显示属性 dataset.data .feature_names .target .target_names .DESCR
mydataset = load_iris()


def dm01_loadiris():
    print(mydataset.data[0:5])
    print(mydataset.target_names)
    print(mydataset.feature_names)
    print(mydataset.target)
    print(mydataset.DESCR)
    pass


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dm02_showiris():
    # 数据转化
    iris_pd = pd.DataFrame(mydataset.data, columns=mydataset.feature_names)
    iris_pd['target'] = mydataset.target
    print(iris_pd)

    # 画图
    sns.lmplot(x='petal length (cm)', y='petal width (cm)', data=iris_pd, hue='target', fit_reg=True)
    plt.show()


from sklearn.model_selection import train_test_split


def dm03_数据集分类():
    mydataset = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(mydataset.data, mydataset.target, test_size=0.2,
                                                        random_state=22)
    print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    pass


'''
def dm04_模型训练和预测():
    # 1 获取数据集
    mydataset = load_iris()

    # 2 数据基本处理
    x_train, x_test, y_train, y_test =  train_test_split(mydataset.data, mydataset.target, test_size=0.2, random_state=22)

    # 3 数据集预处理-数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    # 让测试集的均值和方法, 转换测试集数据;
    # 好处: 训练集测试集分布一致, 有利于模型产生更好效果
    x_test = transfer.transform(x_test)

    # 4 机器学习(模型训练)
    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train, y_train)

    # 5 模型评估 直接计算准确率 100个样本中模型预测对了多少
    myscore = estimator.score(x_test, y_test)
    print(‘myscore-->’, myscore)

    # 6 模型预测  # 需要对待预测数据,执行标准化
    print('通过模型查看分类类别-->', estimator.classes_)
    mydata =  [[5.1, 3.5, 1.4, 0.2],
                [4.6, 3.1, 1.5, 0.2]]
    mydata = transfer.transform(mydata)
    print('mydata-->', mydata)

    mypred = estimator.predict(mydata)
    print('mypred-->\n', mypred)
    mypred = estimator.predict_proba(mydata)
    print('mypred-->\n', mypred)

'''
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def dm04_鸢尾花knn分类和预测():
    # 1 获取数据集
    mydataset = load_iris()
    # 2 数据基本处理
    x_train, x_test, y_train, y_test = train_test_split(mydataset.data, mydataset.target, test_size=0.2,
                                                        random_state=22)
    # 3 数据集预处理-数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4 机器学习(模型训练)
    estimate = KNeighborsClassifier(n_neighbors=3)
    estimate.fit(x_train, y_train)
    print(estimate.classes_)
    # 5 模型评估 直接计算准确率 100个样本中模型预测对了多少
    myscore = estimate.score(x_test, y_test)
    print(myscore)
    # 6 模型预测  # 需要对待预测数据,执行标准化
    mydata = [[5.1, 3.5, 1.4, 0.2],
              [4.6, 3.1, 1.5, 0.2]]
    mydata = transfer.transform(mydata)
    y_pred1 = estimate.predict(mydata)
    y_pred2 = estimate.predict_proba(mydata)
    print(y_pred1, '\n')
    print(y_pred2, '\n')
    pass


if __name__ == '__main__':
    # dm01_loadiris()
    # dm02_showiris()
    # dm03_数据集分类()
    dm04_鸢尾花knn分类和预测()
    print('dm02_鸢尾花分类 End')
