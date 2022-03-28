import pandas as pd

df = pd.read_csv("datasets/ratings_small.csv", low_memory=False)

dt1 = df.groupby("userId")
# Get all the movies that a user with id=1 has rate
movie_set = set(dt1.get_group(1)["movieId"])
print(movie_set)

user_list = []
for userId,group in dt1:
    if userId != 1:
        # Create a set of the movies that every user has vote
        user_set = set(group['movieId'])
        # Searching for common movies of every user with user = 1
        intersect = movie_set.intersection(user_set)
        if len(intersect) >= 3:
            user_list.append(userId)
    
print(user_list)    