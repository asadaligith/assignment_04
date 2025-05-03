import time

def main():                     # main function
    for i in range(10,0,-1):    # for loop for iteration
        print(f"Time left: {i}  " , end="\r")
        time.sleep(1)
    print("LiftOff          ")



if __name__ == '__main__':
    main()