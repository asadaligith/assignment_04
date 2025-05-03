import time

print("Countdown Timer")
def countdown():
    try:
        user_input = int(input("Enter Times in Seconds: "))
        if user_input <= 0:
            print("Please enter a positive number!")
            return

        while user_input > 0:
            print(f"Time Left: {user_input} Seconds ", end="\r")
            time.sleep(1)
            user_input -=1
        print("\rTimes Up!           ")

    except ValueError:
        print("Invalid input! Enter Valid Number")

if __name__ == '__main__':
    countdown()