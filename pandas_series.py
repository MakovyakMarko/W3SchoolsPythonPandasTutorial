# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:29:02 2023

@author: Marko
"""

import pandas as pd
# Series схожа на стовпець в таблиці
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

print(myvar[1])
# встановлюємо свої індекси
myvar = pd.Series(a, index = ["x","y","z"])
print(myvar)

print(myvar["y"])
# робота з словником
calories = {"day1":420, "day2":380, "day3":390}
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# DataFrames - це вся таблиця, а не ствпець як Series
data = {
    "calories":[420,380,390],
    "duration":[50,40,45]
}
myvar = pd.DataFrame(data)
print(myvar)