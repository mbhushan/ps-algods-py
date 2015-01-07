from Stack import Stack


def readInput():
    st = input("Enter String: ")
    return st


def reverseString(st):
    s = Stack()
    stLen = len(st)
    for i in range(stLen):
        s.push(st[i])

    outStr = []
    for i in range(stLen):
        outStr.append(s.pop())

    rev = ''.join(outStr)
    return rev


def main():
    st = readInput()
    rev_st = reverseString(st)
    print ("reversed string: %s" % rev_st)


if __name__ == '__main__':
    main()
