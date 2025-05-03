import random

def guess_number():
    secret_number : int = random.randint(1,99)    # Generate random Number
    print("I am thinking of a number between 1 and 99...")

    
    user_guess = int(input("Enter your Guess: "))

    while user_guess != secret_number:
        if user_guess < secret_number:
            print("To Low!")
        else:
            print("To High!")

        print()
        user_guess = int(input("Enter New Guess: "))
    print(f"Congrats! The Number was {secret_number}")

if __name__ == '__main__':
    guess_number()

    