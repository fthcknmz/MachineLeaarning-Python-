import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataframe = pd.read_csv(".\ML-LinearRegression\hw_25000.csv")
print(dataframe.columns)

height = dataframe.Height.values.reshape(-1,1)
weight = dataframe.Weight.values.reshape(-1,1)

regression = LinearRegression()
regression.fit(height, weight)

h_value = 71
print(regression.predict(([[h_value]])))


plt.scatter(dataframe.Height, dataframe.Weight)
x_values = np.arange(min(dataframe.Height), max(dataframe.Height)).reshape(-1,1)
plt.plot(x_values, regression.predict(x_values), color="red")
plt.title("DATA FRAME and LINEAR REGRESSION MODEL")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

print(r2_score(weight, regression.predict(height))) # 25% true