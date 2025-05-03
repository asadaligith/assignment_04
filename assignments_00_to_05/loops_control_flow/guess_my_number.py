import random

def guess_number():
    print("Guess Number")
    secreat_number = random.randint(1,100)

    user_guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    

    while user_guess != secreat_number:
        if user_guess < secreat_number:
            print("To Low")   
        else:
            print("To High")
        print()
        user_guess = int(input("Enter a New Guess: "))

    print(f"Congrats the Number was {secreat_number}")

   

if __name__ == '__main__':
    guess_number()

