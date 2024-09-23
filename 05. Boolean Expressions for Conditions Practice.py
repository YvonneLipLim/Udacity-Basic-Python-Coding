"""
Boolean expressions are used to evaluate conditions, returning either True or False .
Basic Boolean Operations:
1. AND ( and ) : Returns True if both conditions are True .
2. OR ( or ) : Returns True if at least one condition is True .
3. NOT ( not ) : Returns the opposite of the condition.

The basic syntax will be:
# AND
condition1 and condition2

# OR
condition1 or condition2

# NOT
not condition

An example will be:
x = 5
y = 10

# AND
print(x > 0 and y > 5)  # True

# OR
print(x > 0 or y < 5)  # True

# NOT
print(not x > 0)  # False

Key Points to Note:
1. Understand operator precedence.
2. Evaluate conditions from left to right.
3. Boolean expressions are evaluated lazily.
4. Understand truthy and falsy values in Python.
5. Ensure variable types are compatible.
6. Use parentheses for clarity.
7. Avoid complex boolean expressions.
"""


'''
Q1. 
Create two if statements that determine a winner's prize based on their total points. The points are stored in the integer variable points. 
1st conditional statement updates the prize to the correct name based on points.
2nd conditional statement sets the result to the correct string message based on whether the prize is evaluated as True or False. 
If they had won a prize, state "Congratulations! You won a [prize name]!", if not state "Oh dear, no prize this time.".
0: None
1 - 50: Lollipop
51 - 150: Protein Bar
151 - 180: Wafer Mint
181 - 200: Box of Chocolate
'''

points = 100 #Use this input to make your submission
prize = 'None' #Set prize to default value of None

if points < 0:  #Points are invalid
    prize = 'None'
elif 1 <= points <=50:
    prize = "Lollipop"
elif 51 <= points <= 150:
    prize = "Protein Bar"
elif 151 <= points <= 180:
    prize = "Wafer Mint"
elif 181 <= points <= 200:
    prize = "Box of Chocolate"

if prize != 'None':
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."
print(result)

#Output: 
Congratulations! You won a Protein Bar!

