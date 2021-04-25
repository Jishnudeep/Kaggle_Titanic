# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 15:37:26 2021

@author: bjish
"""
#importing required libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

#Importing dataset
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

#EDA
#Shape of dataframe
print("Shape of Train Data:", train_data.shape)
print("Shape of Test Data:", test_data.shape)

#Checking Null values
print("Null values in Train Data:")
display(train_data.isnull().sum())
print("Null values in Test Data:")
display(test_data.isnull().sum())

#Cleaning Null Values
df_all = pd.concat([train_data, test_data], sort = True).reset_index(drop = True) 
#Combining both datasets to clean them together

#Cleaning Age
#Plotting Age

plt.hist(df_all['Age'])
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()

#Plotting Age on the basis of Passenger Class
plt.hist(df_all[df_all['Pclass'] == 1] ['Age'])
plt.title("Pclass = 1")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()

plt.hist(df_all[df_all['Pclass'] == 2] ['Age'])
plt.title("Pclass = 2")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()

plt.hist(df_all[df_all['Pclass'] == 3] ['Age'])
plt.title("Pclass = 3")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()

print("Median Age separated by Pclass:")
display(train_data.groupby('Pclass')['Age'].median())
