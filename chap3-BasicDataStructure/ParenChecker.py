from Stack import Stack


def parenChecker(paren):
    """ This method checks if the parenthesis is balanced or not.
    Example could be:
        ()(), (()), (())() are all balanced.
        ((), ((()()) are not balanced """
    S = Stack()
    balanced = True
    index = 0
    while index < len(paren):
        if paren[index] == '(':
            S.push(paren[index])
        else:
            if S.is_empty():
                balanced = False
                break
            else:
                S.pop()
        index += 1
    if not S.is_empty():
        balanced = False
    return balanced


def readInput():
    while True:
        flag = True
        paren = input("Enter parenthesis string: ")
        for i in range(len(paren)):
            if paren[i] != '(' and paren[i] != ')':
                print ("Bad Input. Please try again..")
                flag = False
                break
        if flag:
            break
    return paren


def main():
    paren = readInput()
    print ("Parenthesis string: ", paren)
    print ("Are parenthesis balanced: ", parenChecker(paren))


if __name__ == '__main__':
    main()
