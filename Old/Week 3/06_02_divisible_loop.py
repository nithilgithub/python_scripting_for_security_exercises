# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

# Initialize an empty list to store the results
results = []

# Use a for-loop to iterate over the range of numbers from 1500 to 2700
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        results.append(number)

# Print the results
print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700 are:")
print(results)
