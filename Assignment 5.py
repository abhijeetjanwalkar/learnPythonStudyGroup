#6.1 Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
'''
person = {'first_name': 'Reshma','last_name': 'Jadhav','city': 'Wien'}

print(person['first_name'])
print(person['last_name'])
print(person['city'])
'''

#6.2 Use a dictionary to store people's favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite 
#number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number. 
'''
favourite_number = {'Reshma': 8,'Sam': 11,'Bob': 90, 'Kim': 45, 'Luk': 78}

num = favourite_number['Reshma']
print(f"Reshma's favorite nzmber is {num}")
num = favourite_number['Sam']
print(f"Sam's favorite nzmber is {num}")
'''

#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
#Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the
#word on one line and then print its meaning indented on a second line. Use the newline character ('\n') to insert a blank line between each 
#word-meaning pair in your output.

glossary = {
    'string': 'A series of characters.',
    'list': 'A collection of items.',
    'loop': 'used to work on many items but one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"{word}: {glossary[word]}")

word = 'list'
print(f"{word}: {glossary[word]}")

word = 'loop'
print(f"{word}: {glossary[word]}")

word = 'dictionary'
print(f"{word}: {glossary[word]}")
