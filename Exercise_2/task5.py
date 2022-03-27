import pandas as pd
import numpy as np

df = pd.read_csv("datasets/ratings_small.csv", low_memory=False)

dt1 = df.groupby("userId")
movie_set = set(dt1.get_group(1)["movieId"])
print(movie_set)

user_list = []
for name,group in dt1:
    if name != 1:
        user_set = set(group['movieId'])
        intersect = movie_set.intersection(user_set)
        if len(intersect) >= 3:
            user_list.append(name)
    
print(user_list)    