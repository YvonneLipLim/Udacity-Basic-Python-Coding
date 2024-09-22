'''
Q1.
Create a for loop specifying the label and coordinates of each point using zip. Then appends it to the list.
Each string should be formatted as label: x, y, z. Example: F: 23,677, 4
,,,

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

point = []

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord): #Iterate over the elements of the four lists using zip function
    point.append(f"{label}: {x}, {y}, {z}") #Formatted string created using f-strings to concatenates the label, x, y, and z values and appended to point list
    print(point)

['F: 23, 677, 4']
['F: 23, 677, 4', 'J: 53, 233, 16']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6', 'W: 14, 432, 23']
['F: 23, 677, 4', 'J: 53, 233, 16', 'A: 2, 405, -6', 'Q: -12, 433, -42', 'Y: 95, 905, 3', 'B: 103, 376, -6', 'W: 14, 432, 23', 'X: -5, 445, -1']
