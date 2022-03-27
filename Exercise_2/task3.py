import pandas as pd
import numpy as np

# Read the CSV file “movies_metadata” into a Pandas DataFrame
dtf = pd.read_csv("datasets/movies_metadata.csv", low_memory=False)
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

''' 
Create a smaller DataFrame called small_df from the given one by considering only the 
following columns: 'title', 'release_date', 'popularity', 'revenue',
'runtime' and 'genres' 
'''
smaller_dtf = dtf[['title', 'release_date', 'popularity', 'revenue', 'runtime','genres']]

# Create a function “to_float” to convert the type of its input to float
def to_float(x):
    try:
        x = float(x)
    except:
        x = np.nan
    return x 
   
smaller_dtf = dtf[['title', 'release_date', 'popularity', 'revenue', 'runtime', 'genres']].copy()
smaller_dtf.loc['release_date'] = pd.to_datetime(smaller_dtf['release_date'], errors='coerce')
smaller_dtf['release_year'] = smaller_dtf['release_date'].apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
smaller_dtf['release_year'] = smaller_dtf['release_year'].apply(to_float)
smaller_dtf['release_year'] = smaller_dtf['release_year'].astype('float')
smaller_dtf = smaller_dtf.drop(columns="release_date") 

# print the titles of all movies that were released after the year 2010
movies_after_2010 = smaller_dtf[(smaller_dtf['release_year']) > 2010]
print("\n\nMovies after 2010 :\n-----------------------\n", movies_after_2010['title'].to_string(index=False))