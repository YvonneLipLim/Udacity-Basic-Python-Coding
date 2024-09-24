"""
Python provides various ways to read and write files.
r: Open for reading (default)
w: Open for writing, truncate if exists
a: Open for writing, append if exists
x: Open for exclusive creation, fail if exists
b: Binary mode
t: Text mode (default)
+: Open for updating (reading and writing)

Reading Files:
1. open(): Opens a file and returns a file object.
   file = open("example.txt", "r")
2. read(): Reads the entire file content.
   content = file.read()
3. readline(): Reads a single line from the file.
   line = file.readline()
4. readlines(): Reads all lines from the file into a list.
   lines = file.readlines()

Writing Files:
1. write(): Writes a string to the file.
   file.write("Hello, World!")
2. writelines(): Writes a list of strings to the file.
   file.writelines(["Line 1\n", "Line 2\n"])

Key Points to Note:
1. Specify the correct file path.
2. Choose the correct file mode.
3. Check if the file exists.
4. Ensure necessary file permissions.
5. Specify encoding for text files.
6. Use the with statement that automatically closes the file.
   with open("example.txt", "r") as file:
   content = file.read()
7. Catch and handle file-related exceptions.
8. Close files after use.

File-Related Functions:
1. os.remove(): Deletes a file.
2. os.rename(): Renames a file.
3. pathlib.Path.exists(): Checks if a file exists.

import os
os.remove("example.txt")
"""


'''
Q1.
Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. 
It will be run on the file flying_circus_cast.txt. 
Each line of that file consists of an actor's name, a comma, and then some (messy) information about the roles they played in the programme. 
Extract only the name and add it to a list. Use the .split() method(opens in a new tab) to process each line.
'''

def create_cast_list(filename): 
    cast_list = [] #Initializes an empty list to store the actor names
    with open(filename) as f: #Opens specified file named filename for reading
        for line in f: #Iterates through each line in the file
            name = line.split(",")[0] #Splits the current line by commas and extracts the first element (the name)
            cast_list.append(name) #Adds the extracted name to the cast_list
    return cast_list #Returns the list of actor names

cast_list = create_cast_list('flying_circus_cast.txt') #Call create_cast_list function with filename "flying_circus_cast.txt" and assigns returned list of actor names to cast_list variable
for actor in cast_list: #Iterates through each actor in cast_list and performs desired actions within the loop (not shown in the provided code).
    print(actor)

#Output:
Graham Chapman Eric Idle Terry Jones Michael Palin Terry Gilliam John Cleese Carol Cleveland Ian Davidson John Hughman The Fred Tomlinson Singers Connie Booth Bob Raymond Lyn Ashley Rita Davies Stanley Mason David Ballantyne Donna Reading Peter Brett Maureen Flanagan Katya Wyeth Frank Lester Neil Innes Dick Vosburgh Sandra Richards Julia Breck Nicki Howorth Jimmy Hill Barry Cryer Jeannette Wild Marjorie Wilde Marie Anderson Caron Gardner Nosher Powell Carolae Donoghue Vincent Wong Helena Clayton Nigel Jones Roy Gunson Daphne Davey Stenson Falke Alexander Curry Frank Williams Ralph Wood Rosalind Bailey Marion Mould Sheila Sands Richard Baker Douglas Adams Ewa Aulin Reginald Bosanquet Barbara Lindley Roy Brent Jonas Card Tony Christopher Beulah Hughes Peter Kodak Lulu Jay Neill Graham Skidmore Ringo Starr Fred Tomlinson David Hamilton Suzy Mandel Peter Woods

