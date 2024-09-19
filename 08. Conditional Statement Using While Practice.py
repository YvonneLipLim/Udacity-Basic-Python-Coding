#Q1. Find the factorial of a number using a while loop.

number = 7 #Stores the number for which we want to calculate the factorial.
product = 1 #Store the calculated factorial and it's initialized to 1 because the factorial of 0 is 1
current = 1 #Keeps track of the current number being multiplied in the factorial calculation that starts at 1

while number >= 1: #The loop continues as long as number is greater than or equal to 1
    product *= number #Multiplies the current value of product by number and stores the result back in product
    number -= 1 #Decrements number by 1 to move on to the next number in the factorial calculation
print(product)

5040
-----------------------------------------------------------------------------------------------------------------

#Q2 Find the factorial of a number using a for loop.
number = 7 #Stores the number for which we want to calculate the factorial.
product = 1 #Store the calculated factorial and it's initialized to 1 because the factorial of 0 is 1
for i in range(number, 0, -1): #This loop iterates from number down to 1, decrementing by 1 in each iteration
    product *= i #Multiplies the current value of product by i and stores the result back in product.
print(product)

5040
-----------------------------------------------------------------------------------------------------------------

#Q#
