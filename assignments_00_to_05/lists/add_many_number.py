# Write a function that takes a list of numbers and returns the sum of those numbers

def add_many_numbers(numbers):
    sum_of_total_numbers = 0
    for number in numbers:
        sum_of_total_numbers += number
    return sum_of_total_numbers


def main():
    numbers = [10, 25, 65, 14, 88, 105, 250, 97, 180, 72]
    sum_numbers = add_many_numbers(numbers)
    print(sum_numbers)

if __name__ == '__main__':
    main()
