

def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(f"You Enter {count} Even Numbers")
    


def get_int_lst():
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_int_lst()
    count_even(lst)


if __name__ == '__main__':
    main()