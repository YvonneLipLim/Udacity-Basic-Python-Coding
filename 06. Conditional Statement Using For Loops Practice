'''
Q1.
Create usernames from a given list of names. The usernames should be lowercases versions of the names with all spaces replaced by underscores. Add the email domain of @abc.com to the usernames too.
Katharine Hepburn
Meryl Streep
Jack Nicholson
Ingrid Bergman
Daniel Day-Lewis
Frances McDormand
Walter Brennan
Bette Davis
Spencer Tracy
Marlon Brando

names =["Katharine Hepburn", "Meryl Streep", "Jack Nicholson", "Ingrid Bergman", "Daniel Day-Lewis", "Frances McDormand", "Walter Brennan", "Bette Davis", "Spencer Tracy", "Marlon Brando"]
usernames = []

for name in names: #iterates over each name in the names list
    lowercase_name = name.lower().replace(" ", "_") #converts the name to lowercase aqnd replaces all spaces in the name with underscores
    email = lowercase_name + "@abc.com" #converts lowercase name to email address
    usernames.append(email) #adds the email domain to the usernames
print(usernames)

['katharine_hepburn@abc.com', 'meryl_streep@abc.com', 'jack_nicholson@abc.com', 'ingrid_bergman@abc.com', 'daniel_day-lewis@abc.com', 'frances_mcdormand@abc.com', 'walter_brennan@abc.com', 'bette_davis@abc.com', 'spencer_tracy@abc.com', 'marlon_brando@abc.com']
'''


'''
Q2. Given the input name list as below, modify it to a usernames list with everything lowercase and replaces spaces with underscores running in for loop over the list.
names =["Katharine Hepburn", "Meryl Streep", "Jack Nicholson", "Ingrid Bergman", "Daniel Day-Lewis", "Frances McDormand", "Walter Brennan", "Bette Davis", "Spencer Tracy", "Marlon Brando"]

usernames = ["Katharine Hepburn", "Meryl Streep", "Jack Nicholson", "Ingrid Bergman", "Daniel Day-Lewis", "Frances McDormand", "Walter Brennan", "Bette Davis", "Spencer Tracy", "Marlon Brando"]
for names in range(len(usernames)): #This loop structure allows access to both the index i and the element at that index in the list.
    usernames[names] = usernames[names].lower().replace(" ", "_") #converts the name to lowercase aqnd replaces all spaces in the name with underscores
print(usernames)

['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
'''


'''
Q3.
Create a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags(opens in a new tab). Keep track of the number of tags using the variable count.

tokens = ["<html>", "Hello", "<body>", "Welcome", "</body>", "</html>"]
count = 0 #To keep track of the number of XML tags begin with 0

for token in tokens: #iterates over each string in the tokens list
    if token.startswith("<") and token.endswith(">"): #Check if the string starts with "<" and ends with ">", indicating it is an XML tag.
        count += 1 #If string is identified as XML tag, count is incremented
print(count)

4
'''


'''
Q4.
Creatre a for loop that iterates over a list of strings and creates a single string, html_str, which is an HTML list. 
For example, if the list is items = ['first string', 'second string'], printing html_str should output:
<ul>
<li>first string</li>
<li>second string</li>
</ul>

items = ['Hello World', 'Welcome 2024']
html_str = "<ul>\n"

for item in items: #iterates over each string in the items list
    html_str += "<li>" + item + "</li>\n" #Adding each item enclosed in <li> tags to the current item followed by </li>\n which creates an HTML list 
html_str += "</ul>" #Adding closing tag </ul>
print(html_str)

<ul>
<li>Hello World</li>
<li>Welcome 2024</li>
</ul>
'''


