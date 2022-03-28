import pandas as pd

data = [['Toy Story',21.946943],
        ['Jumanji',17.015539],
        ['Grumpier Old Men',11.7129]]

# Create a DataFrame object from the nested list with column headings ‘title’ and ‘popularity’
dtf = pd.DataFrame(data, columns=('title', 'popularity'))
print(dtf)
print("\n\n")

# Create a new DataFrame which has the entries sorted by popularity in ascending order
dtf1 = dtf.sort_values("popularity", ascending=True)
print(dtf1)
print("\n\n")

# Print the popularity values (with double [[]] shows also the column name)
print(dtf1[['popularity']])