import pandas as pd

films = pd.read_csv("imdb_1000.csv")
print(films.columns)

print(films.drop("content_rating", axis=1).head().columns)

print(films)
rowsToDrop = [0,1,2,4,6,8,9,10]
print(films.drop(rowsToDrop, axis=0))