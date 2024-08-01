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
    sns.lmplot(x='petal length (cm)', y='petal width (cm)', data=iris_pd, hue='target', fit_reg=False)
    plt.show()


# dm03_数据集划分()
# dm04_鸢尾花knn分类训和预测()
# dm05_鸢尾花knn分类 模型评估()

if __name__ == '__main__':
    # dm01_loadiris()
    dm02_showiris()
    print('dm02_鸢尾花分类 End')
