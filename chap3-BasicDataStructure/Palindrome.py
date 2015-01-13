from Deque import Deque


def isPalindrome(word):
    if word is None:
        return False
    if len(word) <= 1:
        return True

    DQ = Deque()
    for w in word:
        DQ.addRear(w)

    while (DQ.size() > 1):
        front = DQ.removeFront()
        rear = DQ.removeRear()
        if front != rear:
            return False
    return True


def readInput():
    inp = input("Enter string: ")
    return inp


def main():
    word = readInput()
    print ("Is \"{}\" a palindrome: {}".format(word, isPalindrome(word)))


if __name__ == '__main__':
    main()
