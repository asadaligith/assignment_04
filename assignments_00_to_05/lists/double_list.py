# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def main():
    numbers = [5,6,8,2,3]
    print(f"\nThis is numbers List: {numbers}\n")

    for i in range(len(numbers)):
        doubles_numbers = numbers[i] * 2
        numbers[i] = doubles_numbers
    print("\nList is double")
    print(numbers)



if __name__ == '__main__':
    main()