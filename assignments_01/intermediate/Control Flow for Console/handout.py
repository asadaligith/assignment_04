import random

user_score = 0
computer_score = 0

def handout():
    global user_score , computer_score
    user_number = random.randint(1,100)
    computer_number = random.randint(1,100)

    print(f"Your Number is {user_number}")
    user_input = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    if user_input not in ["higher", "lower"]:
        print("Invalid input! Please type 'higher' or 'lower'.")
        return

    if user_input == "lower" and user_number < computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        user_score += 1
        

    elif user_input == "higher" and user_number > computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        user_score += 1
        

    elif user_input == "lower" and user_number > computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        computer_score += 1
        

    elif user_input == "higher" and user_number < computer_number:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        computer_score += 1

    else:
        print(f"(Round Tigh Up!) Your Number {user_number} and computer Number {computer_number} are equal.")

    print(f"Your score: {user_score} | Computer score: {computer_score}")

def main():
    print("🎮Welcome to the High-Low Game!")
    for round in range(1,6):
        print(f"\n---Round: {round}---")
        handout()
        print()

    print("Game Over")

    if user_score >= 4:
        print("🎉 Wow! You played perfectly.")
    elif user_score >= 2:
        print("👍 Good job, you played really well!")
    else:
        print("😅 Better luck next time!")

    print(f"Final Score ➤ You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")



if __name__ == '__main__':
    main()
        