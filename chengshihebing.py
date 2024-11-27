import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LogisticRegression 
#调用机器学习库中的逻辑回归模型 若无skic-learn，命令行输入pip install sklearn 安装
from sklearn import datasets
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
cities={}
df = pd.read_excel("B-data/人口规模.xlsx")
grouped = df.groupby('城市名称')
for key, value in grouped:
    cities[key] = {}
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['live_popularity'] =  sorted_df.loc[:,['年份','常住人口（万人）']]
    cities[key]['huju_popularity'] =  sorted_df.loc[:,['年份','户籍人口（万人）']]

df = pd.read_excel("B-data/城镇化率.xlsx")
grouped = df.groupby('城市名称')
for key, value in grouped:
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['urbanizationRate'] =  sorted_df.loc[:,['年份','urbanizationRate']]

df = pd.read_excel("B-data/就业信息.xlsx")
grouped = df.groupby('城市名称')
for key, value in grouped:
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['unemploymentRate'] =  sorted_df.loc[:,['年份','unemploymentRate']]

df = pd.read_excel("B-data/就业信息.xlsx",1)
grouped = df.groupby('城市名称')
for key, value in grouped:
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['pi_Employment'] =  sorted_df.loc[:,['年份','pi_Employment']]
    cities[key]['si_Employment'] =  sorted_df.loc[:,['年份','si_Employment']]
    cities[key]['ti_Employment'] =  sorted_df.loc[:,['年份','ti_Employment']]

df = pd.read_excel('B-data/生活水平.xlsx') 
for i in range(1,36):
    key = df.iloc[i,0]
    cities[key]['disposableIcome'] = df.iloc[[0,i],:]
    
df = pd.read_excel('B-data/生活水平.xlsx',1) 
for i in range(2,39):
    key = df.iloc[i,0]
    cities[key]["towner_ConsumptionExpenditures"] = df.iloc[[0,i],:]   

for city in cities:
    df = cities[city]
    print(city)
    with open("citybdata/"+city+".csv","w",encoding="utf-8",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(["year","live_popularity","huju_popularity","urbanizationRate","unemploymentRate",
                             "pi_Employment","si_Employment","ti_Employment",
                             "disposableIcome","towner_ConsumptionExpenditures"])
        values=["live_popularity","huju_popularity","urbanizationRate","unemploymentRate",
                             "pi_Employment","si_Employment","ti_Employment",
                             "disposableIcome","towner_ConsumptionExpenditures"]
        values_d = ["常住人口（万人）","户籍人口（万人）","urbanizationRate","unemploymentRate",
                             "pi_Employment","si_Employment","ti_Employment"]
        for i in range(2001,2022):
            writerows = []
            writerows.append(i)
            for j in range(7):
                dff = df[values[j]]
                if(len(dff[dff['年份'] == i])==0):
                    writerows.append('nan')
                    continue
                result = dff.loc[dff["年份"] == i]
                result.reset_index(drop=True,inplace=True)
                result1 = result.loc[0,values_d[j]]
                writerows.append(result1)
            if ('disposableIcome' not in cities[city]):
                writerows.append('nan')
            else:
                if i<2015:
                    writerows.append('nan')
                else:
                    dff = df["disposableIcome"]
                    dff.reset_index(drop=True,inplace=True)
                    result = dff.iloc[1,i-2013]
                    writerows.append(result)
            if ('towner_ConsumptionExpenditures' not in cities[city]):
                writerows.append('nan')
            else:
                if i<2015:
                    writerows.append('nan')
                else:
                    dff = df["towner_ConsumptionExpenditures"]
                    dff.reset_index(drop=True,inplace=True)
                    result = dff.iloc[1,i-2013]
                    writerows.append(result)
            print(writerows)

            csv_writer.writerow(writerows)
