import random

# Guess the Number Game Python Project (computer)

def number_guessing_game():
    print("Number Guessing Game")
    print("NUmber Guess by Computer")
    try:
        user_input = int(input("Choose a Number between 1 to 50: "))
        if user_input < 1 or user_input > 50:
            print("Choose a number only between 1 to 50")
            
    except ValueError:
        print("Invalid Input! Choose a number between 1 to 50")
        
    
    low, high = 1, 50
    attempts = 0
    
    while True:
        computer_guess = random.randint(low, high)
        attempts += 1
        print(f"Computer guesses: {computer_guess}")
        user_reply = input("Tell if the number is Correct, High, or Low: ").strip().lower()
        
        if user_reply == "correct":
            print(f"Computer guessed the correct number {computer_guess} in {attempts} attempts!")
            break
        elif user_reply == "high":
            high = computer_guess - 1
        elif user_reply == "low":
            low = computer_guess + 1
        else:
            print("Invalid input! Please enter 'Correct', 'High', or 'Low'.")

number_guessing_game()
