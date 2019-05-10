# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:06:49 2019

@author: chamakur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#%matplotlib inline

dataset=pd.read_csv("C:\PSTL\Purdue_PSTL\ML_Training\Polynomial Regression\Position_Salaries.csv")
dataset
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values


from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)


from sklearn.linear_model import LinearRegression
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
lin_reg2

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
             
             