import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import io

movies_file = "dataset/movies.dat"
ratings_file = "dataset/ratings.dat"

# function to read files
def reader(filename):
    with open(filename, 'r') as file:
        file = file.read()
    return file

# function to detect error at user's input
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

# Create the movies dataframe
movies_colnames = ["MovieId",
                   "Title",
                   "Genre"]
data = io.StringIO(movies)
df_movies = pd.read_csv(data,
                        sep="::",
                        names=movies_colnames)

# Create the ratings dataframe
ratings_colnames = ["UserId",
                    "MovieId",
                    "Rating",
                    "Timestamp"]
data = io.StringIO(ratings)
df_ratings = pd.read_csv(data,
                         sep="::",
                         names=ratings_colnames)
df_ratings = df_ratings.drop("Timestamp",
                             axis=1)
# getting the user from input
userId = check_user_input()
# make a dataframe only with the movies taht given user has rated
df_input_user = df_ratings[df_ratings["UserId"] == userId]


# gatting the titles of these movies
df_movies_user_merged = pd.merge(df_input_user,
                                 df_movies,
                                 on="MovieId")
# print 15 random titles of movies that given user has rated
df_15_movies_user = df_movies_user_merged[["Title",
                                           "Genre"]].sample(n=15)
print(df_15_movies_user)

df_input_user = df_input_user.pivot(index='UserId',
                                    columns='MovieId',
                                    values='Rating')

# prepare a dataframe - matrix for the knn
movies_users = df_ratings.pivot_table(index='UserId',
                                      columns='MovieId',
                                      values='Rating')

mat_movies_users = csr_matrix(movies_users.values)

df_input_user1 = movies_users.iloc[userId-1]
df_input_user1 = df_input_user1.to_frame()
df_input_user1 = df_input_user1.transpose()