import pandas as pd
import matplotlib.pyplot as plt

cities = {}

dic_of_urbanizationRate={}
df = pd.read_excel('城镇化率.xlsx')
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['urbanizationRate'] = sorted_df.loc[:, ['年份', 'urbanizationRate']]
    sorted_df.plot(x='年份',y = 'urbanizationRate',x_compat=True)
    sorted_df.plot(x='年份',secondary_y='户籍人口（万人）')
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in '+key)
    plt.savefig('./urbanization/'+str(key)+'.png')
    dic_of_urbanizationRate[key] = [len(cities[key]['urbanizationRate']), min(cities[key]['urbanizationRate']['年份']),
                                    max(cities[key]['urbanizationRate']['年份'])]

dic_of_urbanizationRate=sorted(dic_of_urbanizationRate.items(), key=lambda d: int(d[0][4:]), reverse=False)
with open('urbanizationRate.csv', 'w+', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['city', 'length','start','end'])
    for i in dic_of_urbanizationRate:
        csv_writer.writerow([i[0],i[1][0],i[1][1],i[1][2]])


dic_of_unemploymentRate={}
df = pd.read_excel('就业信息.xlsx', )
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['unemploymentRate'] = sorted_df.loc[:, ['年份', 'unemploymentRate']]
    sorted_df.plot(x='年份',y = 'unemploymentRate',x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in '+key)
    plt.savefig('./unemploymentRate/' + str(key) + '.png')
    dic_of_unemploymentRate[key]=[len(cities[key]['unemploymentRate']),min(cities[key]['unemploymentRate']['年份']),max(cities[key]['unemploymentRate']['年份'])]

dic_of_unemploymentRate=sorted(dic_of_unemploymentRate.items(), key=lambda d: int(d[0][4:]), reverse=False)
with open('unemploymentRate.csv', 'w+', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['city', 'length','start','end'])
    for i in dic_of_unemploymentRate:
        csv_writer.writerow([i[0],i[1][0],i[1][1],i[1][2]])



dic_of_employeesNumber={}
df = pd.read_excel('就业信息.xlsx', 1)
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['employeesNumber'] = sorted_df.loc[:, ['年份', 'employeesNumber']]
    dic_of_employeesNumber[key]=[len(cities[key]['employeesNumber']),min(cities[key]['employeesNumber']['年份']),max(cities[key]['employeesNumber']['年份'])]
    sorted_df.plot(x='年份', y='employeesNumber', x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in '+key)
    plt.savefig('./employeesNumber/' + str(key) + '.png')
dic_of_employeesNumber=sorted(dic_of_employeesNumber.items(), key=lambda d: int(d[0][4:]), reverse=False)
with open('employeesNumber.csv', 'w+', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['city', 'length','start','end'])
    for i in dic_of_employeesNumber:
        csv_writer.writerow([i[0],i[1][0],i[1][1],i[1][2]])


dic_of_Employment={}
df = pd.read_excel('就业信息.xlsx', 2)
grouped = df.groupby('城市名称')
for key, value in grouped:
    citynum = key.split('y')[1]
    sorted_df = value.sort_values(by='年份', ascending=True)
    cities[key]['pi_Employment'] = sorted_df.loc[:, ['年份', 'pi_Employment']]
    cities[key]['si_Employment'] = sorted_df.loc[:, ['年份', 'si_Employment']]
    cities[key]['ti_Employment'] = sorted_df.loc[:, ['年份', 'ti_Employment']]
    sorted_df.plot(x='年份', y='pi_Employment', x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in '+key)
    plt.savefig('./Employment/pi_Employment/' + str(key) + '.png')
    sorted_df.plot(x='年份', y='si_Employment', x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in ' + key)
    plt.savefig('./Employment/si_Employment/' + str(key) + '.png')
    sorted_df.plot(x='年份', y='ti_Employment', x_compat=True)
    plt.xlabel('year')
    plt.ylabel('popularity density')
    plt.title('popularity density per year in ' + key)
    plt.savefig('./Employment/ti_Employment/' + str(key) + '.png')
    dic_of_Employment[key] = [len(cities[key]['pi_Employment']), min(cities[key]['pi_Employment']['年份']),
                                   max(cities[key]['pi_Employment']['年份'])]
dic_of_Employment=sorted(dic_of_Employment.items(), key=lambda d: int(d[0][4:]), reverse=False)
with open('Employment.csv', 'w+', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['city', 'length','start','end'])
    for i in dic_of_Employment:
        csv_writer.writerow([i[0],i[1][0],i[1][1],i[1][2]])
