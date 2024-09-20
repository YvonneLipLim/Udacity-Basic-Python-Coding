'''
Q1.
Find two methods to solve the cargo loading program:
Method 1: Breaking out of the loop when the weight limit is reached, however, this method has limitations. 
Method 2: Adding continue by modifying the existing loop condition
'''

#Method 1
all_cargo = [("sofa", 6), ("bananas", 10), ("chair", 20), ("mattresses", 24), ("dog kennels", 42), ("table", 4),("machine", 120), ("cheeses", 5), ("refrigerator", 8)]

print("METHOD 1")
weight = 0 #Sets the initial weight of the container to 0
items = [] #Creates an empty list to store the names of the items loaded into the container
for cargo_name, cargo_weight in all_cargo: #Iterates over each item in the all_cargo list. cargo_name and cargo_weight
    print("current weight: {}".format(weight))
    if weight >= 200: #Checks if the current weight of the container is greater than or equal to 200
        print("  breaking loop now!") #If condition is true, loop is terminated using the break statement, and print message "breaking loop now!"
        break
    else: #If condition is false (i.e., the weight is still below 200), the following actions will continue
        print("  adding {} ({})".format(cargo_name, cargo_weight)) #The current item continue to add to the container
        items.append(cargo_name) #The cargo_name is appended to the items list
        weight += cargo_weight #The cargo_weight is added to the weight of the container

print("\nFinal Weight: {}".format(weight)) #Prints the final weight of the container
print("Final Items: {}".format(items)) #Prints the list of items that were loaded into the container

METHOD 1
current weight: 0
  adding sofa (6)
current weight: 6
  adding bananas (10)
current weight: 16
  adding chair (20)
current weight: 36
  adding mattresses (24)
current weight: 60
  adding dog kennels (42)
current weight: 102
  adding table (4)
current weight: 106
  adding machine (120)
current weight: 226
  breaking loop now!

Final Weight: 226
Final Items: ['sofa', 'bananas', 'chair', 'mattresses', 'dog kennels', 'table', 'machine']


#Method 2
all_cargo = [("sofa", 6), ("bananas", 10), ("chair", 20), ("mattresses", 24), ("dog kennels", 42), ("table", 4),("machine", 120), ("cheeses", 5), ("refrigerator", 8)]

print("METHOD 2")
weight = 0 #Sets the initial weight of the container to 0
items = [] #Creates an empty list to store the names of the items loaded into the container
for cargo_name, cargo_weight in all_cargo: #Iterates over each item in the all_cargo list. cargo_name and cargo_weight
    print("current weight: {}".format(weight))
    if weight >= 200: #Checks if the current weight of the container is greater than or equal to 200
        print("  breaking from the loop now!") #If condition is true, loop is terminated using the break statement, and print message "breaking loop now!"
        break
    elif weight + cargo_weight > 200: #This new condition checks if current weight of the container plus the weight of the current item would exceed weight limit
        print("  skipping {} ({})".format(cargo_name, cargo_weight)) #If condition is true, the continue statement is used to skip the rest of the loop iteration and proceed to the next item 
        continue #Immediately jumps to the next iteration of the loop, skipping the rest of the code within the loop body for the current item
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight)) #Prints a message indicating that the current item is being added to the container, displaying the name and weight of the item added
        items.append(cargo_name) #Adds the name of the current item to the list which keep track of the items that have been successfully loaded into the container
        weight += cargo_weight #Updates the current weight to reflect the addition of the new item

print("\nFinal Weight: {}".format(weight)) #Prints the final weight of the container
print("Final Items: {}".format(items)) #Prints the list of items that were loaded into the container

METHOD 2
current weight: 0
  adding sofa (6)
current weight: 6
  adding bananas (10)
current weight: 16
  adding chair (20)
current weight: 36
  adding mattresses (24)
current weight: 60
  adding dog kennels (42)
current weight: 102
  adding table (4)
current weight: 106
  skipping machine (120)
current weight: 106
  adding cheeses (5)
current weight: 111
  adding refrigerator (8)

Final Weight: 119
Final Items: ['sofa', 'bananas', 'chair', 'mattresses', 'dog kennels', 'table', 'cheeses', 'refrigerator']
