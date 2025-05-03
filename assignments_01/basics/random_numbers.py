import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print("\nGet 10 Random Numbers\n")
    for _ in range(N_NUMBERS):
        gen_numbers : int = random.randint(MIN_VALUE,MAX_VALUE)
        print(gen_numbers, end=" ")


if __name__ == '__main__':
    main()