def create_story():
    # Starting sentence
    sentence = "Learning Python is an exciting journey where"

    # Collecting user inputs
    adjective = input("Please type an adjective and press enter: ")  # Example: smart
    noun = input("Please type a noun and press enter: ")  # Example: robot
    verb = input("Please type a verb and press enter: ")  # Example: solve

    # Constructing the final story sentence
    story = f"{sentence} I taught my {adjective} {noun} how to {verb} with code!"

    # Print the final story
    print(story)

if __name__ == "__main__":
    create_story()
