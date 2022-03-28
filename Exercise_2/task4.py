import pandas as pd
import numpy as np

# Read the file “ratings_small.csv” into a Pandas DataFrame
df = pd.read_csv("datasets/ratings_small.csv", low_memory=False)

results = []
df1 = df.groupby("movieId")
for movieId,group in df1:
    mean = np.mean(group['rating'])
    median = np.median(group['rating'])
    results.append({'id' : movieId,
                    'rating_mean' : mean,
                    'rating_median' : median})
print(results)


