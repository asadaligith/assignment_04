import random
import string

def password_generator(length_Pass):                                            # Function Password Genertor
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length_Pass))
    return password
    

def main():                             # Main Function 
    print("Password Generator")

    try:
        quantity_password = int(input("Enter How many Paswoord you want to Generate: "))  
        length_Pass = int(input("Enter the lenth of Password at least 8 character long: "))
        if length_Pass < 8:                # Conditions Password must be 8 Character long
            print("(Input is Less then 8!) Enter Must be at least 8 Character long ")  
            return
        
    except ValueError:                      # Handle Error if Given the rong Input
        print("Give me correct input!")

    print("Pasword Generated:")
    for i in range(quantity_password):          # Loop run according the quantity of User 
        pwd =password_generator(length_Pass)
        print(f"{i+1}. {pwd}")
    

if __name__ == '__main__':
    main()
    
    
    
