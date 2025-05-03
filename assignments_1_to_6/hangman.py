import random
import string

words = ["python", "streamlit", "hangman", "dictionary", "function", "loop", "variable", "code"]

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left. Used letters:", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_list))

        # User input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Correct!")
            else:
                lives -= 1
                print("❌ Incorrect. That letter is not in the word.")


        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter. Try another one.")
        else:
            print("⚠️ Invalid character. Please enter a valid letter.")

    # Game over conditions
    if lives == 0:
        print("\n💀 You lost! The word was", word)
    else:
        print("\n🎉 You guessed the word:", word, "— You win!")

# Run the game
hangman()