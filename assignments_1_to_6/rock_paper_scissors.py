# Rock, paper, scissors Python Project
import random

print("Welcome to the Rock , Paper, Scissors Game")
choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0

def rock_paper_scissors():
    global user_score, computer_score, draws
    computer_choice = random.choice(choices)

    user_choice = input("Choose one (rock, paper, scissors): ").strip().lower() # Taken Input from User

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")  # if user input rong choice print this line
        return

    if user_choice == computer_choice:
        print(f"It's a draw! Both chose {computer_choice}.")
        draws += 1

    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You win! You chose {user_choice}, computer chose {computer_choice}.")
        user_score +=1
    
    else:
        print(f"Computer wins! Computer chose {computer_choice}.")
        computer_score +=1


while True:
    rock_paper_scissors()
    play_again = input("\nPlay again? (yes/no): ").strip().lower() # using loop if user want to play again.
    if play_again != "yes":
        print("\n🏁 Final Score:")
        print(f"🧍 You: {user_score}")
        print(f"💻 Computer: {computer_score}")
        print(f"🤝 Draws: {draws}")
        print("Thanks for playing!")
        break


