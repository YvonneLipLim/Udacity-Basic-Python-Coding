"""
Generators are a simple and powerful tool for creating iterators. A generator is a special type of iterable, similar to lists or tuples. 
However, unlike lists, generators do not store all values in memory simultaneously. Instead, they compute each value as it's needed.

They are written like regular functions but use the yield statement whenever they want to return data. 
Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). 

How Generators Work
1. Initialization: When called, a generator function returns a generator object.
2. Iteration: When next() is called on the generator, execution starts or resumes from the last yield.
3. Yielding: The yield statement returns a value and pauses execution.
4. Resuming: Execution resumes from the last yield when next() is called again.

An example shows that generators can be trivially easy to create:
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

When to Use Generators
1. Handling Large Datasets: Process large datasets without loading entire data into memory.
2. Creating Infinite Sequences: Generate infinite sequences without consuming infinite memory.
3. Improving Performance: Reduce memory usage and improve performance in computationally expensive tasks.
4. Streaming Data: Process streaming data in real-time.
"""


#Q1. Create a generator function that works like enumerate function with the following output:
#Lesson 1: Why Python Programming
#Lesson 2: Data Types and Operators
#Lesson 3: Control Flow
#Lesson 4: Functions
#Lesson 5: Scripting

#Method 1
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0): #Custom implementation of the built-in enumerate function that takes an iterable object (iterable) as input and an optional start parameter, which defaults to 0
    count = start #Initializes a variable count to the value of the start parameter which keep track of the current count
    for element in iterable: #Loop iterates over each element in the iterable object
        yield count, element #Makes my_enumerate a generator function and return a tuple containing 2 elements, count and element
        count += 1 #Increments the count variable by 1, preparing it for the next iteration of the loop
      
for i, lesson in my_enumerate(lessons, 1): #Iterates over the results of my_enumerate and unpacks the tuples into i (index) and lesson (element)
    print("Lesson {}: {}".format(i, lesson)) #Prints the formatted string, displaying the lesson number (starting from 1) and the corresponding lesson name

#Output:
Lesson 1: Why Python Programming 
Lesson 2: Data Types and Operators 
Lesson 3: Control Flow 
Lesson 4: Functions Lesson 5: Scripting
--------------------------------------------------------------------------------------------------------------------------------------

#Method 2
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0): #Custom implementation of the built-in enumerate function that takes an iterable object (iterable) as input and an optional start parameter, which defaults to 0
    for i in range(start, len(iterable) + start): #Loop iterates over a range of indices, starting from start and going up to len(iterable) + start - 1
        yield i, iterable[i - start] #Create a generator and in each oteration it returns a tuple containing 2 elements i the current indent and iterable[i - start] the element of current index at original iterable

for i, lesson in my_enumerate(lessons, 1): #Iterates over the results of my_enumerate and unpacks the tuples into i (index) and lesson (element)
    print("Lesson {}: {}".format(i, lesson)) #Prints the formatted string, displaying the lesson number (starting from 1) and the corresponding lesson name

#Output:
Lesson 1: Why Python Programming 
Lesson 2: Data Types and Operators 
Lesson 3: Control Flow 
Lesson 4: Functions Lesson 5: Scripting
--------------------------------------------------------------------------------------------------------------------------------------


#Q2. Create a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time with the following output:
#[0, 1, 2, 3]
#[4, 5, 6, 7]
#[8, 9, 10, 11]
#[12, 13, 14, 15]
#[16, 17, 18, 19]
#[20, 21, 22, 23]
#[24]

def chunker(iterable, size): #Function is designed to break down an iterable object (like a list, tuple, or range) into smaller chunks of a specified size
    for i in range(0, len(iterable), size): #Loop iterates over a range of indices, starting from 0 and incrementing by size each time
        yield iterable[i:i+size] #Create a generator, in each iteration it returns a slice of iterable starting at index i and end at index i + size - 1 which represents a chunk of original iterable

for chunk in chunker(range(25), 4): #Iterates over the chunks generated by chunker function with the range 0 to 24 as the iterable and a chunk size of 4
    print(list(chunk)) #Converts the chunk (which is a generator object) into a list and prints it

#Output:
[0, 1, 2, 3] [4, 5, 6, 7] [8, 9, 10, 11] [12, 13, 14, 15] [16, 17, 18, 19] [20, 21, 22, 23] [24]
