import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression 
#调用机器学习库中的逻辑回归模型 若无skic-learn，命令行输入pip install sklearn 安装
from sklearn import datasets
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
for i in range(1,39):
    df = pd.read_csv('city/city'+str(i)+'.csv')
    n = 6
    data = df.copy()
    data["target"] = data['born_popularity'].shift(1)
    # for i in range(1, n+1):
    #     df['ypre_'+str(i)] = df['born_popularity'].shift(i)
    # data = df[['年份']+['ypre_'+str(i) for i in range(n, 0, -1)]+['born_popularity']]
    # print(data)
    # data = data.drop(columns="target") 
    # 提取训练集和测试集
    X_train = data[data['年份']<2020].drop(columns="target")
    y_train = data[data['年份']<2020][['target']]
    X_test = data[data['年份']>=2019].drop(columns="target")
    y_test = data[data['年份']>=2019][['target']]

    
    # 模型训练和预测
    rf = RandomForestRegressor(n_estimators=10, max_depth=5)
    rf.fit(X_train, np.ravel(y_train))
    print(X_test)
    y_pred = rf.predict(X_test)
    print(y_test)
    print(y_pred)
    
    # 结果对比绘图
    # y_test.assign(yhat=y_pred).plot()
    # plt.show()