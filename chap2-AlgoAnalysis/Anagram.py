

def checkAnagram(s1, s2):
    if s1 is None or s2 is None:
        print ("One of the input string is Null")
        return False

    s1len = len(s1)
    s2len = len(s2)

    if s1len != s2len:
        return False

    s1_list = list(s1.lower())
    s2_list = list(s2.lower())

    s1_list.sort()
    s2_list.sort()

    for i in range(s1len):
        if s1_list[i] != s2_list[i]:
            return False
    return True


def readInput():
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    return (first.strip(), second.strip())


def main():
    s1, s2 = readInput()
    result = checkAnagram(s1, s2)
    print ("are \"{}\" and \"{}\" anagrams? -> {}".format(s1, s2, result))


if __name__ == '__main__':
    main()
