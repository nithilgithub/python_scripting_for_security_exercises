# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.

largest_number =  num_three

if (num_one > largest_number):
    largest_number = num_one
if(num_two > largest_number):
    largest_number = num_two
if(num_four > largest_number):
    largest_number = num_four

else:
    print(f"{num_three} is the largest number")