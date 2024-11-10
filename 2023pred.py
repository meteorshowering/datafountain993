import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression 
#调用机器学习库中的逻辑回归模型 若无skic-learn，命令行输入pip install sklearn 安装
from sklearn import datasets
from scipy.optimize import curve_fit

def logi(t,k,p0,r):
    exp_va=np.exp(r*(t-2005))
    return (k*exp_va*p0)/(k+(exp_va-1)*p0)
cities={}
df = pd.read_csv('popularity/live_popularity_raw.csv')
grouped = df.groupby('city')
for key, value in grouped:
    sorted_df = value.sort_values(by='year', ascending=True)
    cities[key] =  sorted_df.loc[:,['year','live_popularity']]
with open("./popularity/live_popularity_2023_3.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])
    

for city in cities:
    # if city =="city31":
    #     with open("./popularity/live_popularity_2023_2.csv","a+",encoding="utf-8",newline="") as f:
    #         csv_writer=csv.writer(f)
    #         csv_writer.writerow([city,2023,493.0029411764717])
    #     continue
    log_reg = LogisticRegression() #调用逻辑回归库
    df = cities[city]
    df = df.dropna(axis=0,how='any')
    xdata=df.loc[:,'year']
    ydata=df.loc[:,'live_popularity']
    # popt,pcov=curve_fit(logi,xdata,ydata,maxfev=100000)
    f1=np.polyfit(xdata,ydata,3)
    predyaer=2023
    # pred = logi(predyaer,*popt)
    pred=np.polyval(f1,predyaer)
    with open("./popularity/live_popularity_2023_3.csv","a+",encoding="utf-8",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow([city,2023,pred])

# log_reg.fit(X1,y1) #训练模型
# #print(a)
# print(log_reg.intercept_,log_reg.coef_) #输出预测参数
# #plt.scatter(X1[:,0],X1[:,1])
# log_reg.predict([[1.5,1.7]])#单例预测，预测（A=1.5，B=1.7时的C（Y）为？
# log_reg.score(X1,y1)#模型训练结果评估，输出准确率



