'''
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

'''

# 3.4 version

guests_list = [ 'abhi', 'Samrat','Reshma', 'Vaibhav' ]
print(f" Hi {guests_list[0]}, You are invited to join Python course")
print(f" Hi {guests_list[1]}, You are invited to join Python course")
print(f" Hi {guests_list[2]}, You are invited to join Python course")
print(f" Hi {guests_list[3]}, You are invited to join Python course")
print(f" We have invited {len(guests_list)} number of people" )

guests_list = [ 'abhi', 'Samrat','Reshma', 'Vaibhav' ]
for guest in guests_list:
    print(f" Hi {guest}, You are invited to join Python course")   

# 3.5 
print("Section 3.5")
guests_list = [ 'abhi', 'Samrat','Reshma', 'Vaibhav' ]
print(guests_list)
print(f" Hi {guests_list[-1]}, is not joining the session today")
print(f" We have invited {len(guests_list)} number of people" )

# lets remove Vaibhav from list
guests_list_popped = guests_list.pop()
print(guests_list)
# lets add Parag to list

guests_list.append("Parag")
print(guests_list)

for guest in guests_list:
    print(f" Hi {guest}, You are invited to join Python course") 

# 3.6
print("Section 3.6")
guests_list.insert(0,"Vijay")
guests_list.append("Mrunal")
print(f" We have invited {len(guests_list)} number of people" )
for guest in guests_list:
    print(f" Hi {guest}, You are invited to join Python course") 

print(guests_list)
#3.7
print("Section 3.7")
# as usual few people declined to join today so remove them from the list
del guests_list[0]


guests_list.pop()
guests_list.pop()
print(guests_list)
print(f" We have invited {len(guests_list)} number of people" )
#invite remaining people
for guest in guests_list:
    print(f" Hi {guest}, You are invited to join Python course") 
