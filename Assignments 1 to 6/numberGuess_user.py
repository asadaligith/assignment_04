import random

# Guess the Number Game Python Project (user)

def main():
    print("Number Guessing Game")
    print("Computer Choose a one Number between 1 to 100 you guess the correct Number in 7 attempts")

    secreat_number = random.randint(1,100)
    attempts = 7
    while attempts > 0:
        try:
            user_input = int(input("Guess The Secreat Number: "))
            attempts -= 1
            if user_input > secreat_number:
                print(f"To High {attempts} attempts left")
            elif user_input < secreat_number:
                print(f"To Low {attempts} attempts left")
            else:
                print(f"\nYou Choose Correct {secreat_number}")
                break

        except ValueError:
            print("Invalid Input! Enter a Number Between 1 to 100")

        if attempts == 0:
            print(f"\nGame Over You Lose the Game! The secreate Number is {secreat_number}")
            break

if __name__ == '__main__':
    main()
