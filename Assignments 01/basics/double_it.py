
def double_it():

    try:
        current_value = int(input("Enter a Number to double it: "))

        while current_value < 100:
            curr_val = current_value * 2
            print(f"{current_value} double {curr_val}")
            current_value = curr_val


    except ValueError:
        print("Invalid Input! Enter a Valid NUmber: ")


if __name__ == '__main__':
    double_it()

        