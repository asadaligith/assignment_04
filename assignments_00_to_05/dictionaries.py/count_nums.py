
def get_user_number():
    user_number = []

    while True:
        user_input = input("Enter a Number: ")
        if user_input == "":
            break

        Num = int(user_input)
        user_number.append(Num)
    return user_number

def count_nums(num_lst):
    
    num_dict = {}
    for Num in num_lst:
        if Num not in num_dict:
            num_dict[Num] = 1
        else:
            num_dict[Num] += 1
    
    return num_dict


def print_counts(num_dict):
   
    for Num in num_dict:
        print(str(Num) + " appears " + str(num_dict[Num]) + " times.")



def main():
  
    user_number = get_user_number()
    num_dict = count_nums(user_number)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()    

