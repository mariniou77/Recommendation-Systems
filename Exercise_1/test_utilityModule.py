from utilityModule import Statistics

dataset = Statistics("Exercise_1/datasets/ratings.csv")    
avg = dataset.computeMeanRating() 
print("This is the average rating of the movies : " + str(avg)) 