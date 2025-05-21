# Exercise

# Write a program by accepting 2 numbers from the user and check number is greater than other and print the result
# you can use the function `input()` to get user input

# example
first_number = input("please enter a number: ")
second_number = input("please enter another number!: ")

if (first_number > second_number):

   print(f"{first_number} is greater")

else:

   print(f"{second_number} is greater")

print(type(first_number))
print(type(second_number))

## note, what type is your first_number? Is it what you expected?

#By default, the input() function returns a string. So, when you compare first_number and second_number,
# you’re comparing their lexicographical order, not their numerical values.

## look-up the input() documentation to find out what type it will create by default

#For example, "10" is considered less than "2" when comparing as strings because "1"
# comes before "2" lexicographically.

#to fix this issue for taking input use below code, by adding int before input

first_number = int(input("please enter a number: "))
second_number = int(input("please enter another number!: "))

if first_number > second_number:
    
    print(f"{first_number} is greater than {second_number}")
else:
    print(f"{second_number} is greater than {first_number}")

print(type(first_number))
print(type(second_number))