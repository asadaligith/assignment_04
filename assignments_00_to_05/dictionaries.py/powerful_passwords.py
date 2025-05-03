from hashlib import sha256

stored_logins = {}

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def sign_up(email, password):
    if email in stored_logins:
        print(f"email already registered")
        return False
    stored_logins[email] = hash_password(password)
    print("Login Successfully")
    return True


def login(email, password):
    if email not in stored_logins:
        print("Email not found!")
        return False
    if stored_logins[email] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False


def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            sign_up(email, password)
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login(email, password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()