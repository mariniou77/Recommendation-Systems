import pandas as pd
import numpy as np
import io

movies_file = "dataset/movies.dat"
ratings_file = "dataset/ratings.dat"
users_file = "dataset/users.dat"

# function to read files
def reader(filename):
    with open(filename, 'r') as file:
        file = file.read()
    return file

def check_user_input():
    while True:
        try:
            user = int(input("Please enter user id : "))
            return user
            break
        except ValueError:
            print("Invalid input !! ")  
            continue

movies = reader(movies_file)
ratings = reader(ratings_file)
users = reader(users_file)

# Create the movies dataframe
movies_colnames = ["MovieId", "Name", "Genre"]
data = io.StringIO(movies)
df_movies = pd.read_csv(data, sep="::", names=movies_colnames)

# Create the ratings dataframe
ratings_colnames = ["UserId", "MovieId", "Rating", "Timestamp"]
data = io.StringIO(ratings)
df_ratings = pd.read_csv(data, sep="::", names=ratings_colnames)

# Create the users dataframe
users_colnames = ["UserId", "Gender", "Age", "Occupation", "Zip-code"]
data = io.StringIO(users)
df_users = pd.read_csv(data, sep="::", names=users_colnames)


userId = check_user_input()

df_spec_user = df_users[df_users["UserId"] == userId]
df_uses_spec_user_merged = pd.merge(df_ratings, df_spec_user, on = "UserId")
df_movies_user_merged = pd.merge(df_uses_spec_user_merged, df_movies, on = "MovieId")

df_movies_15 = df_movies_user_merged[["Name", "Genre"]].sample(n=15)
print(df_movies_15)


    
