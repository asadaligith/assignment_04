
#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
#Anton is 21 years old.
#Beth is 6 years older than Anton.
#Chen is 20 years older than Beth.
#Drew is as old as Chen's age plus Anton's age.
#Ethan is the same age as Chen.
#Your code should store each person's age to a variable and print their names and ages at the end.
#The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this
#(the below numbers are made up -- your solution should have the correct values!):


def ages():
    Asad = 21
    Ali =  6 + Asad
    Raza = 20 + Ali
    Kashif = Raza + Asad
    Umer = Raza

    print("Hello freinds! Asad , Ali , Raza , Kashif, Umer are freinds of each other and their ages is below")

    print(f"Asad is {Asad} Years old")
    print(f"ALi is {Ali} Years old")
    print(f"Raza is {Raza} Years old")
    print(f"Kashif is {Kashif} Years old")
    print(f"Umer is {Umer} Years old")

ages()