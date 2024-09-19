#Q1. Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. 
month = 3 #Input for month
days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31) #List of number of days per month
num_days = days_per_month[month - 1] #Substracts 1 from the value of the month variable as array indices start from 0
print(num_days)

31
-----------------------------------------------------------------------------------------------------------------

# Q2. Given a list of total solar eclipse dates, select three earliest dates and three most recent dates using the slicing notation.
eclipse_dates = ['3 November 2013', '20 March 2015', '21 August 2017', '2 July 2019', '14 December 2020', '4 December 2021', '20 April 2023', '8 April 2024', '12 August 2026', '2 August 2027', '22 July 2028', '25 November 2030']
print(eclipse_dates [:3]) #Extract first 3 index starting from 0 and omit the 3rd index
print(eclipse_dates [-3:]) #Extract last 3 index 

['3 November 2013', '20 March 2015', '21 August 2017']
['2 August 2027', '22 July 2028', '25 November 2030']
-----------------------------------------------------------------------------------------------------------------

#Q3. For the following expression in sentence1, 
# Replace "." with "!"
# Replace "You" with "We"
# Replace "dream", "a", "new", "dream" with "have", "many", "big", "dreams"

sentence1 = ["You", "are", "never", "too", "old", "to", "set", "another", "goal", "or", "to", "dream", "a", "new", "dream", "."]
sentence1[15] = "!" #Replace full stop with exclamation mark
print(sentence1, "\n")
sentence1[0] = "We" #Replace you with we
print(sentence1, "\n")
sentence1[11:-1] = ["have", "many", "big", "dreams"] #Replacement will start from 12th index and end one element before the last element.
print(sentence1)

['You', 'are', 'never', 'too', 'old', 'to', 'set', 'another', 'goal', 'or', 'to', 'dream', 'a', 'new', 'dream', '!'] 

['We', 'are', 'never', 'too', 'old', 'to', 'set', 'another', 'goal', 'or', 'to', 'dream', 'a', 'new', 'dream', '!'] 

['We', 'are', 'never', 'too', 'old', 'to', 'set', 'another', 'goal', 'or', 'to', 'have', 'many', 'big', 'dreams', '!']
-----------------------------------------------------------------------------------------------------------------

#Q4. Given three lists of integers: a, b, and c, determine the maximum and minimum number of elements among these lists.
a = [4, 50, 95, 32, 65]
b = [47, 26, 85, 7, 89, 52, 115, 313, 186]
c = [66, 141, 283]

print("The maximum number would be: ", max([len(a), len(b), len(c)]))
print("The minimum number would be: ",min([len(a), len(b), len(c)]))

The maximum number would be:  9
The minimum number would be:  3
-----------------------------------------------------------------------------------------------------------------

#Q5. Given a list of integers, calculate the number of duplicate elements present in the list. Then add 88 to the set. Lastly remove a random elements from b. Consider using sets to efficiently remove duplicates. 
a = [24, 4, 4, 14, 41, 1, 20, 26, 34, 4, 26,]
b = set(a) #Convert list into set to contain unqiue elements
b.add(88) #Add element to set b
b.pop() #Removes random element from set b and 88 may or may not be removed since set is unordered so there is no last element
print("There are {} duplicates in the list.".format(len(a) - len(b)))
print(b)

There are 3 duplicates in the list.
{34, 4, 41, 14, 20, 24, 26, 88}
-----------------------------------------------------------------------------------------------------------------

#Q6. Given the list below, define a dictionary name population for the below data
# Key       |   Value    | Key      |   Value    | Key      |   Value
# City      |   Pop_2023 | City     |   Pop_2024 | City     |   Growth%
# Tokyo     |   37.19    | Tokyo    |   37.11    | Tokyo    |   -0.21    
# Delhi     |   32.94    | Delhi    |   32.80    | Delhi    |   2.63    
# Shanghai  |   29.20    | Shanghai |   29.86    | Shanghai |   2.25  
# Dhaka     |   23.21    | Dhaka    |   23.93    | Dhaka    |   3.13
# Sao Paulo |   22.61    | Sao Paulo|   22.80    | Sao Paulo|   0.83
# Cairo     |   22.18    | Cairo    |   22.62    | Cairo    |   1.99
# Mexico    |   22.28    | Mexico   |   22.50    | Mexico   |   1.00
# Beijing   |   21.76    | Beijing  |   22.18    | Beijing  |   1.94
# Mumbai    |   21.29    | Mumbai   |   21.67    | Mumbai   |   1.77
# Osaka     |   19.01    | Osaka    |   18.96    | Osaka    |   -0.24

population = {'Tokyo': {'Pop_2023': 37.19, 'Pop_2024': 37.11, 'Growth': -0.21}, 
              'Delhi': {'Pop_2023': 32.94, 'Pop_2024': 32.80,'Growth': 2.63},
              'Shanghai': {'Pop_2023': 29.20, 'Pop_2024': 29.86,'Growth': 2.25},
              'Dhaka': {'Pop_2023': 23.21, 'Pop_2024': 23.93,'Growth': 3.13},
              'Sao Paulo': {'Pop_2023': 22.61, 'Pop_2024': 22.80,'Growth': 0.83},
              'Cairo': {'Pop_2023': 22.18, 'Pop_2024': 22.62,'Growth': 1.99},
              'Mexico': {'Pop_2023': 22.28, 'Pop_2024': 22.50,'Growth': 1.00},
              'Beijing': {'Pop_2023': 21.76, 'Pop_2024': 22.18,'Growth': 1.94},
              'Mumbai': {'Pop_2023': 21.29, 'Pop_2024': 21.67,'Growth': 1.77},
              'Osaka': {'Pop_2023': 19.01, 'Pop_2024': 18.96,'Growth': -0.24},
             }
for city, data in population.items(): #Iterates through each city and its data in the population dictionary
    if data['Growth'] < 0: #Checks if growth rate for the current city is negative
        print(f"{city} has a decreasing growth rate")
    else: #if growth rate is not negative, it means the population is increasing
        print(f"{city} has an increasing growth rate")

Tokyo has a decreasing growth rate
Delhi has an increasing growth rate
Shanghai has an increasing growth rate
Dhaka has an increasing growth rate
Sao Paulo has an increasing growth rate
Cairo has an increasing growth rate
Mexico has an increasing growth rate
Beijing has an increasing growth rate
Mumbai has an increasing growth rate
Osaka has a decreasing growth rate


