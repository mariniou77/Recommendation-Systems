import pandas as pd

# Read the CSV file “movies_metadata” into a Pandas DataFrame
dtf = pd.read_csv("datasets/movies_metadata.csv")
print(dtf)

# Use the type function to inspect the DataFrame
print(type(dtf))

# Print the information about the first and the last movie in the dataset
first = dtf.iloc[0]
last = dtf.iloc[-1]
print("First movie :\n-----------------------\n", first,"\n\nLast movie :\n-----------------------\n", last)

# Show the information about the movie “Jumanji”
movie = dtf.loc[dtf['title'] == 'Jumanji']
# Converting dataframe to serie
movieSer = movie.squeeze()
print("\n\nJumanji movie :\n-----------------------\n",movieSer)