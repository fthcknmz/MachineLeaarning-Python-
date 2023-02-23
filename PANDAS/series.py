import pandas as pd
import numpy as np


data = np.array(["Fethi", "Mehmet", "Ali"])
series = pd.Series(data, index=[1,2,3])

print(series)
print()

data2 = {"math":10, "physics":20, "algebra": 100}
series2 = pd.Series(data2)
print(series2)
print()

series3 = pd.Series(5)
print(series3)