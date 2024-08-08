'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

def dm01_鸢尾花knn分类_交叉验证网格搜索():
    # 1 获取数据集
    mydataset = load_iris()

    # 2 数据基本处理-划分数据集
    x_train, x_test, y_train ,y_test = train_test_split(mydataset.data, mydataset.target, test_size=0.2,random_state=22)

    # 3 数据集预处理-数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 4 机器学习(模型训练)
    estimator = KNeighborsClassifier()
    print('estimator-->', estimator)


# 4-2 使用校验验证网格搜索
param_grid = {'n_neighbors':[1,3,5,7]}
# 输入一个estimator, 出来一个estimator(功能变的强大)
estimator = GridSearchCV(estimator=estimator, param_grid=param_grid, cv=5)
estimator.fit(x_train, y_train)  # 4个模型 每个模型进行网格搜素找到做好的模型

# 4-3 交叉验证网格搜索结果查看
# estimator.best_score_ .best_estimator_ .best_params_ .cv_results_
print('estimator.best_score_---', estimator.best_score_)
print('estimator.best_estimator_---', estimator.best_estimator_)
print('estimator.best_params_---', estimator.best_params_)
print('estimator.cv_results_---', estimator.cv_results_)

# 4-4 保存交叉验证结果
myret = pd.DataFrame(estimator.cv_results_)
myret.to_csv(path_or_buf='./mygridsearchcv.csv')

# 5 模型评估
myscore = estimator.score(x_test, y_test)
print('myscore-->', myscore)
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.model_selection import train_test_split, GridSearchCV


def dm01_交叉验证网格搜索():
    # 1 获取数据集
    mydataset = load_iris()
    # 2 数据基本处理-划分数据集
    x_train, x_test, y_train, y_test = train_test_split(mydataset.data, mydataset.target, test_size=0.2,
                                                        random_state=22)
    # 3 数据集预处理-数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4 机器学习(模型训练)
    estimator = KNeighborsClassifier()
    param_grid = {"n_neighbors": [1, 3, 5, 7]}
    estimator = GridSearchCV(estimator, param_grid= param_grid, cv=5)
    estimator.fit(x_train, y_train)

    # 4-2 使用校验验证网格搜索
    # 4-3 交叉验证网格搜索结果查看

    print('estimator.best_score_---', estimator.best_score_)
    print('estimator.best_estimator_---', estimator.best_estimator_)
    print('estimator.best_params_---', estimator.best_params_)
    print('estimator.cv_results_---', estimator.cv_results_)

    # 4-4 保存交叉验证结果
    myret = pd.DataFrame(estimator.cv_results_)
    myret.to_csv(path_or_buf='mygridsearchcv.csv')
    # 5 模型评估
    score = estimator.score(x_test, y_test)
    print('score--', score)

if __name__ == '__main__':
    dm01_交叉验证网格搜索()
    print('dm03_交叉验证网格搜索 End')
