'''
Q1. Create a dictionary using the below book titles that count the occurrences of each word in a string using for loops. 
The Housemaid Is Watching
Eruption
Swan Song
Dad I Want To Hear Your Story
The Women
The Housemaid
A Court of Thorns and Roses
Camino Ghost
Reckless The Powerless Trilogy
Dog Man: The Scarlet Shedder
'''

#Counting using for loops:
book_titles = ['The', 'Housemaid', 'Is', 'Watching', 'Eruption', 'Swan', 'Song', 'Dad', 'I', 'Want', 'To', 'Hear', 'Your', 'Story', 'The', 'Women', 'The', 'Housemaid', 'A', 'Court', 'of', 'Thorns', 'and', 'Roses', 'Camino', 'Ghost', 'Reckless', 'The', 'Powerless', 'Trilogy', 'Dog', 'Man:', 'The', 'Scarlet', 'Shedder']
word_counter = {}

for word in book_titles: #iterate over each book title in the book_titles list
    if word not in word_counter: #checks if the current book title (word) is already a key in the word_counter dictionary and if the word is not found, it means it's encountered for the first time
        word_counter[word] = 1 #If the word is not found, it's added as a key to the word_counter dictionary with a value of 1, indicating its first occurrence
    else:
        word_counter[word] +=1 #If the word is found in the word_counter dictionary, it means it has been encountered before. The value associated with that word (which represents its count) is incremented by 1 to reflect the additional occurrence.
print(word_counter)

{'The': 5, 'Housemaid': 2, 'Is': 1, 'Watching': 1, 'Eruption': 1, 'Swan': 1, 'Song': 1, 'Dad': 1, 'I': 1, 'Want': 1, 'To': 1, 'Hear': 1, 'Your': 1, 'Story': 1, 'Women': 1, 'A': 1, 'Court': 1, 'of': 1, 'Thorns': 1, 'and': 1, 'Roses': 1, 'Camino': 1, 'Ghost': 1, 'Reckless': 1, 'Powerless': 1, 'Trilogy': 1, 'Dog': 1, 'Man:': 1, 'Scarlet': 1, 'Shedder': 1}
-----------------------------------------------------------------------------------------------------------------------


#Q2. Create a dictionary using the above book titles that combine the for loop and the get method to count the occurrences of each word in a string.

#Using get() method:
book_titles = ['The', 'Housemaid', 'Is', 'Watching', 'Eruption', 'Swan', 'Song', 'Dad', 'I', 'Want', 'To', 'Hear', 'Your', 'Story', 'The', 'Women', 'The', 'Housemaid', 'A', 'Court', 'of', 'Thorns', 'and', 'Roses', 'Camino', 'Ghost', 'Reckless', 'The', 'Powerless', 'Trilogy', 'Dog', 'Man:', 'The', 'Scarlet', 'Shedder']
word_counter = {}

for word in book_titles: #iterate over each book title in the book_titles list
  word_counter[word] = word_counter.get(word, 0)+1
print(word_counter)

{'The': 5, 'Housemaid': 2, 'Is': 1, 'Watching': 1, 'Eruption': 1, 'Swan': 1, 'Song': 1, 'Dad': 1, 'I': 1, 'Want': 1, 'To': 1, 'Hear': 1, 'Your': 1, 'Story': 1, 'Women': 1, 'A': 1, 'Court': 1, 'of': 1, 'Thorns': 1, 'and': 1, 'Roses': 1, 'Camino': 1, 'Ghost': 1, 'Reckless': 1, 'Powerless': 1, 'Trilogy': 1, 'Dog': 1, 'Man:': 1, 'Scarlet': 1, 'Shedder': 1}
-----------------------------------------------------------------------------------------------------------------------


'''
Q3. Create an iteration through a dictionary to access the keys and values from the below cast list. 
Given a dictionary that uses actors' names as keys and their characters as values, print each actor's name along with their corresponding character.

The cast of Dune Part 2:
Timothee Chalamet as Paul Atreides
Zendaya as Chani
Rebecca Ferguson as Jessica
Javier Bardem as Stilgar
Josh Brolin as Gurney Halleck
Austin Butler as Feyd-Rautha
Florence Pugh as Princess Irulan
Dave Bautista as Beast Rabban
Christopher Walken as Emperor
Lea Seydoux as Lady Margot Fenring
'''

cast = {
        "Timothee Chalamet": "Paul Atreides",
        "Zendaya": "Chani",
        "Rebecca Ferguson": "Jessica",
        "Javier Bardem": "Stilgar",
        "Josh Brolin": "Gurney Halleck",
        "Austin Butler": "Feyd-Rautha",
        "Florence Pugh": "Princess Irulan",
        "Dave Bautista": "Beast Rabban",
        "Christopher Walken": "Emperor",
        "Lea Seydoux": "Lady Margot Fenring"
}
print("Iterating through keys")
for key in cast: #iterates directly over the keys of the cast dictionary
    print(key) #This loop prints each actor's name (the key)

print("\nIterating through keys and values:")
for key, value in cast.items(): #Uses the items() method to iterate over the keys and values of the cast dictionary which returns tuples of key-value pairs that represent the actor's name, and the character they play.
    print("Actor: {} Role: {}".format(key,value)) #Display the actor's name and their character in a readable format.

Iterating through keys
Timothee Chalamet
Zendaya
Rebecca Ferguson
Javier Bardem
Josh Brolin
Austin Butler
Florence Pugh
Dave Bautista
Christopher Walken
Lea Seydoux

Iterating through keys and values:
Actor: Timothee Chalamet Role: Paul Atreides
Actor: Zendaya Role: Chani
Actor: Rebecca Ferguson Role: Jessica
Actor: Javier Bardem Role: Stilgar
Actor: Josh Brolin Role: Gurney Halleck
Actor: Austin Butler Role: Feyd-Rautha
Actor: Florence Pugh Role: Princess Irulan
Actor: Dave Bautista Role: Beast Rabban
Actor: Christopher Walken Role: Emperor
Actor: Lea Seydoux Role: Lady Margot Fenring
-----------------------------------------------------------------------------------------------------------------------


#Q4. Working with a dictionary and a list to count the number of fruits in a trolley with the given data below.

result = 0 #This variable will store the running total of fruit count
trolley_items = {'eggs': 12, 'bananas': 6, 'cheese': 1, 'broccoli': 2, 'apples': 5, 'strawberries': 1, 'bread': 1, 'potatoes': 8, 'watermelon': 1, 'cookies': 5, 'juice': 2, 'orange': 10} #List of items and the quantity
fruits = ['apples', 'bananas', 'grapes', 'orange', 'pears', 'peaches', 'strawberries', 'watermelon'] #List containing the names of various fruits

for fruit, count in trolley_items.items(): #Iterates over each key-value pair in the trolley_items dictionary
    if fruit in fruits: #Check if the current item (fruit) is present in the fruits list and if the item is a fruit, it means it's one of the fruits we want to count
        result += count #If the item is a fruit, its count (quantity) is added to the result variable, incrementing the running total of fruits
print(result)

23
-----------------------------------------------------------------------------------------------------------------------


#Q5. Apply Q4 solutions to work on the following dictionary to make sure it works.

result = 0
trolley_items = {'peaches': 5, 'bananas': 10, 'tuna': 4, 'bell pepper': 4, 'pears': 5, 'strawberries': 1, 'bread': 1, 'potatoes': 8, 'grapes': 1, 'cookies': 5, 'juice': 2, 'orange': 10}
fruits = ['apples', 'bananas', 'grapes', 'orange', 'pears', 'peaches', 'strawberries', 'watermelon']
for fruit, count in trolley_items.items(): #Iterates over each key-value pair in the trolley_items dictionary
    if fruit in fruits: #If the item is a fruit, its count (quantity) is added to the result variable, incrementing the running total of fruits
        result += count
print(result)

32
-----------------------------------------------------------------------------------------------------------------------


#Q6 Use the for loops method to track the number of fruits and other items in the trolley for Q4 and Q5.

fruit_count, not_fruit_count = 0, 0 #This variable will store the running total of fruit_count and not_fruit_count to default 0
trolley_items = {'eggs': 12, 'bananas': 6, 'cheese': 1, 'broccoli': 2, 'apples': 5, 'strawberries': 1, 'bread': 1, 'potatoes': 8, 'watermelon': 1, 'cookies': 5, 'juice': 2, 'orange': 10}
fruits = ['apples', 'bananas', 'grapes', 'orange', 'pears', 'peaches', 'strawberries', 'watermelon']
for fruit, count in trolley_items.items(): #Iterates over each key-value pair in the trolley_items dictionary
    if fruit in fruits: #Check if the current item (fruit) is present in the fruits list and if the item is a fruit, it means it's one of the fruits we want to count
        fruit_count += count #A variable that keeps track of the total number of fruits
    else: #If the item is not a fruit
        not_fruit_count += count #The variable is incremented by count, adding the quantity of the non-fruit item to the total.
print(fruit_count,not_fruit_count)

fruit_count, not_fruit_count = 0, 0 #This variable will store the running total of fruit_count and not_fruit_count to default 0
trolley_items = {'peaches': 5, 'bananas': 10, 'tuna': 4, 'bell pepper': 4, 'pears': 5, 'strawberries': 1, 'bread': 1, 'potatoes': 8, 'grapes': 1, 'cookies': 5, 'juice': 2, 'orange': 10}
fruits = ['apples', 'bananas', 'grapes', 'orange', 'pears', 'peaches', 'strawberries', 'watermelon']

for fruit, count in trolley_items.items(): #Iterates over each key-value pair in the trolley_items dictionary
    if fruit in fruits: #Check if the current item (fruit) is present in the fruits list and if the item is a fruit, it means it's one of the fruits we want to count
        fruit_count += count #A variable that keeps track of the total number of fruits
    else: #If the item is not a fruit
        not_fruit_count += count #The variable is incremented by count, adding the quantity of the non-fruit item to the total.
print(fruit_count,not_fruit_count)

23 31
32 24
