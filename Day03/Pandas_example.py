import pandas as pd

data=pd.read_csv(r"C:\Training\AI_ML_Python_Training\Day02\insurance.csv")

print("unique->\n"+(data['region'].unique()))

print("\nNunique->\n"+str(data['region'].nunique()))

print("\nValue Counts->\n"+str(data['region'].value_counts()))

print("\naxis='COLUMNS'->\n"+str(data.drop('age',axis='columns')))

print("\naxis='ROWS'->\n"+str(data.drop([1,4,5],axis='rows')))

sample=data.drop([1,4,5],axis='rows').head()

print("\nsample data\n")
print((sample))

#loc & iloc

print("\nsample.loc[3,['bmi','children']]\n")
print((sample.loc[3,['bmi','children']]))

print("\nsample.loc[[3,6,7],['bmi','children']]\n")
print((sample.loc[[3,6,7],['bmi','children']]))

print("\nsample.iloc[[2,3,4],[2,3]]\n")
print((sample.iloc[[2,3,4],[2,3]]))

print("\nsample.iloc[2:5,2:4]\n")
print((sample.iloc[2:5,2:4])) #2:5 -> from 2nd column to 5th row

print("\nsample.iloc[2:5,:]\n")
print((sample.iloc[2:5,:])) #include all column ' : ' -> from starting : ending

print("\nsample.iloc[2:5,3:]\n")
print((sample.iloc[2:5,3:]))

print("\nsample.iloc[2:5,:3]\n")
print((sample.iloc[2:5,:3]))

print("\ndata.iloc[1000:1030,:]\n")
print(data.iloc[1000:1030,:])


info={"name":["javeed","jhon","jessica","ankit"],
      "age":[23,45,35,46],
      "cc_score":[678,789,810,450]}

info=pd.DataFrame(info,index=['a','b','c','d'])
print("\nINFO for Sample Json\n")
print(info)

print("\ninfo.loc[['b','c'],['age','cc_score']]\n")
print(info.loc[['b','c'],['age','cc_score']])

print("\ninfo.iloc[1:3,1:]\n")
print(info.iloc[1:3,1:])

print("\ninfo.iloc[1:3,0:3:2]\n")
print(info.iloc[1:3,0:3:2])


# filter data

print(data[data['age']>60])

print(data[data['age']>60].shape[0])

print(data[(data['age'] > 60) & (data['sex'] == 'male')])

print(data[(data['region']=='northeast')&(data['bmi']>23.45)])

print(data[data['sex']!='male'])

print(data.sort_values('age',ascending=True))

print(data.sort_values('bmi',ascending=False))

print(data.sort_values(['age','charges'],ascending=False))


print(data.describe())
print(data['age'].mean())
print(data['age'].max())
print(data['age'].min())
print(data['age'].std())


print(data[['bmi','age','charges']].corr())


gdata=data.groupby('region')

for a,b in gdata:
    print(a)
    print(b)


nw=gdata.get_group('northwest')
print(nw)

gdata=data.groupby('region')
print(gdata.get_group('northwest')['age'].mean())


newdata=data.groupby(['region','smoker'])
print("\n'region','smoker' Mean()")
print(newdata.get_group(('northwest','yes'))['age'].mean())
print(newdata.get_group(('northwest','no'))['age'].mean())


def trans(c):
    if c>10000:
        return "HIGH"
    else:
        return "LOW"
    
data['c_h_l']=data['charges'].apply(trans)

print(data.head())

data['b_l_h']=data['bmi'].apply(lambda x: "HIGH" if x>22.23 else "LOW")

print(data)

data['update_charges']=data['charges']+100

print(data.head())

#data Cleaning

data1=pd.read_csv(r"C:\Training\AI_ML_Python_Training\Day03\insurance_v2.csv")

#combine the data

drop_row=data1.dropna()
print(drop_row.isna().sum())
print(drop_row.shape)

#working with new file

print(data1.shape)

# data1['age']=data1['age'].fillna(data1['age'].mean())
# print(data1)


str_data=[]
for i in data1['age']:
    if str(i).isnumeric():
        pass
    else:
        str_data.append(i)
print(str_data)

import numpy as np
data1['age']=data1['age'].replace("?",np.nan)
print(data1.isna().sum())

data1['age']=data1['age'].astype('float')
data1['age']=data1['age'].fillna(data1['age'].mean())
print(data1.isna().sum())

print(data1['region'].unique())

print(data1['region'].mode())
data1['region']=data1['region'].fillna(data1['region'].mode()[0])
print(data1)

#########################################################


#explanation on the merger_explanation.md file

info={"name":["jhon","abhi","Jessica","ankit"],
       "age":[23,34,45,23],
       "cc_score":[678,789,810,450],
       "id":[1,3,4,6]}
 
customer={
    "id":[1,3,0,8,9],
    "salary":[9078,8978.09,897687,8989,4524],
    "gender":["male","male","female","male","female"]
}
 
data1=pd.DataFrame(info)
data2=pd.DataFrame(customer)
 
print(data1)
print(data2)

print("\n::::::::::::::::\n") 
print(pd.merge(data1,data2, on='id',how='inner'))

print("\n::::::::::::::::\n")
print(pd.merge(data1,data2, on='id',how='outer'))

print("\n::::::::::::::::\n")
print(pd.merge(data1,data2, on='id',how='left'))
 
print("\n::::::::::::::::\n")
print(pd.merge(data1,data2, on='id',how='right'))