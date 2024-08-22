import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# 读取 Excel 数据
data = pd.read_excel('2019.csv')

# 假设最后一列是目标变量（要预测的列）
X = data.drop(data.columns[-1], axis=1)
y = data[data.columns[-1]]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建并训练随机森林模型
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = rf_model.predict(X_test)

# 评估模型
print('均方误差：', metrics.mean_squared_error(y_test, y_pred))
print('决定系数：', metrics.r2_score(y_test, y_pred))

# 保存预测结果到新的 Excel 文件
result = pd.DataFrame({'实际值': y_test, '预测值': y_pred})
result.to_excel('prediction_result.xlsx', index=False)