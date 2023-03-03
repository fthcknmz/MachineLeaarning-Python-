import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataframe = pd.read_csv(".\ML-LinearRegression\insurance.csv")
print(dataframe.columns)
print(dataframe.describe())

expenses = dataframe.expenses.values.reshape(-1,1)

age_children = dataframe.iloc[:, [0,3]].values

regression = LinearRegression()
regression.fit(age_children, expenses)

value = np.array([[40, 0]])
print(regression.predict(value))