# Logical_operators_4

# Initialize variable a to true, b to false and c to true
a = True
b = False
c = True

# Print the value of:
# what do you think: print(a and b or c)  will return? Why?
print(a and b or c)
# Does the order of operations matter?
# is print(a or b and c) different?
print(a or b and c)

# Assign c to false and print the value of a and b or c
a = True
b = False
c = False

print(a and b or c)

# Understand the difference in each scenario
# what is happening here?

# now try to use some ()'s to force python to evaluate it differently.
# For example:
a = True
b = False
c = False

print((a and b) or c)   # Parentheses force 'a and b' to be evaluated first
print(a and (b or c))   # Parentheses force 'b or c' to be evaluated first