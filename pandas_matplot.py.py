
import pandas as pd
list1=[21,18,5,3,4]
var1=pd.Series(list1)
print(var1)

"""
## giving custom indexes"""

var1=pd.Series(list1,index=['a','b','x','y','z'])
print(var1)

"""## series for dictionary"""

dist1={'1':'abc','2':'dfg'}
var1=pd.Series(dist1)
print(var1)

"""## creating a DataFrame and printing value of index 0"""

data={
    'sapid':[157,159,161,None],
    'name':['abc','dfg','xyz',None]
}
df=pd.DataFrame(data)
df.loc[0]

"""# Finding the Index of Rows in a DataFrame Where the 'name' Column is 'abc"""

row=df.loc[df['name']=='xyz'].index
row

df

"""# Use of head ,tail, info, finding null values in Dataframe"""

df.head(2)
df.tail(1)
df.info()
df.isna().sum()
df.dropna()

"""# filling Null Values with mean"""

data={
    'sapid':[156,159,160,None],
    'name':['abcd','efgh','xyzq','erff']
}
df=pd.DataFrame(data)

df.fillna(df.mean())

"""# filling Null Values with median"""

data={
    'sapid':[156,159,160,None],
    'name':['abcd','efgh','xyzq','erff']
}
df=pd.DataFrame(data)

df.fillna(df.median())

"""# Use of describe method"""

df.describe()

"""# Plotting a graph"""

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['P1','P2','P3','P4','P5'])
y=np.array([19,14,12,18,17])
plt.scatter(x,y)
plt.show()

"""plotting pie chart"""

x = np.array(['P1', 'P2', 'P3', 'P4', 'P5'])
y = np.array([20, 15, 37, 18, 10])

plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title('Distribution of Values')
plt.show()

"""plotting bar graph"""

x = np.array(['P1', 'P2', 'P3', 'P4', 'P5'])
y = np.array([19, 14, 12, 18, 17])

plt.bar(x, y)
plt.xlabel('Products')
plt.ylabel('Values')
plt.title('Bar Graph of Values for Each Product')
plt.show()

"""Plotting a histogram"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
data = np.random.randn(1000)

plt.hist(data, bins=20, color='skyblue', edgecolor='black')

plt.xlabel('Random Values')
plt.ylabel('Frequency')
plt.title('Histogram of Random Values')

plt.show()

x=np.random.normal(100,10,200)
plt.hist(x)
plt.show()