import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
 
cities={}

#人口密度.xlsx
df = pd.read_excel('人口密度.xlsx')
grouped = df.groupby('城市名称')
plt.figure()
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] = {}
    cities[key]['popularity density'] = sorted_df.loc[:,['年份','人口密度（人/平方公里）']]
    # sorted_df.plot(x='年份',y = '人口密度（人/平方公里）',x_compat=True)
    # print(sorted_df)
    plt.plot(sorted_df['年份'], sorted_df['人口密度（人/平方公里）'], label=key)
plt.title('popularity dense before pre process.')
plt.xlabel('year')
plt.ylabel('popularity dense')
plt.legend(title='city')
plt.grid(True)
plt.show()

year=[int(i) for i in range(2000,2023)]

with open("./popularity_dense/raw.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city","year","popularity_dense"])
    for key in cities:
        df=cities[key]['popularity density']
        df.reset_index(drop=True,inplace=True)
        print(df)
        for i in range(1,len(df)-1):
            csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['人口密度（人/平方公里）']])
            
plt.figure()
for key in cities:
    if ('popularity density' not in cities[key]):
        print(key)
        continue
    df = cities[key]['popularity density']
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y = data_train['人口密度（人/平方公里）']
    clf = LinearRegression()
    clf.fit(data_train_x, data_train_y)
    for i in year:
        if(len(df[df['年份'] == i])==0):
            yred = clf.predict([[i]])
            cities[key]['popularity density'] = cities[key]['popularity density']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif(len(df[df['年份'] == i])==1):
            pass
        else:
            # 计算平均值
            mean_of_i=df[df['年份'] == i].mean()
            # 删除
            cities[key]['popularity density']=cities[key]['popularity density'].drop(df[df['年份'] == i].index)
            # 重新写入
            cities[key]['popularity density'] = cities[key]['popularity density']._append(
                pd.DataFrame([[i, mean_of_i['人口密度（人/平方公里）']]], columns=df.columns))
    # 对所有的编号重新排序索引
    cities[key]['popularity density'] = cities[key]['popularity density'].sort_values(by=['年份'],ascending=[True])
    # cities[key]['popularity density'] = cities[key]['popularity density'].drop(index = False,header=False)
    cities[key]['popularity density'].reset_index(drop=True)
    # print(cities[key]['popularity density'])
    dff = cities[key]['popularity density']
    #print(dff)
    plt.plot(dff.iloc[:,0],dff.iloc[:,1],label=key)
plt.title('popularity dense after pre process.')
plt.xlabel('year')
plt.ylabel('popularity dense')
plt.legend(title='city')
plt.grid(True)
plt.show()

year=[int(i) for i in range(2000,2023)]

with open("./popularity_dense/process.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city","year","popularity_dense"])
    for key in cities:
        df=cities[key]['popularity density']
        df.reset_index(drop=True,inplace=True)
        print(df)
        for i in range(1,len(df)-1):
            csv_writer.writerow([key,df.loc[i]['年份'],df.loc[i]['人口密度（人/平方公里）']])
    
# df = pd.read_excel('人口规模.xlsx')    
# grouped = df.groupby('城市名称')
# for key, value in grouped:
#     citynum = key.split('y')[1]
#     sorted_df = value.sort_values(by='年份', ascending=True)
#     cities[key]['changzhupopularity'] = sorted_df.loc[:,['年份','常住人口（万人）']]
#     cities[key]['hujipopularity'] = sorted_df.loc[:,['年份','户籍人口（万人）']]
#     sorted_df.plot(x='年份',y = '常住人口（万人）',x_compat=True)
#     sorted_df.plot(x='年份',secondary_y='户籍人口（万人）')
