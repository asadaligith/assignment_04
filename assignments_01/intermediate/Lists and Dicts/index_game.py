
# Index Game

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return "Element updated."
    else:
        return "Index out of range."

def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "Invalid indices."

def index_game():
    my_list = [10, 'apple', 42, 'banana', 99]
    print("Current List:", my_list)

    operation = input("Choose operation (access/modify/slice): ").lower()

    if operation == "access":
        idx = int(input("Enter index to access: "))
        print(access_element(my_list, idx))

    elif operation == "modify":
        idx = int(input("Enter index to modify: "))
        new_val = input("Enter new value: ")
        print(modify_element(my_list, idx, new_val))
        print("Updated List:", my_list)

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced List:", slice_list(my_list, start, end))

    else:
        print("Invalid operation.")

index_game()
