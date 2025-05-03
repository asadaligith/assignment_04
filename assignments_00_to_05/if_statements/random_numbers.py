

import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    Number_lst = []

    for _ in range(N_NUMBERS):
        Numbers = random.randint(MIN_VALUE,MAX_VALUE)
        Number_lst.append(Numbers)

    print(Number_lst)


if __name__ == '__main__':
    main()