import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

dataframe = pd.read_csv(".\ML-LinearRegression\positions.csv")
print(dataframe.columns)

salary = dataframe.iloc[:,2].values.reshape(-1,1)
level = dataframe.iloc[:,1].values.reshape(-1,1)

# LINEAR MODEL

regression = LinearRegression()
regression.fit(level, salary)

plt.scatter(level, salary, color="red")
plt.plot(level, regression.predict(level), color="blue")
plt.title("DATA FRAME AND LINEAR MODEL")
plt.xlabel("LEVEL")
plt.ylabel("SALARY")

plt.text(1, 450000, r2_score(salary, regression.predict(level)), fontsize=10)
plt.show()


# POLYNOMIAL MODEL

regressionPoly = PolynomialFeatures(degree = 4)
levelPoly = regressionPoly.fit_transform(level)

regression2 = LinearRegression()
regression2.fit(levelPoly, salary)

plt.scatter(level, salary, color="red")
plt.plot(level, regression2.predict(levelPoly), color="blue")
plt.title("DATA FRAME AND POLYNOMIAL MODEL")
plt.xlabel("LEVEL")
plt.ylabel("SALARY")

plt.text(1, 450000, r2_score(salary, regression2.predict(levelPoly)), fontsize=10)
plt.show()

