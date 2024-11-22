"""
import numpy as np
 
y= np.array([1,1,0,0])
pred=np.array([0.8,0.9,0.01,0.1])
 
bce_loss= -np.mean(y * np.log(pred) + (1-y)* np.log(1-pred))
 
print(bce_loss)
"""
 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
data=pd.read_csv(r"C:\Training\AI_ML_Python_Training\Day05\Bank_churn_modelling.csv")
print(data.shape)
print(data.head().T)
 
print(data.columns)
 
data=data.drop(['RowNumber', 'CustomerId', 'Surname', 'Tenure', 'HasCrCard','EstimatedSalary'],axis='columns')
print(data.head().T)
 
 
 
# data preprocessing technique
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
gender_encoder= LabelEncoder()
Geo_encoder=OneHotEncoder()
data['Gender']=gender_encoder.fit_transform(data['Gender'])
out=Geo_encoder.fit_transform(data[['Geography']])
out=pd.DataFrame(out.toarray(),columns=Geo_encoder.get_feature_names_out())
newdata=pd.concat([out,data],axis='columns')
newdata=newdata.drop('Geography',axis='columns')
 
 
x=newdata.drop("Exited",axis='columns')
y=newdata["Exited"]
 
print(x.head().T)
 
from sklearn.model_selection import train_test_split
 
xtrain,xtest,ytrain,ytest=train_test_split(x,y,train_size=0.8)
 
print(xtrain.shape)
print(ytrain.shape)
print(xtest.shape)
print(ytest.shape)
 
from sklearn.linear_model import LogisticRegression
algo=LogisticRegression()
model=algo.fit(xtrain,ytrain)
 
print(model.coef_)
print(model.intercept_)
 
ypred=model.predict(xtest)
 
 
 
ypred=pd.DataFrame(ypred)
 
ytest=pd.DataFrame(ytest)
 
ytest=ytest.reset_index()
ytest=ytest['Exited']
 
 
onedata=pd.concat([ytest,ypred],axis='columns',ignore_index=True)
print(onedata.head())