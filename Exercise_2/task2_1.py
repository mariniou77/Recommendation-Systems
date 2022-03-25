import pandas as pd

data = ['Toy Story','Jumanji','Grumpier Old Men'] 
# Create a Pandas Series from the list
ser = pd.Series(data)
# Print the first element
print(ser[:1])
# Print the first two elements
print(ser[:2])
# Print the last two elements
print(ser[1:3])

# Create a new series from the list with defined indexes: [‘a’, ’b’, ’c’]
indexes = ["a", "b", "c"]
ser1 = pd.Series(data, indexes)
print(ser1)
# Print the element at index position ‘b’ (with double [[]] you print also the index, with single [] you print just the value)
print(ser1[["b"]])