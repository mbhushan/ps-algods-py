from Stack import Stack


def decToBin(num):
    """ Given decimal number D > 0 as input - convert it to binary string """
    S = Stack()
    while num > 1:
        m = num % 2
        S.push(m)
        num = num//2
    S.push(num)
    L = []
    while not S.is_empty():
        L.append(S.pop())
    return ''.join([str(i) for i in L])


def readInput():
    while True:
        num = input("Enter decimal number: ")
        try:
            num = int(num)
            if (num <= 0):
                print ("Please enter postive number!")
                continue
            return num
        except ValueError:
            print ("Bad Input! Please try again..")


def main():
    decNum = readInput()
    binNum = decToBin(decNum)
    print ("{} in binary is: {}".format(decNum, binNum))

if __name__ == '__main__':
    main()
