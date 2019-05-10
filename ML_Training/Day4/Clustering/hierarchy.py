# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:34:40 2019

@author: chamakur
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv('C:\PSTL\Purdue_PSTL\ML_Training\Day4\Clustering\Customers_MAlls.csv')

X=dataset.iloc[:,[3,4]].values


# Using the dedgrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(X,method='ward'))
    
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()


# Fitting Hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
aggg=AgglomerativeClustering(n_clusters = 5, affinity='euclidean', linkage='ward')
y_hc=aggg.fit_predict(X)


# Visualising the cluster

plt.scatter(X[y_hc==0,0], X[y_hc==0,1], s=100, c='red', label='Cluster 1' )
plt.scatter(X[y_hc==1,0], X[y_hc==1,1], s=100, c='blue', label='Cluster 2' )
plt.scatter(X[y_hc==2,0], X[y_hc==2,1], s=100, c='green', label='Cluster 3' )
plt.scatter(X[y_hc==3,0], X[y_hc==3,1], s=100, c='cyan', label='Cluster 4' )
plt.scatter(X[y_hc==4,0], X[y_hc==4,1], s=100, c='magenta', label='Cluster 5' )


plt.title('cluster of customers')
plt.xlabel('Annuan income k$')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()




    





