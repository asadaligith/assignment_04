
def main():
    print("Enter the Number and see is double ")
    curr_val = int(input("Enter a Number: "))

    while True :
        double = curr_val * 2   # Value is doubled
        if double > 100:        # Conditions 
            break
        print(f"{curr_val} doubled is {double}")
        curr_val = double       # Update current values


if __name__ == '__main__':
    main()