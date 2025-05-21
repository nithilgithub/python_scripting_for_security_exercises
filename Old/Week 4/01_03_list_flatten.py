#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

# Sample input
nested_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Flattening the list
flattened_list = [item for sublist in nested_list for item in sublist]

# Output the flattened list
print("Flattened list:", flattened_list)

