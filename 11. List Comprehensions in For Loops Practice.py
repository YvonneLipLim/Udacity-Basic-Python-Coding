"""
List comprehensions are a concise way to create lists which provide a compact syntax to perform operations on iterables and produce new lists.
The basic syntax will be:
new_list = [expression for element in iterable if condition]

An example will be:
numbers = [1, 2, 3, 4, 5]
double_numbers = [x * 2 for x in numbers]
print(double_numbers)  # Output: [2, 4, 6, 8, 10]

Benefits of Using List Comprehensions:
1. Less code, improved readability.
2. Faster execution than for loops.
3. Handle multiple iterables and conditions.

Use Cases:
1. Convert data formats.
2. Remove unwanted data.
3. Combined data.
"""


#Q1. Extract the first names from the list, names in lowercase.
names = ["Colin Firth", "Taron Egerton", "Samuel L. Jackson", "Michael Caine", "Mark Strong"]
first_names = [name.split()[0].lower() for name in names] #Split the current full name using .split() while [0] takes the first element created by name.split() and converts to lowercase with lowercase() then iterates over each full name in the names list.
print(first_names)

#Output:
['colin', 'taron', 'samuel', 'michael', 'mark']
---------------------------------------------------------------------------------------------------------------------------


#Q2. Create multiples of 7 list named, multiples_7, containing first 20 multiples.
multiples_7 = [x*7 for x in range(1,21)]
print(multiples_7)

#Output:
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140]
---------------------------------------------------------------------------------------------------------------------------


#Q3. Create a list named, passed that only includes those scored at least 65 by using comprehension.
scores = {"Colin Firth": 95, "Taron Egerton": 88, "Samuel L. Jackson": 29, "Michael Caine": 40, "Mark Strong": 76}
passed = [name for name, score in scores.items() if score >= 65]
print(passed)

#Output:
['Colin Firth', 'Taron Egerton', 'Mark Strong']
---------------------------------------------------------------------------------------------------------------------------
