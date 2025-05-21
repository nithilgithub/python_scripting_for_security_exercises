# Boolean Exercise_1
# Let's check all the default boolean values of the types we know

# make
# an int
# a float
# a string
# the int 0
# the int 1
# the int 1000

# now print out all the `bool()` values using the bool() function
# are you surprised at the default boolean value for any python type?

a = 0
b = 1
c = 1000

int_a = a
float_b = float(b)
string_c = str(c)

print(bool(int_a))
print(bool(float_b))
print(bool(string_c))

print(type(int_a))
print(type(float_b))
print(type(string_c))