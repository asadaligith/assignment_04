"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
"""

def square_number():
    try:
        user_input = int(input("Type a number to see its square: "))
        square = user_input ** 2
        print(f"{user_input} squared is {square}")

    except ValueError:
        print("Invalid input! Enter a Number")

square_number()