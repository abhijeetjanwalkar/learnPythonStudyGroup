#8.1 Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the 
#function, and make sure the message displays correctly.
'''
display_message = 'We are learning about Python.'
print(display_message)
'''
            #OR
'''
def display_message():
    msg = "We are learning Python."
    print(msg)

display_message()
'''

#8.2 Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite 
#books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
'''
def favorite_book(title):
    print(f"{title} is one of my favorite books.")

favorite_book('Secret Seven')
'''

#8.3 Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments 
#to make a shirt. Call the function a second time using keyword arguments.
'''
def make_shirt(size , message):
    print(f" I will make {size} size of the shirt")
    print(f"It will say {message}")

make_shirt('small', 'Python is cool.')
'''
#8.4 Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a 
#medium shirt with the default message, and a shirt of any size with a different message.
'''
def make_shirt():
    print(f" I will make large size of the shirt")
    print(f"It will say Python is cool")

make_shirt()
'''
                    #OR
'''
def make_shirt(size='large', message='Python is cool'):
   
    print(f"I'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
'''

#8.5 Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least
# one of which is not in the default country.

def describe_city(city_name, country):
    print(f"{city_name} is in {country}.")

describe_city('Pune', 'India')
