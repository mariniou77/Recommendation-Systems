import pandas as pd
import numpy as np

# Read the file “ratings_small.csv” into a Pandas DataFrame
df = pd.read_csv("datasets/ratings_small.csv", low_memory=False)

results = []
dt1 = df.groupby("movieId")
for name,group in dt1:
    mean = np.mean(group['rating'])
    median = np.median(group['rating'])
    results.append({'id' : name,
                    'rating_mean' : mean,
                    'rating_median' : median})
print(results)


