"""
String methods are used to manipulate and transform strings in Python.
Common String Methods:

1. String Transformation
lower() : Converts to lowercase.
upper() : Converts to uppercase.
title() : Converts to title case.
strip() : Removes leading and trailing whitespace.

An example will be:
text = " Hello, World! "
print(text.lower()) # "hello, world!"
print(text.upper()) # "HELLO, WORLD!"
print(text.title()) # "Hello, World!"
print(text.strip()) # "Hello, World!"

2. String Searching
find(): Returns the index of the first occurrence.
rfind(): Returns the index of the last occurrence.
index(): Returns the index of the first occurrence (raises ValueError if not found).
count(): Returns the number of occurrences.

An example will be:
text = "Hello, World!"
print(text.find("World"))  # 7
print(text.rfind("World"))  # 7
print(text.index("World"))  # 7
print(text.count("l"))  # 3

3. String Replacement
replace(): Replaces occurrences of a substring

An example will be:
text = "Hello, World!"
print(text.replace("World", "Universe")) # "Hello, Universe!"

4. String Splitting
split(): Splits into a list of substrings.
rsplit(): Splits into a list of substrings from the right.

An example will be:
text = "apple,banana,cherry"
print(text.split(","))  # ["apple", "banana", "cherry"]
print(text.rsplit(",", 1))  # ["apple,banana", "cherry"]

5. String Joining
join(): Joins a list of strings into a single string

An example will be:
fruits = ["apple", "banana", "cherry"]
print(",".join(fruits)) # "apple,banana,cherry"


6. String Formatting
format(): Formats a string with placeholders.

An example will be:
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

String Method Variations:
1. Regular Expressions: Use the re module for advanced string matching.
2. String Interpolation: Use f-strings or the format() method.
3. Unicode Strings: Use Unicode literals or encoding declarations.
"""

'''
Q1 Create a string variable that contains the first verse of the poem, The Victor, by C. W. Longenecker and find out:
What is the length of the string variable?
What is the index of the first occurrence of the word 'win' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse?

If you think you are beaten, you are.
If you think you dare not, you don’t.
If you like to win but think you can’t,
It’s almost a cinch you won’t.
If you think you’ll lose, you’re lost.
For out in the world we find
Success begins with a fellow’s will.
It’s all in the state of mind.
'''

poem = "If you think you are beaten, you are.\nIf you think you dare not, you don’t.\nIf you like to win but think you can’t,\nIt’s almost a cinch you won’t.\nIf you think you’ll lose, you’re lost.\nFor out in the world we find\nSuccess begins with a fellow’s will.\nIt’s all in the state of mind."
print(poem)
print("The poem has a length of {} characters.".format(len(poem))) #Using format method to take the result of (len(variable) to find the length of text string stored in variable and insert into {} placeholder
print("The first occurrence of the word 'win' occurs at the {}th index.".format(poem.find('win'))) #Using format method to take the result of (variable.find(' ') to find the lowest index and insert into {} placeholder
print("The last occurrence of the word 'you' occurs at the {}th index.".format(poem.rfind('you'))) #Using format method to take the result of (variable.rfind(' ') to find the highest index and insert into {} placeholder
print("The word 'you' occurs {} times in the poem.".format(poem.count('you'))) #Using format method to take the result of (variable.count(' ') to count words and insert them into {} placeholder

#Output:
If you think you are beaten, you are.
If you think you dare not, you don’t.
If you like to win but think you can’t,
It’s almost a cinch you won’t.
If you think you’ll lose, you’re lost.
For out in the world we find
Success begins with a fellow’s will.
It’s all in the state of mind.
The poem has a length of 282 characters.
The first occurrence of the word 'win' occurs at the 91th index.
The last occurrence of the word 'you' occurs at the 173th index.
The word 'you' occurs 12 times in the poem.
