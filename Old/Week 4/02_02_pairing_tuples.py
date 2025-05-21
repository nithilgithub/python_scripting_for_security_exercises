### This code creates a random list for you to use
import random

# Generate a random list of numbers
list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))

# Sort the list
randlist.sort()

# Create a new list to store tuples
tuple_list = []

# Process the list in pairs
for i in range(0, len(randlist), 2):
    if i + 1 < len(randlist):  # If there's a pair
        tuple_list.append((randlist[i], randlist[i + 1]))
    else:  # If the list has an odd number of items
        tuple_list.append((randlist[i], 0))

# Print each tuple
for t in tuple_list:
    print(t)

# Write a script that takes randlist (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

# Note: This lab might be challenging! Make sure to discuss ask questions
# and get help!  You will need a python function called `sort`

# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]