#Write a program that continually reads in mass from the user and then outputs the equivalent energy 
#using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
#E = m * c**2

C = 299792458  # Speed of light in meters per second

def main():
    while True :
        user_input = input("Enter kilos of mass (or type 'exit' to stop): ")
        
        if user_input.lower() == "exit":
            print("Exited ")
            break

        try:
            user_mass = float(user_input)
            if user_mass < 0:
                print("Please enter a valid positive mass.")
                continue

            energy = user_mass * (C ** 2)
            print(f"\n m = {user_mass} kg")
            print(f"C = {C} m/s")
            print(f"E = {energy} joules of energy!\n")

        except ValueError:
            print("Invalid input! Enter a Valid Input (or type 'exit' to Stop)")

if __name__ == '__main__':
    main()