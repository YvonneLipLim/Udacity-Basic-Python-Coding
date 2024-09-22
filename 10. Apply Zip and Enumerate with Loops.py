'''
Q1.
Create a for loop specifying the label and coordinates of each point using zip. Then appends it to the list.
Each string should be formatted as label: x, y, z. Example: F: 23,677, 4
'''

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

point = []

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord): #Iterate over the elements of the four lists using zip function
    point.append(f"{label}: {x}, {y}, {z}") #Formatted string created using f-strings to concatenates the label, x, y, and z values and appended to point list
    print(point)

['F: 23, 677, 4']
['F: 23, 677, 4', 'J: 53, 233, 16']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6', 'W: 14, 432, 23']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6', 'W: 14, 432, 23', 'X: -5, 445, -1']
-------------------------------------------------------------------------------------------------------------------------------------------------


#Q2. Create a dictionary cast that uses names as keys and heights as values with zip.
best_movies = ["Oppenheimer", "Past Lives", "Poor Things", "The Holdovers", "Killers of the Flower Moon"]
movie_ratings = [8.3, 7.8, 7.8, 7.9, 7.6]

movies = dict(zip(best_movies, movie_ratings)) #Pair the elements of the two lists with zip function and create a list of tuples where each tuple contains name of movies and ratings. Dict() function is then used to convert tuples into dictionary
print(movies)

{'Oppenheimer': 8.3, 'Past Lives': 7.8, 'Poor Things': 7.8, 'The Holdovers': 7.9, 'Killers of the Flower Moon': 7.6}
-------------------------------------------------------------------------------------------------------------------------------------------------


#Q3. Unzip the movies tuple into show and ratings

movies = (("Oppenheimer", 8.3), ("Past Lives", 7.8), ("Poor Things", 7.8), ("The Holdovers", 7.9), ("Killers of the Flower Moon", 7.6))
show, ratings = zip(*movies) #Unpacks this tuple of lists into two variables: show and ratings
print(show)
print(ratings)

('Oppenheimer', 'Past Lives', 'Poor Things', 'The Holdovers', 'Killers of the Flower Moon')
(8.3, 7.8, 7.8, 7.9, 7.6)
-------------------------------------------------------------------------------------------------------------------------------------------------


#Q4. Transpose from a 4-by-3 matrix to a 3-by-4 matrix using zip.
num = ((6, 14, 22), (22, 31, 34), (47, 72, 77), (83, 95, 99))
num_transpose = tuple(zip(*num))
print(num_transpose)

((6, 22, 47, 83), (14, 31, 72, 95), (22, 34, 77, 99))
-------------------------------------------------------------------------------------------------------------------------------------------------


#Q5. Modify the movies list so that each element contains the show followed by the ratings using enumerate.

#Method 1
movies = ["Oppenheimer", "Past Lives", "Poor Things", "The Holdovers", "Killers of the Flower Moon"]
ratings = [8.3, 7.8, 7.8, 7.9, 7.6]

for i, show in enumerate(movies): #Iterates over the elements of the movies list, but also provides an index for each element stored in i
    movies[i] = show + " " + str(ratings[i]) #Converts the rating to a string as the + operator requires both operands to be strings
print(movies)

['Oppenheimer 8.3', 'Past Lives 7.8', 'Poor Things 7.8', 'The Holdovers 7.9', 'Killers of the Flower Moon 7.6']
-------------------------------------------------------------------------------------------------------------------------------------------------

#Method 2
movies = ["Oppenheimer", "Past Lives", "Poor Things", "The Holdovers", "Killers of the Flower Moon"]
ratings = [8.3, 7.8, 7.8, 7.9, 7.6]

movies = [f"{show} {ratings[i]}" for i, show in enumerate(movies)] #Combines the current element show from the movies list with ratings[i] from ratings, separate by space. Enumerate(movies) part iterates over the elements of the movies list, but also provides an index for each element stored in i
print(movies)

['Oppenheimer 8.3', 'Past Lives 7.8', 'Poor Things 7.8', 'The Holdovers 7.9', 'Killers of the Flower Moon 7.6']
-------------------------------------------------------------------------------------------------------------------------------------------------
