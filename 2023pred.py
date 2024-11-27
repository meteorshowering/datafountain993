import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression 
#调用机器学习库中的逻辑回归模型 若无skic-learn，命令行输入pip install sklearn 安装
from sklearn import datasets
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression


def logi(t,k,p0,r):
    exp_va=np.exp(r*(t-2005))
    return (k*exp_va*p0)/(k+(exp_va-1)*p0)
cities={}
# with open("B-data/人口规模.xlsx","r",encoding="utf-8",newline="") as f:
#     df = f.read_excel()
df = pd.read_excel("B-data/人口规模.xlsx")
grouped = df.groupby('城市名称')
for key, value in grouped:
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] =  sorted_df.loc[:,['年份','常住人口（万人）']]
# with open("./popularity/born_popularity_2023_3.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["city_id","year","pred"])
def logireg(xdata,ydata):    
    # for city in cities:
        # if city =="city31":
        #     with open("./popularity/live_popularity_2023_2.csv","a+",encoding="utf-8",newline="") as f:
        #         csv_writer=csv.writer(f)
        #         csv_writer.writerow([city,2023,493.0029411764717])
        #     continue
    log_reg = LogisticRegression() #调用逻辑回归库
        # df = cities[city]
        # df = df.dropna(axis=0,how='any')
        # xdata = df[['year']]
        # ydata = df[['born_popularity']]
    log_reg.fit(xdata,ydata) #训练模型
    pred = log_reg.predict([[2023]])#单例预测，预测（A=1.5，B=1.7时的C（Y）为？
    return log_reg.predict(xdata),pred[0]
        # with open("./popularity/born_popularity_2023_1.csv","a+",encoding="utf-8",newline="") as f:
        #     csv_writer=csv.writer(f)
        #     csv_writer.writerow([city,2023,pred])
def polytry(xdata,ydata):
    # for city in cities:
    #     df = cities[city]
    #     df = df.dropna(axis=0,how='any')
    #     xdata = df.loc[:,'year']
    #     ydata = df.loc[:,'born_popularity']
        f1=np.polyfit(xdata,ydata,3)
        predyaer=2023
        pred=np.polyval(f1,predyaer)
        return np.polyval(f1,xdata),pred
        # with open("./popularity/born_popularity_2023_1.csv","a+",encoding="utf-8",newline="") as f:
        #     csv_writer=csv.writer(f)
        #     csv_writer.writerow([city,2023,pred])
def lineartry(xdata,ydata):
    # for city in cities:
    #     df = cities[city]
    #     df = df.dropna(axis=0,how='any')
    #     xdata = df[['year']]
    #     ydata = df[['born_popularity']]
        clf2 = LinearRegression()
        clf2.fit(xdata, ydata)
        
        pred = clf2.predict([[2023]])
        predx = pred[0][0]
        return clf2.predict(xdata),predx
        # with open("./popularity/born_popularity_2023_2.csv","a+",encoding="utf-8",newline="") as f:
        #     csv_writer=csv.writer(f)
        #     csv_writer.writerow([city,2023,predx])
def logi2(xdata,ydata):
        popt,pcov=curve_fit(logi,xdata,ydata,maxfev=100000)
        pred = logi(2023,*popt)
        with open("./popularity/born_popularity_2023_3.csv","a+",encoding="utf-8",newline="") as f:
            csv_writer=csv.writer(f)
            csv_writer.writerow([city,2023,pred])
plt.figure()
i=1
# with open("b_born_popularity.csv","w",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["city-id","year","linear","logi","poly"])

for city in cities:
    if i>=33:
        df = cities[city]
        df = df.dropna(axis=0,how='any')
        xdata = df[['年份']]
        ydata = df[['常住人口（万人）']]
        lineaty,linearpred = lineartry(xdata,ydata)
        logiy,logipred = logireg(xdata,ydata)
        xdata = df.loc[:,'年份']
        ydata = df.loc[:,'常住人口（万人）']
        polyy,polypred = polytry(xdata,ydata)  
        # with open("b_born_popularity.csv","a+",encoding="utf-8",newline="") as f:
        #     csv_writer=csv.writer(f)
        #     csv_writer.writerow([city,2023,linearpred,logipred,polypred])

        ax = plt.subplot(4,4,i-32)
        ax.set_title(city)
        ax.scatter(xdata, ydata, c="blue")
        ax.plot(xdata,lineaty, c="red",label='linear')
        ax.plot(xdata,polyy, c="green",label='poly')
        ax.plot(xdata,logiy, c="yellow",label='logistic')
    i=i+1

plt.show()
