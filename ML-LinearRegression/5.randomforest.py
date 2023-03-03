import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

dataframe = pd.read_csv(".\ML-LinearRegression\positions.csv")

level = dataframe.iloc[:,1].values.reshape(-1,1)
salary = dataframe.iloc[:,2].values

regression = RandomForestRegressor(n_estimators=50, random_state=0)
regression.fit(level, salary)

x_values = np.arange(min(level), max(level), 0.01).reshape(-1,1)
plt.scatter(level, salary, color="red")
plt.plot(x_values, regression.predict(x_values), color="blue")
plt.title("DATA FRAME AND RANDOM FOREST MODEL")
plt.xlabel("LEVEL")
plt.ylabel("SALARY")

plt.text(1, 450000, r2_score(salary, regression.predict(level)), fontsize=10)
plt.show()