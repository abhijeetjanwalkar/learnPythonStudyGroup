'''
8-6. City Names: 
Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile"
Call your function with at least three city-country pairs, and print the values that are returned.
'''

def city_country(city, country):
    """ This functions take city and country name as input and prints "City, Country" """
    cityAndCountry = f"{city}, {country}"
    #print(f"{cityAndCountry}")
    return cityAndCountry.title()

citylist = city_country("India", "Pune") 
print(f"{citylist}")
citylist = city_country("Austria", "Wien")
print(f"{citylist}")
citylist = city_country("InDia", "MumBai")
print(f"{citylist}")