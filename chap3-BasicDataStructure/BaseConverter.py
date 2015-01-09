from Stack import Stack


def baseConverter(decNum, base):
    """ Converts decimal number greater than ZERO to any base
    less than 16 and greater than 1"""
    digits = "0123456789ABCDEF"
    S = Stack()
    while decNum > 0:
        mod = decNum % base
        S.push(digits[mod])
        decNum = decNum // base

    L = []
    while not S.is_empty():
        L.append(S.pop())

    return ''.join(L)


def readInput():
    while True:
        num = input("Enter decimal number: ")
        try:
            decNum = int(num)
            if decNum < 0:
                print ("Enter number greater than ZERO.")
                continue
            break
        except ValueError:
            print ("Bad Input, Please try again..")
    while True:
        base = input("Enter base for decimal to convert: ")
        try:
            base = int(base)
            if base < 2 or base > 16:
                print ("Invalid base. Please enter between 2 & 16")
                continue
            break
        except ValueError:
            print ("Bad Input, Try again ...")
    return (decNum, base)


def main():
    decNum, base = readInput()
    result = baseConverter(decNum, base)
    print ("{} in base {} is: {}".format(decNum, base, result))


if __name__ == '__main__':
    main()
