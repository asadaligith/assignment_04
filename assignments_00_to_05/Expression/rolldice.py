import random
 
# Simulate rolling two dice, and prints results of each roll as well as the total

num_side = 6

def roll_dice():
    die1 = random.randint(1, num_side)
    die2 = random.randint(1,num_side)
    total_dice = die1 + die2

    print(f"🎲 Dice 1st {die1} + Dice 2nd {die2} 🎲 Total = {total_dice}")

if __name__ == '__main__':
    roll_dice()