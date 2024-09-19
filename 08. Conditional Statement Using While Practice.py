#Q1. Find the factorial of a number using a while loop.

number = 7 #Stores the number for which we want to calculate the factorial.
product = 1 #Store the calculated factorial and it's initialized to 1 because the factorial of 0 is 1
current = 1 #Keeps track of the current number being multiplied in the factorial calculation that starts at 1

while number >= 1: #The loop continues as long as the number is greater than or equal to 1
    product *= number #Multiplies the current value of the product by number and stores the result back in the product
    number -= 1 #Decrements number by 1 to move on to the next number in the factorial calculation
print(product)

5040
-----------------------------------------------------------------------------------------------------------------


#Q2. Find the factorial of a number using a for loop.

number = 7 #Stores the number for which we want to calculate the factorial.
product = 1 #Store the calculated factorial and it's initialized to 1 because the factorial of 0 is 1
for i in range(number, 0, -1): #This loop iterates from number down to 1, decrementing by 1 in each iteration
    product *= i #Multiplies the current value of the product by i and stores the result back in product.
print(product)

5040
-----------------------------------------------------------------------------------------------------------------


'''
Q3. How would you write a loop to count from start_num to end_num by increments of count_by, using break_num as the variable that you'll change each time through the loop? 
What initial value should break_num have, how should it be updated in each iteration, and what condition should be used to determine when to stop looping?
'''

start_num = 20 #This variable stores the starting number for the count
end_num = 100 #This variable stores the ending number and the loop will stop when break_num reaches this value
count_by = 6 #This variable determines the increment or decrement step

break_num = start_num #To start the counting process from the specified starting point
while break_num < end_num: #The loop continues as long as break_num is less than end_num
    break_num += count_by #Increments break_num by count_by which mean the value of break_num increases by the specified amount in each step
print(break_num)

104
-----------------------------------------------------------------------------------------------------------------


'''
Q4. How would you write a loop to count from start_num to end_num by increments of count_by, using break_num as the variable that you'll change each time through the loop? 
If start_num is greater than end_num, set the result to an appropriate error message such as "Oops! Looks like your start value is greater than the end value. Please try again."
Otherwise, set the result to the final value of break_num.
'''

start_num = 20 #This variable stores the starting number for the count
end_num = 100 #This variable stores the ending number and the loop will stop when break_num reaches this value
count_by = 6 #This variable determines the increment or decrement step

if start_num > end_num: #Check if the starting number is greater than the ending number    
    result = "Oops! Looks like your start value is greater than the end value. Please try again." #If condition is true, it means user has provided an invalid input and code sets result in an error message.
else: #If the condition is false, it means the starting number is valid, and the code proceeds to the else block
    break_num = start_num #To start the counting process from the specified starting point
    while break_num < end_num: #The loop continues as long as break_num is less than end_num
        break_num += count_by #Increments break_num by count_by which mean the value of break_num increases by the specified amount in each step
    result = break_num
print(result)

104

#Testing the start_num logic

start_num = 200 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 6 #provide some number to count by 

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num
print(result)

Oops! Looks like your start value is greater than the end value. Please try again.
-----------------------------------------------------------------------------------------------------------------


#Q5. How would you write a while loop to find the largest square number less than or equal to a given integer limit, and store it in a variable nearest_square?

limit = 20 #This variable stores the specified limit
num = 1 #This variable is used to iterate through numbers to find the largest square number less than or equal to the limit and start at 1
nearest_square = 0 #This variable stores the largest square number found so far and it is initially set to 0.

while (num * num) < limit: #The loop continues as long as the square of num is less than the limit.
    nearest_square = num * num #Updates nearest_square with the current square of num as this ensures that nearest_square always holds the largest square number found
    num += 1 #Increments num by 1 to move on to the next number
print(nearest_square)

16
-----------------------------------------------------------------------------------------------------------------


'''
Q6. Create a loop that takes the numbers in a given list named num_list below. 
Your code should add up the odd numbers in the list, but only up to the first 8 odd numbers together. 
If there are more than 8 odd numbers, you should stop at the eighth. If there are fewer than 8 odd numbers, add all of the odd numbers.

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
'''

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0 #This variable keeps track of the number of odd numbers added
list_sum = 0 #This variable stores the sum of the odd numbers
i = 0 #This variable is used as an index to iterate through the num_list
len_num_list = len(num_list) #This variable stores the length of the num_list for efficiency

while (count_odd < 8) and (i < len_num_list): #Loop continues as long as these conditions are true which ensures that only first 8 odd numbers are considered and prevents index from going out of bounds of the list
    if num_list[i] % 2 != 0: #This checks if the current number (at index i) is odd. If it's odd, the following actions are performed:
        list_sum += num_list[i] #Adds the current odd number to the list_sum
        count_odd += 1 #Increments count_odd to indicate that another odd number has been added
    i += 1 #Increments the index i to move on to the next number in the list

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

The numbers of odd numbers added are: 8
The sum of the odd numbers added is: 1242

# We would write a while loop to write this code for the following reasons:
# We don't need a break statement that a for loop will require. Without a break statement, a for loop will iterate through the whole list, which is not efficient.
# We don't want to iterate over the entire list, but only over the required number of elements in the list that meet our condition.
# It is easier to understand because you explicitly control the exit conditions for the loop.
-----------------------------------------------------------------------------------------------------------------

