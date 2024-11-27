from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR
import numpy as np
import pandas as pd
import csv
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
import warnings 
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 

warnings.filterwarnings("ignore") 
with open("born_popularity_2023_gb42.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])
for i in range(40):
    # if i<16:
    df = pd.read_csv("citybdata/city"+str(i+1)+".csv")
    print("city"+str(i+1))
    # x = np.array(df.iloc[7:23,[0,2,4,9,16]].values)
    # x = np.array(df.iloc[7:23,[0,2,4,8,11]].values)
    # x = np.array(df.iloc[7:23,[0,2,5,9]].values)
    dff = df[["live_popularity","huju_popularity","unemploymentRate","si_Employment","ti_Employment"]]
    x = np.array(dff.iloc[8:22,:].values)
    year = df[["year"]]
    plotx = np.array(year.iloc[8:22,:].values)
    print(plotx)
    # print(x)
    y = np.array(df.iloc[8:22,[1]].values) #1-live,2-born

    # 多任务回归
    # inlinemodel = LinearRegression()
    # inlinemodel = LinearSVR()
    # inlinemodel =RandomForestRegressor(n_estimators=40, max_depth=5)
    # inlinemodel =RandomForestRegressor(n_estimators=80, max_depth=5)
    inlinemodel = GradientBoostingRegressor(random_state=42)
    model = MultiOutputRegressor(inlinemodel)
    model.fit(x[:-1], np.hstack([x[1:], y[1:]]))  # 预测下一年特征+人口

    # 使用第8年的特征预测第9年
    predicted_2022_year = model.predict(x[-1].reshape(1, -1))
    predicted_features = predicted_2022_year[0, :-1]  # 下一年的特征
    predicted_population = predicted_2022_year[0, -1]  # 下一年人口
    predicted_2023_year = model.predict(predicted_features.reshape(1, -1))
    predicted_2023_population = predicted_2023_year[0, -1]
    print("预测第9年的特征:", predicted_features)
    print("预测第9年人口:", predicted_population)
    print("2023:",predicted_2023_population)
    predicty = []
    for j in range(13):
        predicted_next_year = model.predict(x[j].reshape(1, -1))
        predicty.append(predicted_next_year[0,-1])
    predicty = np.array(predicty)
    #     ax = plt.subplot(4,4,i+1)
    #     ax.set_title("city"+str(i+1))
    #     ax.scatter(plotx, y, c="blue")
    #     ax.plot(plotx[1:],predicty[:-1], c="red",label='linear')
    #     i=i+1
    # if i==16:
    #     break
# plt.show()
    with open("born_popularity_2023_gb42.csv","a",encoding="utf-8",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(["city"+str(i+1),2023,predicted_2023_population])
