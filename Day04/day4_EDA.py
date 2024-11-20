#Explory Data Analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r"Day04\Bank_churn_modelling.csv")

print(data.shape)
print(data.info())
print(data.head().T)
 
#univariate Analysis
#Bi-Variate Analysis
 
 
data=data.drop_duplicates()
 
data=data.drop(["RowNumber","CustomerId",'Surname'],axis='columns')
print(data.shape)
print(data.head().T)
print(data.columns)
 
cate=['Geography', 'Gender', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'Exited']
con=['CreditScore',  'Age', 'Tenure', 'Balance', 'EstimatedSalary']
 
# for i in cate:
#     sns.countplot(x=data[i])
#     plt.show()

# for i in con:
#     print(data[i].describe())
#     sns.histplot(data[i])
#     plt.show()


# # bi-variate Analysis

# for i in con:
#     sns.histplot(data[data['Exited']==0][i],color='y')
#     sns.histplot(data[data['Exited']==1][i],color='r')

#     plt.show()


a=pd.crosstab(data['Geography'],data['Exited'],margins=True)
print(a)
 
print(a[1]/a['All'])
 
 
for i in cate:
    sns.barplot(x=data[i],y=data['Exited'])
    plt.show()