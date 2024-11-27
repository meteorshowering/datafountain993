from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import csv
with open("born_popularity_2023_5.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])
# 示例数据 (假设已准备好)
df = pd.read_csv("city/city2.csv")
x = np.array(df.iloc[7:22,[0,3,4,9,16]].values)
print(x)
y = np.array(df.iloc[8:23,3].values)

# 线性回归预测就业率
# model1 = LinearRegression()
# model1.fit(x[:,[0]], x[:,[3]])
# pred3=model1.predict([[2023]])[0]
# print("预测第9年就业率:", pred3)

xtest = np.mean(x[-3:],axis=0)  # 用最近3年平均值
# 简单移动平均法预测下一年的就业率
xtest[0]=2023
print("预测下一年就业率:", xtest)

# 数据拆分
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 模型初始化和训练
model2 = LinearRegression()
model2.fit(X_train, y_train)

# 预测
y_pred = model2.predict([xtest])

print("测试集预测值:", y_pred)
