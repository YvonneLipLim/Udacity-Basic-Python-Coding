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

