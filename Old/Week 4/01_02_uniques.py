# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]


list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

# Convert the list to a set to remove duplicates, then back to a list
unique_list = list(set(list_))

print("Unique values:", unique_list)