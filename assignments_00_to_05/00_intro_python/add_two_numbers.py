
#Problem Statement
#Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
#Prompt the user to enter the second number.
#Read the input and convert it to an integer.
#Calculate the sum of the two numbers.
#Print the total sum with an appropriate message.
#The provided solution demonstrates a working implementation of this problem, 
# where the main() function guides the user through the process of entering two numbers and displays their sum.

#Start 
print("Give Two Numbers and Check Their Sum")

def main():
    prompt_1 = input("Enter a number: ")
    prompt_1 = int(prompt_1)

    prompt_2 = input("Enter a second number: ")
    prompt_2 = int(prompt_2)

    total = prompt_1 + prompt_2

    print(f"The sum is {prompt_1} + {prompt_2} = {total}")
    print(type(prompt_1))
    print(type(prompt_2))

main()