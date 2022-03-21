# @author Antonis Marinidis
from io import UnsupportedOperation
class Statistics:
    def __init__(self, name):
        self.name = name
    
    # function to calculate the mean rating
    def computeMeanRating(self):
        # handle errors
        try:
            with open(self.name) as d:
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