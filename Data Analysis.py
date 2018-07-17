# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 09:52:27 2018

@author: ibm
"""
# Importing the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the dataset
dataset = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
pd.set_option('display.max_columns',40)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Visualizing the dataset at hand
dataset.head()
dataset.describe()

#Deleting columns which have no relevance in dataset (noise)
#del dataset.EmployeeNumber

#Check whether dataset has null values
dataset.isnull().values.any()

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_cat = LabelEncoder()

categories[:,0] = labelencoder_cat.fit_transform(categories[:,0])
onehotencoder = OneHotEncoder(categorical_features = 0)

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


