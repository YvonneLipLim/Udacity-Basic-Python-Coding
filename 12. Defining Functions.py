"""
A function is a block of code that performs a specific task. Functions are reusable, making code more efficient, readable, and maintainable.
The basic syntax will be:
def function_name(parameters):
    # function body
    pass

An example will be:
def greet(name):
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!
"""


#Q1. Create a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values.

def population_density(population,land_area):
    return population/land_area #Calculate population density

#Test cases for the function
test1 = population_density(10, 1) #Population is 10 and the land area is 1
expected_result1 = 10 #10 people per square unit
print("Expected result: {}, Actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4) #Population is 864,816 and the land area is 121.4 square units
expected_result2 = 7123.6902801 #Expected population density is calculated and stored in expected_result2
print("Expected result: {}, Actual result: {}".format(expected_result2, test2))

#Output:
Expected result: 10, Actual result: 10.0
Expected result: 7123.6902801, Actual result: 7123.690280065897
----------------------------------------------------------------------------------------------------------------------------------


'''
Q2. 
Create a function named readable_timedelta that should take one argument, an integer days, and return a string that says how many weeks and days. 
For example, calling the function and printing the result like this: 1 week(s) and 3 day(s).
'''

def readable_timedelta(days): #Represents the total number of days to be converted
    weeks = days // 7 #Calculate number of whole weeks by dividing total days by 7 and rounding down to the nearest integer using integer division (//)
    remainder = days % 7 #Calculates remaining days after subtracting number of weeks from the total days using the modulo operator (%)
    return "{} week(s) and {} days(s).".format(weeks,remainder) #Return a formatted string that combines the calculated number of weeks and remaining days  
print(readable_timedelta(20)) #Calculate total days is equivalent to number of weeks and days

#Output:
2 week(s) and 6 days(s).
----------------------------------------------------------------------------------------------------------------------------------
