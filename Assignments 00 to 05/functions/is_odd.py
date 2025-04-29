
def main():
    for i in range(10, 20):
        if isodd(i):
            print(f"{i} Odd")
        else:
            print(f"{i} even")


def isodd(value : int):
    reminder = value % 2
    return reminder == 1


if __name__ == '__main__':
    main()