
def get_first_element(lst):
    # Print the first element of the list
    print("The first element is:", lst[0])

# Prompt user to input the number of elements
n = int(input("How many elements do you want to enter? "))

user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

get_first_element(user_list)
