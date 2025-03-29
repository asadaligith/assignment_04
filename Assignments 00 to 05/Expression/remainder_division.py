
def remainder_division():
    try:
        print("\nDivided Two Number and Get result with remainder\n")

        divided = int(input("Enter 1st integer Number to be Divided: "))
        divisor = int(input("Enter 2nd integer Number by Division: "))

        if divisor == 0:  
            print("Error! Division by zero is not allowed.")  
            return 

        result = divided // divisor 
        reminder = divided % divisor
 
        print(f"The Division result is {result} with a reminder {reminder}")

    except ValueError:
        print("Invalid Input! Enter a Valid Number")


if __name__ == '__main__':
    remainder_division()