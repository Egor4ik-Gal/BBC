import pandas as pd
import numpy as np

# 1
d = pd.read_csv("tested.csv")
print(d.describe()) # базовые характеристики
print(d.isnull().sum()) # количесто 0
print(d.info()) # информация какого типа в каком столбце
print(f"{len(d)} - колличество строк, {len(d.columns)} - колличество столбцов")
# sred = d["Age"].sum() / len(d["Age"])
print(d["Age"].mean(), "- средний возраст")
d.fillna({"Age": d["Age"].mean()}, inplace=True)
print(d["Age"])
d = d.dropna(subset=["Embarked"]) # удаляю строки в которых не написано куда отправились гости (таких нет)

# 2

print(d["Survived"].mean() * 100) # % выживших
