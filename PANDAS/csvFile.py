import pandas as pd

films = pd.read_csv("imdb_1000.csv")

print(films.columns)
print(films[['title', 'star_rating']].head())
print()

print(films[
    (films['star_rating']>=8.5)
    &
    (films['star_rating']<=9)
    ][['title','star_rating']])

print()

print(films.query('star_rating>=9.0')[['title','star_rating']])
