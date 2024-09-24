'''
Lambda expressions, also known as lambda functions or anonymous functions, are a concise way to create functions without declaring them with the def keyword:
1. Not declared with a name
2. Contain only a single expression
3. Cannot include statements (e.g., if, for, while) or multiple expressions

The general syntax of a lambda expression is: lambda arguments: expression
Example:
sum = lambda x, y: x + y
print(sum(3, 4))  # Outputs: 7

Use cases:
1. Often used as event handlers or callback functions
2. Can be used with functions like filter(), map(), and reduce() to process data
3. Can be used as a key function for sorting.

Advantages:
1. Reduce code length
2. Improve readability by encapsulating simple operations
3. Can be defined anywhere
'''


#Q1. The below code uses map() to find the mean of each list in numbers to create the list averages. 
#    Rewrite the code to be more concise by replacing the mean function with lambda expression defined with the call to map().

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list): #Defines a function mean() that calculates the average of a list of numbers
    return sum(num_list) / len(num_list) #Calculates average by summing all numbers using sum() and dividing by the count using len()
averages = list(map(mean, numbers)) #Apply mean() to each sublist in numbers using map() and stores results in averages list.

print(averages)

#Output:
[57.0, 58.2, 50.6, 27.2]
----------------------------------------------------------------------------------------------------------------------------

#Rewrite with Lambda Expression Method 1
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers)) #Apply lambda function (calculating average) to each element in the list numbers using map(), and stores results in averages list
print(averages)

#Output:
[57.0, 58.2, 50.6, 27.2]
----------------------------------------------------------------------------------------------------------------------------

#Rewrite with Lambda Expression Method 2
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# Anonymous function (lambda) that calculates the average of input list num_list.
# It sums all numbers using sum() and divides by the number of elements (length) using len().
divide = lambda num_list: sum(num_list) / len(num_list) 
averages = list(map(divide, numbers)) #Apply divide function to each element in numbers using map() and store results in averages list

print(averages)

#Output:
[57.0, 58.2, 50.6, 27.2]
----------------------------------------------------------------------------------------------------------------------------


#Q2. Below code uses filter() to get the names in cities that are fewer than 10 characters long to create the list short_cities. 
#    Rewrite this code to be more concise by replacing the is_short function with a lambda expression defined within the call to filter().

cities = ["New York City", "Orlando", "Las Vegas", "San Francisco", "New Orleans", "Miami", "Chicago", "Washington", "Boston", "Honolulu"]
def is_short(name): #Defines a function named is_short that takes one argument, name
    return len(name) < 10 #Check the length of the name string and returns true if length is less than 10 otherwise false
short_cities = list(filter(is_short, cities)) #Filters cities list to include only city names that are shorter than 10 characters 
print(short_cities)

#Output:
['Orlando', 'Las Vegas', 'Miami', 'Chicago', 'Boston', 'Honolulu']
----------------------------------------------------------------------------------------------------------------------------

#Rewrite with Lambda Expression Method 1
cities = ["New York City", "Orlando", "Las Vegas", "San Francisco", "New Orleans", "Miami", "Chicago", "Washington", "Boston", "Honolulu"]
short_cities = list(filter(lambda x: len(x) < 10, cities)) #Filter cities list using lambda function, selecting cities with fewer than 10 characters
print(short_cities)

#Output:
['Orlando', 'Las Vegas', 'Miami', 'Chicago', 'Boston', 'Honolulu']


#Rewrite with Lambda Expression Method 2
cities = ["New York City", "Orlando", "Las Vegas", "San Francisco", "New Orleans", "Miami", "Chicago", "Washington", "Boston", "Honolulu"]
is_short = lambda name: len(name) < 10 #Lambda function is_short checks if name length is under 10 characters
short_cities = list(filter(is_short, cities)) #Filters cities list to include only city names that are shorter than 10 characters 
print(short_cities)

#Output:
['Orlando', 'Las Vegas', 'Miami', 'Chicago', 'Boston', 'Honolulu']
