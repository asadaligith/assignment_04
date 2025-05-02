
def multiple_repeat(massage, repeat):
    for i in range(repeat):
        print(massage)

def main():
    massage = input("Enter a Massage: ")
    repeat = int(input("How many time do you want to repeat: "))
    multiple_repeat(massage, repeat)



if __name__ == '__main__':
    main()