

def readInput():
    while True:
        num = input("Enter number: ")
        num = num.strip()
        if not num.isdigit():
            print ("Bad Input. Try again..")
            continue
        num = int(num)
        base = input("Enter base <less than 16>: ")
        if not base.isdigit() or int(base.strip()) > 16:
            print ("Bad base input. Plz try again..")
            continue
        return (num, int(base.strip()))


def toString(num, base):
    convertStr = "0123456789ABCDEF"
    if num < base:
        return convertStr[num]
    else:
        return toString(num // base, base) + convertStr[num % base]


def main():
    num, base = readInput()
    ans = toString(num, base)
    print ("number:%d in base:%d is: %s" % (num, base, ans))


if __name__ == '__main__':
    main()
