# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# List to store prime numbers
primes = []

# Find all prime numbers between 0 and 100
for number in range(101):
    if is_prime(number):
        primes.append(number)

# Print all prime numbers
print("Prime numbers between 0 and 100 are:")
print(primes)

# Print the count of prime numbers
print(f"Total number of prime numbers between 0 and 100: {len(primes)}")
