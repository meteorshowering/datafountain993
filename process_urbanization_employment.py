import pandas as pd
import matplotlib.pyplot as plt
import csv
import os
from sklearn.linear_model import LinearRegression


cities = {}


df = pd.read_excel('城镇化率.xlsx')
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    cities[key] = {}
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['urbanizationRate'] = sorted_df.loc[:, ['年份', 'urbanizationRate']]


df = pd.read_excel('就业信息.xlsx', )
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['unemploymentRate'] = sorted_df.loc[:, ['年份', 'unemploymentRate']]


df = pd.read_excel('就业信息.xlsx', 1)
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['employeesNumber'] = sorted_df.loc[:, ['年份', 'employeesNumber']]

df = pd.read_excel('就业信息.xlsx', 2)
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['pi_Employment'] = sorted_df.loc[:, ['年份', 'pi_Employment']]
    cities[key]['si_Employment'] = sorted_df.loc[:, ['年份', 'si_Employment']]
    cities[key]['ti_Employment'] = sorted_df.loc[:, ['年份', 'ti_Employment']]

print("Done read")
# process of raw data(mean) 2000-2022
# urbanizationRate
# NAN填写，删除重复值
year=[int(i) for i in range(2000,2023)]


# for key in cities:
#     df = cities[key]['urbanizationRate']
#     mean_of_urbanizationRate=cities[key]['urbanizationRate']['urbanizationRate'].mean()
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             cities[key]['urbanizationRate'] = cities[key]['urbanizationRate']._append(pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['urbanizationRate']=cities[key]['urbanizationRate']._drop(df['年份'] == i)
#             # 重新写入
#             cities[key]['urbanizationRate'] = cities[key]['urbanizationRate']._append(
#                 pd.DataFrame([[i, mean_of_i]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['urbanizationRate'] = cities[key]['urbanizationRate'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['urbanizationRate'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/urbanizationRate/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['urbanizationRate'].to_csv(f)


# process of raw data(linear) 2000-2022


# for key in cities:
#     df = cities[key]['urbanizationRate']
#     # 训练
#     data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
#     data_train_x = data_train[['年份']]
#     data_train_y = data_train['urbanizationRate']
#     clf = LinearRegression()
#     clf.fit(data_train_x, data_train_y)
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             yred=clf.predict([[i]])
#             cities[key]['urbanizationRate'] = cities[key]['urbanizationRate']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['urbanizationRate']=cities[key]['urbanizationRate']._drop(df['年份'] == i)
#             # 重新写入
#             cities[key]['urbanizationRate'] = cities[key]['urbanizationRate']._append(
#                 pd.DataFrame([[i, mean_of_i]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['urbanizationRate'] = cities[key]['urbanizationRate'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['urbanizationRate'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/urbanizationRate/linear_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['urbanizationRate'].to_csv(f)



# for key in cities:
#     if('unemploymentRate' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['unemploymentRate']
#     mean_of_urbanizationRate=cities[key]['unemploymentRate']['unemploymentRate'].mean()
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             cities[key]['unemploymentRate'] = cities[key]['unemploymentRate']._append(pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['unemploymentRate']=cities[key]['unemploymentRate']._drop(df['年份'] == i)
#             # 重新写入
#             cities[key]['unemploymentRate'] = cities[key]['unemploymentRate']._append(
#                 pd.DataFrame([[i, mean_of_i]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['unemploymentRate'] = cities[key]['unemploymentRate'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['unemploymentRate'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/unemploymentRate/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['unemploymentRate'].to_csv(f)


# 读取所有文件，对city13 city34补全
# mean_of_city={}
# result=os.listdir("./processdata/unemploymentRate/mean_data")
# for city in result:
#     with open("./processdata/unemploymentRate/mean_data/" + city, "r", encoding="utf-8") as f:
#         csv_reader = csv.reader(f)
#         i=0
#         for row in csv_reader:
#             if(i==0):
#                 i += 1
#                 continue
#
#             else:
#                 i+=1
#                 if(int(row[0]) not in mean_of_city):
#                     mean_of_city[int(row[0])]=float(row[1])
#                 else:
#                     mean_of_city[int(row[0])]+=float(row[1])
# mean_of_city=sorted(mean_of_city.items(), key=lambda d: d[0], reverse=False)
# with open("./processdata/unemploymentRate/mean_data/city13.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","unemploymentRate"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/unemploymentRate/mean_data/city34.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","unemploymentRate"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])


# for key in cities:
#     if('unemploymentRate' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['unemploymentRate']
#     # 训练
#     data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
#     data_train_x = data_train[['年份']]
#     data_train_y = data_train['unemploymentRate']
#     clf = LinearRegression()
#     clf.fit(data_train_x, data_train_y)
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             yred = clf.predict([[i]])
#             cities[key]['unemploymentRate'] = cities[key]['unemploymentRate']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['unemploymentRate']=cities[key]['unemploymentRate']._drop(df['年份'] == i)
#             # 重新写入
#             cities[key]['unemploymentRate'] = cities[key]['unemploymentRate']._append(
#                 pd.DataFrame([[i, mean_of_i]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['unemploymentRate'] = cities[key]['unemploymentRate'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['unemploymentRate'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/unemploymentRate/linear_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['unemploymentRate'].to_csv(f)

# 读取所有文件，对city13 city34补全
# mean_of_city={}
# result=os.listdir("./processdata/unemploymentRate/linear_data")
# for city in result:
#     with open("./processdata/unemploymentRate/linear_data/" + city, "r", encoding="utf-8") as f:
#         csv_reader = csv.reader(f)
#         i=0
#         for row in csv_reader:
#             if(i==0):
#                 i += 1
#                 continue
#
#             else:
#                 i+=1
#                 if(int(row[0]) not in mean_of_city):
#                     mean_of_city[int(row[0])]=float(row[1])
#                 else:
#                     mean_of_city[int(row[0])]+=float(row[1])
# mean_of_city=sorted(mean_of_city.items(), key=lambda d: d[0], reverse=False)
# with open("./processdata/unemploymentRate/linear_data/city13.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","unemploymentRate"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/unemploymentRate/linear_data/city34.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","unemploymentRate"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])

# employeesNumber mean
# for key in cities:
#     if('employeesNumber' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['employeesNumber']
#     mean_of_urbanizationRate=cities[key]['employeesNumber']['employeesNumber'].mean()
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             cities[key]['employeesNumber'] = cities[key]['employeesNumber']._append(pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['employeesNumber']=cities[key]['employeesNumber'].drop(df[df['年份'] == i].index)
#             # 重新写入
#             cities[key]['employeesNumber'] = cities[key]['employeesNumber']._append(
#                 pd.DataFrame([[i, mean_of_i['employeesNumber']]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['employeesNumber'] = cities[key]['employeesNumber'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['employeesNumber'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/employeesNumber/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['employeesNumber'].to_csv(f)

# 读取所有文件，对city26
# city30
# city34
# city37
# city40补全


# mean_of_city={}
# result=os.listdir("./processdata/employeesNumber/mean_data")
# for city in result:
#     with open("./processdata/employeesNumber/mean_data/" + city, "r", encoding="utf-8") as f:
#         csv_reader = csv.reader(f)
#         i=0
#         for row in csv_reader:
#             if(i==0):
#                 i += 1
#                 continue
#
#             else:
#                 i+=1
#                 if(int(row[0]) not in mean_of_city):
#                     mean_of_city[int(row[0])]=float(row[1])
#                 else:
#                     mean_of_city[int(row[0])]+=float(row[1])
# mean_of_city=sorted(mean_of_city.items(), key=lambda d: d[0], reverse=False)
# with open("./processdata/employeesNumber/mean_data/city26.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/mean_data/city30.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
#
# with open("./processdata/employeesNumber/mean_data/city34.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/mean_data/city37.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/mean_data/city40.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])


# employeesNumber linear
# for key in cities:
#     if('employeesNumber' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['employeesNumber']
#     # 训练
#     data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
#     data_train_x = data_train[['年份']]
#     data_train_y = data_train['employeesNumber']
#     clf = LinearRegression()
#     clf.fit(data_train_x, data_train_y)
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#                 yred = clf.predict([[i]])
#                 cities[key]['employeesNumber'] = cities[key]['employeesNumber']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['employeesNumber']=cities[key]['employeesNumber'].drop(df[df['年份'] == i].index)
#             # 重新写入
#             cities[key]['employeesNumber'] = cities[key]['employeesNumber']._append(
#                 pd.DataFrame([[i, mean_of_i['employeesNumber']]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['employeesNumber'] = cities[key]['employeesNumber'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['employeesNumber'].set_index('年份', inplace=True)
#     # 写入文件
#     with open("./processdata/employeesNumber/linear_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         cities[key]['employeesNumber'].to_csv(f)


# 读取所有文件，对city26
# city30
# city34
# city37
# city40补全


# mean_of_city={}
# result=os.listdir("./processdata/employeesNumber/linear_data")
# for city in result:
#     with open("./processdata/employeesNumber/linear_data/" + city, "r", encoding="utf-8") as f:
#         csv_reader = csv.reader(f)
#         i=0
#         for row in csv_reader:
#             if(i==0):
#                 i += 1
#                 continue
#
#             else:
#                 i+=1
#                 if(int(row[0]) not in mean_of_city):
#                     mean_of_city[int(row[0])]=float(row[1])
#                 else:
#                     mean_of_city[int(row[0])]+=float(row[1])
# mean_of_city=sorted(mean_of_city.items(), key=lambda d: d[0], reverse=False)
# with open("./processdata/employeesNumber/linear_data/city26.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/linear_data/city30.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
#
# with open("./processdata/employeesNumber/linear_data/city34.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/linear_data/city37.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])
#
# with open("./processdata/employeesNumber/linear_data/city40.csv","w+",encoding="utf-8",newline="") as f:
#     csv_writer=csv.writer(f)
#     csv_writer.writerow(["年份","employeesNumber"])
#     for i in mean_of_city:
#         csv_writer.writerow([i[0],i[1]/len(result)])



# Employment mean
# for key in cities:
#     print('pi_Employment')
#     if('pi_Employment' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['pi_Employment']
#     mean_of_urbanizationRate=cities[key]['pi_Employment']['pi_Employment'].mean()
#     for i in year:
#         if(len(df[df['年份'] == i])==0):
#             cities[key]['pi_Employment'] = cities[key]['pi_Employment']._append(pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif(len(df[df['年份'] == i])==1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i=df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['pi_Employment']=cities[key]['pi_Employment'].drop(df[df['年份'] == i].index)
#             # 重新写入
#             cities[key]['pi_Employment'] = cities[key]['pi_Employment']._append(
#                 pd.DataFrame([[i, mean_of_i['pi_Employment']]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['pi_Employment'] = cities[key]['pi_Employment'].sort_values(by=['年份'],ascending=[True])
#     cities[key]['pi_Employment'].set_index('年份', inplace=True)
# for key in cities:
#     print('si_Employment')
#     if ('si_Employment' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['si_Employment']
#     mean_of_urbanizationRate = cities[key]['si_Employment']['si_Employment'].mean()
#     for i in year:
#         if (len(df[df['年份'] == i]) == 0):
#             cities[key]['si_Employment'] = cities[key]['si_Employment']._append(
#                 pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif (len(df[df['年份'] == i]) == 1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i = df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['si_Employment'] = cities[key]['si_Employment'].drop(df[df['年份'] == i].index)
#             # 重新写入
#             cities[key]['si_Employment'] = cities[key]['si_Employment']._append(
#                 pd.DataFrame([[i, mean_of_i['si_Employment']]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['si_Employment'] = cities[key]['si_Employment'].sort_values(by=['年份'], ascending=[True])
#     cities[key]['si_Employment'].set_index('年份', inplace=True)
#     # 写入文件
#     # with open("./processdata/employeesNumber/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#     #     cities[key]['employeesNumber'].to_csv(f)
# for key in cities:
#     print('ti_Employment')
#     if ('ti_Employment' not in cities[key]):
#         print(key)
#         continue
#     df = cities[key]['ti_Employment']
#     mean_of_urbanizationRate = cities[key]['ti_Employment']['ti_Employment'].mean()
#     for i in year:
#         if (len(df[df['年份'] == i]) == 0):
#             cities[key]['ti_Employment'] = cities[key]['ti_Employment']._append(
#                 pd.DataFrame([[i, mean_of_urbanizationRate]], columns=df.columns))
#         elif (len(df[df['年份'] == i]) == 1):
#             pass
#         else:
#             # 计算平均值
#             mean_of_i = df[df['年份'] == i].mean()
#             # 删除
#             cities[key]['ti_Employment'] = cities[key]['ti_Employment'].drop(df[df['年份'] == i].index)
#             # 重新写入
#             cities[key]['ti_Employment'] = cities[key]['ti_Employment']._append(
#                 pd.DataFrame([[i, mean_of_i['ti_Employment']]], columns=df.columns))
#     # 对所有的编号重新排序索引
#     cities[key]['ti_Employment'] = cities[key]['ti_Employment'].sort_values(by=['年份'], ascending=[True])
#     cities[key]['ti_Employment'].set_index('年份', inplace=True)
#
# print(cities)
#
# # 写入文件
# for key in cities:
#     with open("./processdata/Employment/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
#         csv_writer=csv.writer(f)
#         csv_writer.writerow(["年份",	"pi_Employment","si_Employment","ti_Employment"])
#         df1=cities[key]["pi_Employment"]
#         df2 = cities[key]["si_Employment"]
#         df3 = cities[key]["ti_Employment"]
#         for i in year:
#             data1=df1.loc[i]["pi_Employment"]
#             data2=df2.loc[i]["si_Employment"]
#             data3 = df3.loc[i]["ti_Employment"]
#             csv_writer.writerow([i,data1,data2,data3])


for key in cities:
    print('pi_Employment')
    if('pi_Employment' not in cities[key]):
        print(key)
        continue
    df = cities[key]['pi_Employment']
    # 训练
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y = data_train['pi_Employment']
    clf = LinearRegression()
    clf.fit(data_train_x, data_train_y)
    for i in year:
        if(len(df[df['年份'] == i])==0):
            yred = clf.predict([[i]])
            cities[key]['pi_Employment'] = cities[key]['pi_Employment']._append(pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif(len(df[df['年份'] == i])==1):
            pass
        else:
            # 计算平均值
            mean_of_i=df[df['年份'] == i].mean()
            # 删除
            cities[key]['pi_Employment']=cities[key]['pi_Employment'].drop(df[df['年份'] == i].index)
            # 重新写入
            cities[key]['pi_Employment'] = cities[key]['pi_Employment']._append(
                pd.DataFrame([[i, mean_of_i['pi_Employment']]], columns=df.columns))
    # 对所有的编号重新排序索引
    cities[key]['pi_Employment'] = cities[key]['pi_Employment'].sort_values(by=['年份'],ascending=[True])
    cities[key]['pi_Employment'].set_index('年份', inplace=True)
for key in cities:
    print('si_Employment')
    if ('si_Employment' not in cities[key]):
        print(key)
        continue
    df = cities[key]['si_Employment']
    # 训练
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y = data_train['si_Employment']
    clf = LinearRegression()
    clf.fit(data_train_x, data_train_y)
    for i in year:
        if (len(df[df['年份'] == i]) == 0):
            yred = clf.predict([[i]])
            cities[key]['si_Employment'] = cities[key]['si_Employment']._append(
                pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif (len(df[df['年份'] == i]) == 1):
            pass
        else:
            # 计算平均值
            mean_of_i = df[df['年份'] == i].mean()
            # 删除
            cities[key]['si_Employment'] = cities[key]['si_Employment'].drop(df[df['年份'] == i].index)
            # 重新写入
            cities[key]['si_Employment'] = cities[key]['si_Employment']._append(
                pd.DataFrame([[i, mean_of_i['si_Employment']]], columns=df.columns))
    # 对所有的编号重新排序索引
    cities[key]['si_Employment'] = cities[key]['si_Employment'].sort_values(by=['年份'], ascending=[True])
    cities[key]['si_Employment'].set_index('年份', inplace=True)
    # 写入文件
    # with open("./processdata/employeesNumber/mean_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
    #     cities[key]['employeesNumber'].to_csv(f)
for key in cities:
    print('ti_Employment')
    if ('ti_Employment' not in cities[key]):
        print(key)
        continue
    df = cities[key]['ti_Employment']
    # 训练
    data_train = df.iloc[[int(i) for i in range(0, int(0.8 * len(df)))]]
    data_train_x = data_train[['年份']]
    data_train_y = data_train['ti_Employment']
    clf = LinearRegression()
    clf.fit(data_train_x, data_train_y)
    for i in year:
        if (len(df[df['年份'] == i]) == 0):
            yred = clf.predict([[i]])
            cities[key]['ti_Employment'] = cities[key]['ti_Employment']._append(
                pd.DataFrame([[i, yred[0]]], columns=df.columns))
        elif (len(df[df['年份'] == i]) == 1):
            pass
        else:
            # 计算平均值
            mean_of_i = df[df['年份'] == i].mean()
            # 删除
            cities[key]['ti_Employment'] = cities[key]['ti_Employment'].drop(df[df['年份'] == i].index)
            # 重新写入
            cities[key]['ti_Employment'] = cities[key]['ti_Employment']._append(
                pd.DataFrame([[i, mean_of_i['ti_Employment']]], columns=df.columns))
    # 对所有的编号重新排序索引
    cities[key]['ti_Employment'] = cities[key]['ti_Employment'].sort_values(by=['年份'], ascending=[True])
    cities[key]['ti_Employment'].set_index('年份', inplace=True)

print(cities)

# 写入文件
for key in cities:
    with open("./processdata/Employment/linear_data/"+str(key)+".csv","w+",encoding="utf-8",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(["年份",	"pi_Employment","si_Employment","ti_Employment"])
        df1=cities[key]["pi_Employment"]
        df2 = cities[key]["si_Employment"]
        df3 = cities[key]["ti_Employment"]
        for i in year:
            data1=df1.loc[i]["pi_Employment"]
            data2=df2.loc[i]["si_Employment"]
            data3 = df3.loc[i]["ti_Employment"]
            csv_writer.writerow([i,data1,data2,data3])