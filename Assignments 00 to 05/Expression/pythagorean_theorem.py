import math

def calculate_hypotenuse():
    print("\nCalculate the Hypotenuse of a Right Triangle\n")
    
    try:
        ab = float(input("Enter the length of AB: "))
        ac = float(input("Enter the length of AC: "))
        
        if ab <= 0 or ac <= 0:
            print("Lengths must be positive numbers!")
            return
        
        bc = math.sqrt(ab ** 2 + ac ** 2)
        print(f"\nThe length of BC (the hypotenuse) is: {bc:.2f}\n")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculate_hypotenuse()
