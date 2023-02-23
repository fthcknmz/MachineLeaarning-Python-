import pandas as pd
import numpy as np

data = [10,20,30,40,50]
df = pd.DataFrame(data)
print(df)
print()

data2 = [["Fethi", 23, "Istanbul"],["Mehmet", 23, "Trabzon"],["Ali", 21, "Ankara"]]
df2 = pd.DataFrame(data2, columns=["name","age","city"], index=[1,2,3])
print(df2)
print()

data3 = {"name": ["Fethi","Derin","Ayse"],
        "age": [23,19,22],
        "city": ["Ankara", "Izmit", "ızmir"]}
df3 = pd.DataFrame(data3, columns=["name","age","city"], index=[1,2,3])
print(df3)
print()

df2.pop("city")
print(df2)
print()

print(df3.loc[2])
print()

print(df3.iloc[1]) 

