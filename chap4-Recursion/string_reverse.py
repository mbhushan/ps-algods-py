def readInput():
    string = input("Enter string: ")
    string = string.strip()
    return string


def reverseString(string):
    if len(string) == 1:
        return string
    return reverseString(string[1:]) + string[0]


def main():
    string = readInput()
    revstr = reverseString(string)
    print ("Reversed String: %s" % revstr)


if __name__ == '__main__':
    main()
