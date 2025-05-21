# Type Casting Exercise

a = 7

# 1. print the type of the variable
#   Convert integer variable to float and confirm the type cast worked (print it out)

print(type(a))
float_a = float(a)
print(float_a)
print(type(float_a))


# 2. Now, Convert your float variable to string and print out the type
string_a = str(float_a)
print(string_a)
print(type(string_a))

# 3. Finally, Convert your string variable back to integer and print it out (the type)
integer_a = int(string_a)
print(integer_a)
print(type(integer_a))

# above will through error as a string cannot typecast to integer
