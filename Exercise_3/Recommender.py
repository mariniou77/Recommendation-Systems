import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import io

print("Loading the datasets, please wait ...")

movies_file = "dataset/movies.dat"
ratings_file = "dataset/ratings.dat"

# function to read files
def reader(filename):
    with open(filename, 'r') as file:
        file = file.read()
    return file

# function to detect error at user's input
def check_user_input(df):
    while True:
        try:
            user = int(input("Please enter user id : "))
            exist = user in set(df['UserId'])
            if exist:
                return user
                break
            else:
                print("User not found. Please try again : ")
                continue
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


df_sampled_ratings = df_ratings.sample(n=1000)

sampled_movies_users = df_sampled_ratings.pivot_table(index='UserId',
                                                      columns='MovieId',
                                                      values='Rating').fillna(0)


# getting the user from input
userId = check_user_input(df_sampled_ratings)
            


# make a dataframe only with the movies that given user has rated
df_input_user = df_ratings[df_ratings["UserId"] == userId]
# getting the avg rating of the given user
avg_user_rating = df_input_user['Rating'].mean()


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
sampled_movies_users = df_sampled_ratings.pivot_table(index='UserId',
                                                      columns='MovieId',
                                                      values='Rating').fillna(0)

mat_movies_users = csr_matrix(sampled_movies_users.values)

df_input_user1 = sampled_movies_users.iloc[userId-1]
df_input_user1 = df_input_user1.to_frame()
df_input_user1 = df_input_user1.transpose()


# print(df_ratings.loc[df_ratings['UserId'] == userId])
# reveal = pearson_calculation(movies_users)
# print(reveal)

# sam = KNN(10)
# sam.fit(mat_movies_users)


