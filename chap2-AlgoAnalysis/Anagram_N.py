def checkAnagram(s1, s2):
    if s1 is None or s2 is None:
        return False

    s1len = len(s1)
    s2len = len(s2)

    if s1len != s2len:
        return False

    s1_list = list(s1.lower())
    s2_list = list(s2.lower())

    s1_map = {}
    s2_map = {}

    # Get the unique chars from s1
    char_set = set([])

    # create a map of char -> count for s1
    for i in s1_list:
        count = 0
        if i in s1_map:
            count = s1_map[i]
        s1_map[i] = (count + 1)
        char_set.add(i)

    # create a map of char -> count for s2
    for j in s2_list:
        count = 0
        if j in s2_map:
            count = s2_map[j]
        s2_map[j] = (count + 1)

    # check if chars in s1 have the same count as in s2 string.
    for c in char_set:
        if c not in s2_map:
            return False
        if s1_map[c] != s2_map[c]:
            return False
    # Every condition pertaining to anagrams holds true - so lets return True :)
    return True


def readInput():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    return (s1.strip(), s2.strip())


def main():
    s1, s2 = readInput()
    ans = checkAnagram(s1, s2)
    print ("Are \"{}\" and \"{}\" anagrams? -> {}".format(s1, s2, ans))


if __name__ == '__main__':
    main()
