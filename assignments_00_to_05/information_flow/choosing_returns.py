
ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    


def main():
    print("(Entered age is an adult age)")
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    print()
    print("(Entered age is not an adult age)")
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))


if __name__ == "__main__":
    main()