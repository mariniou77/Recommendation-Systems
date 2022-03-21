# @author Antonis Marinidis
from io import UnsupportedOperation

# function to calculate the mean rating
def computeMean_Median_ModeRating(name):
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
    mean = sum(dt_list)/len(dt_list)  

    # calculate the median value of the ratings
    # devide the list in 2 parts and store it as an integer (//)
    index = len(dt_list) // 2
    # check if the length of the list is odd or even
    # odd :
    if len(dt_list) % 2:
        median = sorted(dt_list)[index]
    # even :    
    else:
        # find the sum of the 2 numbers in the middle of the sorted list and devide them by 2
        median = sum(sorted(dt_list)[index -1:index + 1]) / 2    
    # calculate the mode of the ratings
    # this will return the element that occurs the maximum times in the given list
    mode = (max(set(dt_list), key = dt_list.count))

    return mean, median, mode      

# main programm that calls the function with the name of the file 
dataset = "Exercise_1/datasets/ratings.csv"    
avg, med, mod = computeMean_Median_ModeRating(dataset)  
print("This is the average rating of the movies : " + str(avg)) 
print("This is the median rating of the movies : " + str(med)) 
print("This is the mode rating of the movies : " + str(mod))