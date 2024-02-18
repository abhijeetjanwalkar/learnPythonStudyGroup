# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Also, use the sum() function to see how quickly Python can add  a million numbers.
million = [number for number in range(1,1000001)]
total = 0
minimum = min(million)
print(f"the smallest number is {minimum}")

maximum = max(million)
print(f"The biggest number is {maximum}")
for number in million:
    total = total + number
print(f"the total is {total}")
totalByFUnction = sum(million)
print(f"total by sum function is {totalByFUnction}")