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

int_a = 0
int_b = 1
int_c = 1000

print(bool(int_a))
print(bool(int_b))
print(bool(int_c))

float_a = float(int_a)
float_b = float(int_b)
float_c = float(int_c)

print(bool(float_a))
print(bool(float_b))
print(bool(float_c))

string_a = str(float_a)
string_b = str(float_b)
string_c = str(float_c)

print(bool(string_a))
print(bool(string_b))
print(bool(string_c))