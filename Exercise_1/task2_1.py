# @author Antonis Marinidis
dt_list = []

# opening and reading the file withe the ratings
dataset = "Exercise_1/datasets/ratings.csv"
with open(dataset) as d:
    lines = d.readlines()

# extract the 3rd column which is the rating and store it in the list after converting it to float
for rate in lines:
    rating = rate.split(",")
    if rating[2] != "rating":
        dt_list.append(float(rating[2]))

# calculating the average value of the ratings
avg = sum(dt_list)/len(dt_list)        
print("This is the average rating of the movies : " + str(avg))