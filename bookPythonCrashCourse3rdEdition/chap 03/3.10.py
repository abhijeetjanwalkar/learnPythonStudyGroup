'''
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
'''
Mountains = ['Everest', 'Fuji','K2', 'Kilimanjaro', 'McKinley', 'Fuji','Fuji','Fuji','Fuji']
Rivers = ['Nile', 'Amazon', 'Yangtze', 'Danube', 'Mississippi']
Countries = ['India', 'Austria', 'Thailand', 'United Kingdom', 'France']
Cities = ['Vienna', 'Eindhoven', 'nottingham', 'Pune', 'Chiplun']
Languages = ['Marathi', 'Hindi', 'English', 'German', 'Sanskrit']

# https://www.geeksforgeeks.org/list-methods-python/

#print(f"{Mountains}")
#
##poppedMountain = Mountains.pop()
#print(f"{Mountains.pop()} ")
#print(f"{Mountains}")
#
#Mountains.append("Fuji")
#print(f"{Mountains}")
#
#Mountains.insert(1, "Kalsubai")
#print(f"{Mountains}")

#print(f"Number of my fav mounts are {len(Mountains)}")
#print(f"Number of my times Fuji in the list {Mountains.count("Fuji")}")
print(f"Give me position of Fuji in the list {Mountains.index("Fuji")}")
#
#Mountains.remove("K2")
#print(f"{Mountains}")
#
#Mountains.reverse()
#print(f"and reversed list of mountains looks like {Mountains}")
#
#Mountains.sort()
#print(f"and sorted list of mountains looks like {Mountains}")
#
#Mountains.sort(reverse=True)
#print(f"and reversed list of mountains looks like {Mountains}")