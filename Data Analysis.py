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
df_category = pd.DataFrame(X,columns = ['BusinessTravel','Department','EducationField','Gender','JobRole','MaritalStatus','Over18','OverTime'])
df_oh_p = pd.get_dummies(df_category)
    
df_people_new = pd.concat([df_category, df_oh_p], axis=1)

# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


