import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
import warnings
warnings.filterwarnings("ignore")

cities={}

#人口密度.xlsx
df = pd.read_excel('人口规模.xlsx')
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] = {}
    cities[key]['born_popularity'] = sorted_df.loc[:,['年份','户籍人口（万人）']]
    cities[key]['live_popularity'] = sorted_df.loc[:,['年份','常住人口（万人）']]
    # plt.plot(sorted_df['年份'], sorted_df['常住人口（万人）'],label=key)
    plt.plot(sorted_df['年份'], sorted_df['户籍人口（万人）'], label=key)
# with open("./popularity/live_popularity_raw.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["city","year","live_popularity"])
#     for key in cities:
#         df=cities[key]['live_popularity']
#         df.reset_index(drop=True,inplace=True)
#         print(df)
#         for i in range(1,len(df)-1):
#             csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['常住人口（万人）']])
  
# with open("./popularity/born_popularity_raw.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["city","year","born_popularity"])
#     for key in cities:
#         df=cities[key]['born_popularity']
#         df.reset_index(drop=True,inplace=True)
#         print(df)
#         for i in range(1,len(df)-1):
#             csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['户籍人口（万人）']])
          
# 插值
year=[int(i) for i in range(2000,2024)]
for key in cities:
    if ('live_popularity' not in cities[key]):
        print(key)
        continue
    df = cities[key]['live_popularity']
    df = df.dropna(axis=0,how='any')
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y = data_train['常住人口（万人）']
    clf = LinearRegression()
    clf.fit(data_train_x, data_train_y)
    for i in year:
        if(len(df[df['年份'] == i])==0):
            yred = clf.predict([[i]])
            # if i ==2006:
            #     print(key +"  :"+str(yred))
            cities[key]['live_popularity'] = cities[key]['live_popularity']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif(len(df[df['年份'] == i])==1):
            # if i ==2006:
            #     print(key)
            #     print(cities[key]['live_popularity'])
                pass
        else:
            mean_of_i=df[df['年份'] == i].mean()
            cities[key]['live_popularity']=cities[key]['live_popularity'].drop(df[df['年份'] == i].index)
            cities[key]['live_popularity'] = cities[key]['live_popularity']._append(
                pd.DataFrame([[i, mean_of_i['常住人口（万人）']]], columns=df.columns))
            
            cities[key]['live_popularity'] = cities[key]['live_popularity'].sort_values(by=['年份'],ascending=[True])
    cities[key]['live_popularity'].reset_index(drop=True)
    # print(cities[key]['popularity density'])
    # plt.plot(dff.iloc[:,0],dff.iloc[:,1],label=key)
# plt.title('live_popularity after pre process.')
# plt.xlabel('year')
# plt.ylabel('live_popularity')
# plt.legend(title='city')
# plt.grid(True)
# plt.savefig('./popularity/live_popularity_process.jpg')
# plt.show()
with open("./popularity/live_popularity_process.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city","year","live_popularity"])
    for key in cities:
        df=cities[key]['live_popularity']
        df.reset_index(drop=True,inplace=True)
        for i in range(0,len(df)-1):
            csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['常住人口（万人）']])

# with open("./popularity/live_popularity_2023.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["city_id","year","pred"])
#     for key in cities:
#         df = cities[key]['live_popularity']
#         df.reset_index(drop=True,inplace=True)
#         print(df)
#         csv_writer.writerow([key,2023,df.loc[23,'年份']])
for key in cities:
    if ('born_popularity' not in cities[key]):
        print(key)
        continue
    df = cities[key]['born_popularity']
    df = df.dropna(axis=0,how='any')
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y2 = data_train['户籍人口（万人）']
    clf2 = LinearRegression()
    clf2.fit(data_train_x, data_train_y2)
    for i in year:
        if(len(df[df['年份'] == i])==0):
            yred = clf2.predict([[i]])
            cities[key]['born_popularity'] = cities[key]['born_popularity']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif(len(df[df['年份'] == i])==1):
            pass
        else:
            mean_of_i=df[df['年份'] == i].mean()
            cities[key]['born_popularity']=cities[key]['born_popularity'].drop(df[df['年份'] == i].index)
            cities[key]['born_popularity'] = cities[key]['born_popularity']._append(
                pd.DataFrame([[i, mean_of_i['户籍人口（万人）']]], columns=df.columns))
            
            cities[key]['born_popularity'] = cities[key]['born_popularity'].sort_values(by=['年份'],ascending=[True])
    cities[key]['born_popularity'].reset_index(drop=True)
    # print(cities[key]['popularity density'])
#     dff = cities[key]['born_popularity']
#     #print(dff)
#     plt.plot(dff.iloc[:,0],dff.iloc[:,1],label=key)
# plt.title('born_popularity after pre process.')
# plt.xlabel('year')
# plt.ylabel('born_popularity')
# plt.legend(title='city')
# plt.grid(True)
# plt.savefig('./popularity/born_popularity_process.jpg')
# plt.show()
with open("./popularity/born_popularity_process.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city","year","born_popularity"])
    for key in cities:
        df=cities[key]['born_popularity']
        df.reset_index(drop=True,inplace=True)
        print(df)
        for i in range(0,len(df)-1):
            csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['户籍人口（万人）']])
