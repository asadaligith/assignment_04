
def feet_to_inches():
    print("\nConvert Feet to Inches\n")
    try:
        user_input = float(input("Enter a Feet Number to convert in Inches: "))  
        inches = user_input * 12
        print(f"{user_input} Feet is {inches} Inches")

    except ValueError:
        print("Invalid Input! Please enter a valid number.")

feet_to_inches()
