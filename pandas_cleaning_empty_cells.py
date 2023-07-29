# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 09:23:20 2023

@author: Marko
"""

import pandas as pd

df = pd.read_csv('training_data.csv')

# видалити пусті рядки 
new_df = df.dropna()

print("After drop:",new_df.to_string())

#df.dropna(inplace = True)

#print(df.to_string)

# змаінити пусті рядки на значення. Замінити значення NULL на число 130
df.fillna(130,inplace=True)
print("After fill:",df.to_string)


# замінити значення NULL у стовпцях "Калорії" на число 130
df['Calories'].fillna(130,inplace=True)

# поширреним способом заміни порожніх клітинок є обчислення
# середнього, медіани або модового значення стовпця
# Обчислимо середнє значення та замінимо ним будь-які порожні значення:
# Середнє = сума усіх значень, поділена на кількість значень
x = df['Calories'].mean()
df['Calories'].fillna(x, inplace=True)
# Обчислимо MEDIAN і замінимо ним будь-які значення
# MEDIAN = значення посередині після того, як ви відсортували всі значення за зростанням:
x = df['Calories'].median()
df['Calories'].fillna(x, inplace=True)
# Обчисломо модове значення і заміним ним будь-які порожні значення 
# Модове значення = значення, яке з'являється найчастіше
x = df['Calories'].mode()
df['Calories'].fillna(x, inplace=True)
print(df.to_string)