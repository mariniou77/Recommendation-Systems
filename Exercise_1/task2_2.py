from io import UnsupportedOperation

# function to calculate the mean rating
def computeMeanRating(name):
    # handle errors
    try:
        with open(name) as d:
            lines = d.readlines()
    # throw error message if file does not exist        
    except FileNotFoundError:
        print("The file not found")
        exit(1) 
    # throw error message if file is not readable               
    except UnsupportedOperation:
        print("The file is not readable")

    dt_list = []
    # extract the 3rd column which is the rating and store it in the list after converting it to float
    for rate in lines:
        rating = rate.split(",")
        if rating[2] != "rating":
            dt_list.append(float(rating[2]))

    # calculating the average value of the ratings
    return sum(dt_list)/len(dt_list)     

# pain programm that calls the function with the name of the file 
dataset = "Exercise_1/datasets/ratings.csv"    
avg = computeMeanRating(dataset)  
print("This is the average rating of the movies : " + str(avg))  
