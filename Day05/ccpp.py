import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
data=pd.read_csv(r"Day05\combined_cycle_power_plant.csv",sep=';')
 
print(data.shape)
print(data.head())
 
#for i in data.columns:
  #  sns.histplot(data[i])
   # plt.show()
 
#for i in data.columns:
 #   sns.scatterplot(x=data[i],y=data['energy_output'])
  #  plt.show()
 
corr=data.corr()
#sns.heatmap(corr,annot=True)
#plt.show()
 
 
x=data.drop("energy_output",axis='columns')
y=data['energy_output']
print(x.head())
print(y.head())
 
 
from sklearn.model_selection import train_test_split
 
xtrain,xtest,ytrain,ytest=train_test_split(x,y,train_size=0.8)
 
print(xtrain.shape)
print(ytrain.shape)
 
print(xtest.shape)
print(ytest.shape)
 
from sklearn.linear_model import LinearRegression
 
algo=LinearRegression()
 
model=algo.fit(xtrain,ytrain)
 
print(model.coef_)
print(model.intercept_)
 
########## Predict ########
ypred=model.predict(xtest)
print(type(ypred))


ypred=model.predict(xtest)
 
 
ypred=pd.DataFrame(ypred)
 
ytest=pd.DataFrame(ytest)
 
ytest=ytest.reset_index()
ytest=ytest['energy_output']
 
 
onedata=pd.concat([ytest,ypred],axis='columns',ignore_index=True)
print(onedata.head())


from sklearn.metrics import mean_squared_error
import numpy as np

print(np.sqrt(mean_squared_error(ytest,ypred)))

import joblib as jb
jb.dump(model,r'Day05\ccpp_model.pkl')