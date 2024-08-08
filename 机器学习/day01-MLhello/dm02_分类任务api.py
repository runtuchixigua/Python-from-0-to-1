# from sklearn.neighbors import KNeighborsClassifier
# def dm03_knn分类():
# 2 准备数据
# 0-喜剧片 1-动作片 2-爱情片
# x = [[39, 0, 31],   # 0
#          [3, 2, 65],    # 1
#          [2, 3, 55],    # 2
#          [9, 38, 2],    # 2
#          [8, 34, 17],   # 2
#          [5, 2, 57],    # 1
#          [21, 17, 5],   # 0
#          [45, 2, 9]]    # 0
#     y = [0, 1, 2, 2, 2, 1, 0, 0]
#
#     # 3 实例化
#     estimator = KNeighborsClassifier(n_neighbors=3)
#     print('estimator-->', estimator)
#
#     # 4 模型训练 .fit()
#     estimator.fit(x, y)
#
#     # 5 模型预测 .predict() 搞笑镜头23 拥抱镜头3 打动镜头17
#     mypre = estimator.predict([[23, 3, 17]])
#     print('mypre-->', mypre)
from sklearn.neighbors import KNeighborsClassifier

def dm02_分类任务():
    # 2 准备数据
    # 0-喜剧片 1-动作片 2-爱情片
    x = [[39, 0, 31],   # 0
         [3, 2, 65],    # 1
         [2, 3, 55],    # 2
         [9, 38, 2],    # 2
         [8, 34, 17],   # 2
         [5, 2, 57],    # 1
         [21, 17, 5],   # 0
         [45, 2, 9]]    # 0
    y = [0, 1, 2, 2, 2, 1, 0, 0]

    # 3 实例化
    estimator = KNeighborsClassifier(n_neighbors=3)
    # 4 模型训练 .fit()
    estimator.fit(x, y)
    # 5 模型预测 .predict() 搞笑镜头23 拥抱镜头3 打动镜头17
    y_pred = estimator.predict([[23, 3, 17]])
    print(y_pred)
    pass


if __name__ == '__main__':
    dm02_分类任务()
    print('dm02分类任务 End')