# 导入 paddle
import paddle
import paddle.nn.functional as F

# 导入其他模块
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
print(paddle.__version__)
import paddle.nn as nn
from sklearn import preprocessing
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("city/city1.csv")
df = df.dropna(axis=0,how='any')
test_split=round(len(df)*0.20)
df_for_training=df[:-test_split]
df_for_testing=df[-test_split:]
# 将数据归一化到 0~1 范围
scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
df_for_training_scaled = scaler.fit_transform(df_for_training)
df_for_testing_scaled=scaler.transform(df_for_testing)
print(df_for_training_scaled)

def createXY(dataset,n_past):
    trainY = dataset[0:n_past,3]
    trainX = dataset[0:n_past,0:2]
    return trainX,trainY

 
window_size = 6
trainX,trainY=createXY(df_for_training_scaled,window_size)
testX,testY=createXY(df_for_testing_scaled,window_size)
print(trainY)
print(trainY[0])
print(trainY[0])
 
# 将数据集转换为 LSTM 模型所需的形状（样本数，时间步长，特征数）
trainX = np.reshape(df_for_training_scaled, (df_for_training_scaled.shape[0], window_size, 5))
testX = np.reshape(df_for_training_scaled, (df_for_training_scaled.shape[0], window_size, 5))
 
print("trainX Shape-- ",trainX.shape)
print("trainY Shape-- ",trainY.shape)
print("testX Shape-- ",testX.shape)
print("testY Shape-- ",testY.shape)

def build_model(optimizer):
    grid_model = nn.Sequential()
    grid_model.add(nn.LSTM(50,return_sequences=True,input_shape=(30,5)))
    grid_model.add(nn.LSTM(50))
    grid_model.add(nn.Dropout(0.2))
    grid_model.add(nn.Dense(1))
 
    grid_model.compile(loss = 'mse',optimizer = optimizer)
    return grid_model
 
grid_model = KerasRegressor(build_fn=build_model,verbose=1,validation_data=(testX,testY))
parameters = {'batch_size' : [16,20],
              'epochs' : [8,10],
              'optimizer' : ['adam','Adadelta'] }
 
grid_search  = GridSearchCV(estimator = grid_model,
                            param_grid = parameters,
                            cv = 2)
grid_search = grid_search.fit(trainX,trainY)
print(grid_search.best_params_)
my_model=grid_search.best_estimator_.model