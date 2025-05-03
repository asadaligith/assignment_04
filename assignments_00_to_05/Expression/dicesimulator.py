import random

# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

print("\nDice rolling Three Times \n ")

num_side = 6     # global variable

def roll_dice():
    die1 : int = random.randint(1, num_side)   #Local Variable
    die2 : int = random.randint(1, num_side)   #Local Variable
    total = die1 + die2

    print(f"Die 1: {die1}, Die 2: {die2} => Total: {total}")

def main():
    die1 = 10  # Local variable of inner function (ye roll_dice se independent hai)
    for _ in range(3):
        roll_dice()

if __name__ == '__main__':
    main()