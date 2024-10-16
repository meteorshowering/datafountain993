import pandas as pd
import matplotlib.pyplot as plt

cities={}

#人口密度.xlsx
df = pd.read_excel('人口密度.xlsx')
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] = {}
    cities[key]['popularity density'] = sorted_df.loc[:,['年份','人口密度（人/平方公里）']]
    # sorted_df.plot(x='年份',y = '人口密度（人/平方公里）',x_compat=True)
    # plt.xlabel('year')
    # plt.ylabel('popularity density')
    # plt.title('popularity density per year in '+key)
    # plt.show()
    
df = pd.read_excel('人口规模.xlsx')    
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['changzhupopularity'] = sorted_df.loc[:,['年份','常住人口（万人）']]
    cities[key]['hujipopularity'] = sorted_df.loc[:,['年份','户籍人口（万人）']]
    # sorted_df.plot(x='年份',y = '常住人口（万人）',x_compat=True)
    # sorted_df.plot(x='年份',secondary_y='户籍人口（万人）')
    # plt.xlabel('year')
    # plt.ylabel('popularity density')
    # plt.title('popularity density per year in '+key)
    # plt.show()
    
df = pd.read_excel('城镇化率.xlsx')    
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['urbanizationRate'] = sorted_df.loc[:,['年份','urbanizationRate']]
    # sorted_df.plot(x='年份',y = 'urbanizationRate',x_compat=True)
    # sorted_df.plot(x='年份',secondary_y='户籍人口（万人）')
    # plt.xlabel('year')
    # plt.ylabel('popularity density')
    # plt.title('popularity density per year in '+key)
    # plt.show()
    
df = pd.read_excel('就业信息.xlsx',)    
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['unemploymentRate'] = sorted_df.loc[:,['年份','unemploymentRate']]
    # sorted_df.plot(x='年份',y = 'unemploymentRate',x_compat=True)
    # plt.xlabel('year')
    # plt.ylabel('popularity density')
    # plt.title('popularity density per year in '+key)
    # plt.show()
 
df = pd.read_excel('就业信息.xlsx',1)    
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['employeesNumber'] = sorted_df.loc[:,['年份','employeesNumber']]
       
df = pd.read_excel('就业信息.xlsx',2)    
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['pi_Employment'] = sorted_df.loc[:,['年份','pi_Employment']]
    cities[key]['si_Employment'] = sorted_df.loc[:,['年份','si_Employment']]
    cities[key]['ti_Employment'] = sorted_df.loc[:,['年份','ti_Employment']]
    
df = pd.read_excel('工资水平.xlsx')   
for i in range(1,40):
    key = "city"+str(i)
    df2 = df.loc[:,['averageWage',key]]
    cities[key]['averageWage'] = df2
    
df = pd.read_excel('年龄结构.xlsx')    
grouped = df.groupby('城市')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['0-14'] = sorted_df.loc[:,['年份','0-14']]
    cities[key]['15-64'] = sorted_df.loc[:,['年份','15-64']]
    cities[key]['65+'] = sorted_df.loc[:,['年份','65+']]

df = pd.read_excel('生活水平.xlsx') 
for i in range(2,23):
    key = df.iloc[i,0]
    cities[key]['disposableIcome'] = df.iloc[[0,i],:]
    
df = pd.read_excel('生活水平.xlsx',1) 
for i in range(2,24):
    key = df.iloc[i,0]
    cities[key]['consumptionExpenditures'] = df.iloc[[0,i],:]
    
df = pd.read_excel('生活水平.xlsx',2) 
for i in range(2,29):
    key = df.iloc[i,0]
    cities[key]['towner_ ConsumptionExpenditures'] = df.iloc[[0,i],:]
    
df = pd.read_excel('生活水平.xlsx',3) 
for i in range(2,23):
    key = df.iloc[i,0]
    cities[key]['rural_ConsumptionExpenditures'] = df.iloc[[0,i],:]

df = pd.read_excel('生活水平.xlsx',4) 
for i in range(2,34):
    key = df.iloc[i,0]
    cities[key]['towner_disposableIcome'] = df.iloc[[0,i],:]
    
df = pd.read_excel('生活水平.xlsx',4) 
for i in range(2,29):
    key = df.iloc[i,0]
    cities[key]['rural_disposableIcome'] = df.iloc[[0,i],:]

print(cities)