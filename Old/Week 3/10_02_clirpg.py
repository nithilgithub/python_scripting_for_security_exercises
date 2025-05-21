# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.


def start_game():
    print("Enter your name")
    name = input()
    print(f"Welcome, {name}! Let's begin your adventure.")

    has_sword = False

    while True:
        print("You see two doors in front of you. Do you choose the left door or the right door (left/right)")
        choice = input().lower()

        if choice == "left":
            print("The room is empty. Do you want to look around (yes/no)")
            choice = input().lower()
            if choice == "yes":
                print("You found a sword! Do you want to take it (yes/no)")
                choice = input().lower()
                if choice == "yes":
                    has_sword = True
                    print("you took the sword")
                else:
                    print("you left the sowrd")
            else:
                print("You did'nt look around")

        elif choice == "right":
            print("You encounter a dragon, Do you want to fight it? (yes/no)")
            choice = input().lower()
            if choice == "yes":
                    if has_sword:
                        print("You defeated the dragon with the sword! and win!")
                        break
                    else:
                        print("You don't have a weapon and the dragon eats you. Game over.")
                        break
            else:
                print("You decide to avoid the dragon and go back")
        else:
            print("Invalid choice, Try again.")
start_game()











            







