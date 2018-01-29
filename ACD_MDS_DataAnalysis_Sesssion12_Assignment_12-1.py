# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt

# read in Titanic dataset
url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url)

# Scatter plot - Age vs Fare (plot color by sex/gender)
# X axis - Age, Y axis - Fare
x = titanic["age"]
y = titanic["fare"]
s = titanic["sex"]
titanic["sex_num"] = s
replace_nums = {"sex_num": {"male": 1, "female": 0}}
titanic.replace(replace_nums, inplace=True)
sn = titanic["sex_num"]   
z = 128 + 64 * sn
plt.scatter(x,y,c=z,marker='.')
plt.show()

# Pie chart, showing Male/Female proportion:
s = titanic["sex"].value_counts()
sizes = [s[0], s[1]]
labels = 'Male', 'Female'
fig1, ax1 = plt.subplots()
ax1.pie(sizes,  labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
