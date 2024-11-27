import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import csv
with open("born_popularity_2023_4.csv","w+",encoding="utf-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["city_id","year","pred"])

for i in range(1,41):
    df = pd.read_csv('city/city'+str(i)+'.csv')
    x = np.array(df.iloc[7:22,[0,2,3,4]].values)
    xtest = np.array(df.iloc[7:24,[0,2,3,4]].values)
    print(xtest)
    y = np.array(df.iloc[7:23,3].values)
    y = y[1:]


    poly_reg =PolynomialFeatures(degree=1) #三次多项式
    X_ploy =poly_reg.fit_transform(x)
    lin_reg_2=linear_model.LinearRegression()
    lin_reg_2.fit(X_ploy,y)

    xtestpply = poly_reg.fit_transform(xtest)
    predict_y =  lin_reg_2.predict(xtestpply)
    y2022 = predict_y[-1]
    with open("born_popularity_2023_4.csv","a+",encoding="utf-8",newline="") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(['city'+str(i),2023,y2022])



# predict_y =  lin_reg_2.predict(xtest)
# strError = stdError_func(predict_y, y)
# R2_1 = R2_1_func(predict_y, y)
# R2_2 = R2_2_func(predict_y, y)
# score = lin_reg_2.score(X_ploy, y) ##sklearn中自带的模型评估，与R2_1逻辑相同



