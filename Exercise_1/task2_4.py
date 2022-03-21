# @author Antonis Marinidis
import csv

def genre_names(name):   
    file = open(dataset, 'r', encoding="utf8")
    # read the csv file
    movies = csv.DictReader(file)
    genres = []
    # split the genre column with the delimeter "|" and append it in the genres list
    for row in movies:
        for item in row["genres"].split("|"):
            genres.append(item)
    # make a new list that containes the unique genres
    genres_unique = list(set(genres))
    print("Unique genres : \n", genres_unique)
    
    # create a dictionary with the genres as keys and 0 as all the values
    genres_counts = {}
    for genre in genres_unique:
        genres_counts[genre] = 0
    # search in the genres list and count +1 the value of the genre-key in the dictionary    
    for item in genres:
        genres_counts[item] += 1
    print("\nMovies per genre : \n", genres_counts)
    
    # search in genres_counts for the genre with the most movies
    max_movies = -1
    max_genre = "" 
    for genre, count in genres_counts.items():
        if max_movies <= count:
            max_movies = count
            max_genre = genre
    print("\n", max_genre, max_movies)

    # sort the dictionary
    genre_list = sorted(genres_counts.items(), key=lambda x:x[1])
    # reverse the list to be in descending order
    genre_list.reverse()
    sorted_genres_count = dict(genre_list)
    print("\n", sorted_genres_count)
    
# main programm    
dataset = "Exercise_1/datasets/movies.csv"
genres = genre_names(dataset)

