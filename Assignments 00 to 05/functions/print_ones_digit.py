def ones_digit(num):
    print("The ones digit is", num % 10)



def main():
    num = int(input("Enter a Number: "))
    ones_digit(num)

if __name__ == '__main__':
    main()