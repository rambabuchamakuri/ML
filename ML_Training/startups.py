# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 14:27:53 2019

@author: chamakur

Linear Regression with LabelEndcoder, OneHotEncoder
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

startups=pd.read_csv("C:\PSTL\Purdue_PSTL\ML_Training\LinearRegression\Startups_Expense.csv")

print(startups.head())
#print(startups.info())
#print(startups.describe())

sns.pairplot(startups)

sns.distplot(startups['Profit'])

startups.head()

features=startups.iloc[:,:4].values
profit=startups['Profit'].values

#features
#profit


from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelencoder=LabelEncoder()
labelencoder=labelencoder.fit(features[:,3])
features[:,3]=labelencoder.transform(features[:,3])
features[:,3]

onehotencoder=OneHotEncoder(categorical_features=[3])
onehotencoder

features=onehotencoder.fit_transform(features).toarray()
features=features[:,1:]


from sklearn.model_selection import train_test_split
features_train, features_test, profit_train, profit_test = train_test_split(features, profit, test_size=0.2, random_state=101)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(features_train,profit_train)
print('Coefficients: \n', lm.coef_)

predictions=lm.predict(features_test)
plt.scatter(profit_test,predictions)

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(profit_test, predictions))
print('MSE:', metrics.mean_squared_error(profit_test, predictions))   #S r
print('RMSE:', np.sqrt(metrics.mean_squared_error(profit_test, predictions)))

from sklearn.metrics import r2_score
r2_score1=r2_score(profit_test,predictions)

r2_score1
