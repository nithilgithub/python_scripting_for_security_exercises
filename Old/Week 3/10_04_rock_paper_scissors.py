# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

computer_choice = random.randint(1, 3)

# you can map each of rock / paper / scissors to an integer from 1 - 3

rock = 1
papper = 2
scissors = 3

while True:
    option = int(input("Enter a number between (1-3) "))

    if option == 1:
        print(rock)
    elif option == 2:
        print(papper)
    else:
        print(scissors)