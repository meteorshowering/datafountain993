import pandas as pd
import matplotlib.pyplot as plt

cities={}

#人口密度.xlsx
df = pd.read_excel('人口密度.xlsx')
grouped = df.groupby('城市名称')
for key, value in grouped:
    print(key)
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] = {}
    cities[key]['popularity density'] = sorted_df
    # sorted_df.plot(x='年份',y = '人口密度（人/平方公里）',x_compat=True)
    # plt.xlabel('year')
    # plt.ylabel('popularity density')
    # plt.title('popularity density per year in '+key)
    # plt.show()
    
df = pd.read_excel('人口规模.xlsx')    
grouped = df.groupby('城市名称')
for key, value in grouped:
    print(key)
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key] = {}
    cities[key]['popularity density'] = sorted_df
    print(sorted_df)
    sorted_df.plot(x='年份',y = '人口密度（人/平方公里）',x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in '+key)
    plt.show()