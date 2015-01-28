

def factorialRec(num):
    if num <= 1:
        return 1
    return num * factorialRec(num-1)


def readInput():
    while True:
        num = input("Enter number: ")
        num = num.strip()
        if num.isdigit():
            num = int(num)
            return num
        else:
            print ("Bad Input. Try again..")


def main():
    num = readInput()
    fact = factorialRec(num)
    print ("Factorial of %d is: %d" % (num, fact))


if __name__ == '__main__':
    main()
