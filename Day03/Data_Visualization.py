import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

data=pd.read_csv(r"C:\Training\AI_ML_Python_Training\Day02\insurance.csv")

# Seaborn Matplotlib Bokeh, poltly dash
print(data.head())

plt.hist(data['age'],color='g')
plt.xlabel("age")
plt.ylabel("fequency")
plt.title(" Distribution of Age")
plt.grid()
plt.show()
 

sns.histplot(data['age'],color='b',binwidth=5)
plt.show()

sns.histplot(data['charges'],color='y')
plt.show()

sns.countplot(x=data['smoker'])
plt.show()

sns.countplot(x=data['region'])
plt.show()

sns.scatterplot(x=data['age'],y=data['charges'],color='r')
plt.show()

sns.scatterplot(x=data['bmi'],y=data['charges'],color='r')
plt.show()

sns.histplot(data[data['smoker']=='yes']['charges'],color='r')
sns.histplot(data[data['smoker']=='no']['charges'],color='y')
plt.show()

sns.histplot(data[data['sex']=='male']['charges'],color='r')
sns.histplot(data[data['sex']=='female']['charges'],color='y')
plt.show()


sns.scatterplot(x=data['age'],y=data['charges'],hue=data['smoker'],color='r')
plt.show()


sns.scatterplot(x=data['bmi'],y=data['charges'],hue=data['smoker'],color='r')
plt.show()