from Stack import Stack


def readInput():
    while True:
        num = input("Enter number: ")
        base = input("Enter base: ")
        num = num.strip()
        base = base.strip()
        if not num.isdigit() or not base.isdigit():
            print ("Bad input. Try again...")
            continue
        num = int(num)
        base = int(base)
        if base < 2 or base > 16:
            print ("Bad base value.")
            continue
        return num, base


def convertIntToStringBase(num, base):
    convString = "0123456789ABCDEF"
    stack = Stack()
    while num > 0:
        if num < base:
            stack.push(convString[num])
        else:
            stack.push(convString[num % base])
        num = num // base
    result = []
    while not stack.isEmpty():
        result.append(stack.pop())
    return ''.join(result)


def main():
    num, base = readInput()
    result = convertIntToStringBase(num, base)
    print ("Number: %d in Base: %d is: %s" % (num, base, result))


if __name__ == '__main__':
    main()
