# -*- coding: utf-8 -*-
"""11 | House price prediction using Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ry0raEyThl-qJH51v5V4yfoyfkb-_8A-

# **Day-11 | House price prediction using Linear Regression-SingleVariable**

### *Import Libraries*
"""

import pandas as pd
from sklearn.linear_model import LinearRegression 
import matplotlib.pyplot as plt

"""### *Load Dataset from Local Directory*"""

from google.colab import files
uploaded = files.upload()

"""### *Load Dataset*"""

dataset = pd.read_csv('dataset.csv')

"""### *Load Summarize*"""

print(dataset.shape)
print(dataset.head(5))

"""### *Visualize Dataset*"""

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(dataset.area,dataset.price,color='red',marker='*')

"""### *Segregate Dataset into Input X & Output Y*"""

X = dataset.drop('price',axis='columns')
X

Y = dataset.price
Y

"""### *Training Dataset using Linear Regression*"""

model = LinearRegression()
model.fit(X,Y)

"""### *Predicted Price for Land sq.Feet of custom values*"""

x=40000
LandAreainSqFt=[[x]]
PredictedmodelResult = model.predict(LandAreainSqFt)
print(PredictedmodelResult)

"""### Let's check is our model is Right ?
### Theory Calculation
### Y = m * X + b (m is coefficient and b is intercept)

*Coefficient - m*
"""

m=model.coef_
print(m)

"""*Intercept - b*"""

b=model.intercept_
print(b)

"""### Y=mx+b
*x is Independant variable - Input - area*
"""

y = m*x + b
print("The Price of {0} Square feet Land is: {1}".format(x,y[0]))