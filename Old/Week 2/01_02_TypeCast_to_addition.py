# Type casting Exercise - 2
# Addition of string and integer using explicit conversion

# Initialise a string variable and integer variable
a = 10
b = "10"

int_a = a
int_b = int(b)


# After explicit conversion, use python to successfully perform
# the addition of these variables - print the result to the console

c = int_a + int_b
print(c)

## Now try to convert this variable
c = "ten"

int_c = int(c)
print(type(int_c))

## What kind of error does python give?
## What do you think the reason is?
## Python gives an error like "ValueError: invalid literal for int() with base 10: 'ten'", because python can typecast numerical
## strings with int() function, for example "10" or "45" but not "ten" because its not a numerical value.