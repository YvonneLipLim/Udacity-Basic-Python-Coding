"""
The Python Standard Library is a collection of pre-written code that provides various functionalities, making it easier to perform common tasks.
Benefits of Using the Standard Library:
1. Convenience: Avoid reinventing the wheel.
2. Efficiency: Optimized code for performance.
3. Reliability: Well-tested and maintained code.
4. Portability: Compatible across different platforms.

Categories of Standard Library Modules:
1. File and Directory Modules: os, shutil, pathlib
2. Data Structures and Utilities: collections, itertools, functools
3. Math and Statistics Modules: math, statistics, random
4. Networking and Internet Modules: socket, urllib, http
5. Cryptography and Security Modules: hashlib, hmac, ssl
6. Database Modules: sqlite3, dbm
7. GUI and Graphics Modules: tkinter, turtle

Most Commonly Used Standard Library Modules:
1. os: Interact with the operating system
    import os
    print(os.getcwd())
2. math: Perform mathematical operations
    import math
    print(math.pi)
3. random: Generate random numbers
    import random
    print(random.randint(1, 10))
4. time: Work with dates and times
    import time
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
5. json: Parse and generate JSON data
    import json
    data = {"name": "John", "age": 30}
    print(json.dumps(data))

Key Points to Note:
1. Familiarize Yourself with the Standard Library: Explore available modules.
2. Use Standard Library Modules Whenever Possible: Avoid redundant code.
3. Check Module Documentation: Understand module usage and limitations.
4. Use `help()` function to explore module documentation.
5. Use `dir()` function to list module attributes.
6. Use online resources, such as the Python documentation, to learn more about the standard library.
"""

#Q1. Import and use the math module to calculate e to the power of 3, then print the answer.

#Method 1
import math
print(math.exp(3)) #Output: 20.085536923187668

#Method 2
import math
result = math.exp(3)
print("e to the power of 3 is: ", result) #Output: 20.085536923187668
---------------------------------------------------------------------------------------------------------------------------------------


#Q2. Create a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
#The function should not accept arguments and should reference the global variable word_list to build the password.

import random
word_file = "words.txt"
word_list = []

with open(word_file,'r') as words: #Fill up the word_list from the `words.txt` file
	for line in words:
		word = line.strip().lower() #Remove white space and make everything lowercase
		if 3 < len(word) < 8: # don't include words that are too long or too short
			word_list.append(word)

def generate_password():
	return random.choice(word_list) + random.choice(word_list) + random.choice(word_list) #Concatenated together without spaces of 3 random words
print(generate_password())

#Output:
twicealicewhat
