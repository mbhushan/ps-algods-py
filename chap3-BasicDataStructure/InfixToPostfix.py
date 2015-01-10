from Stack import Stack


def infixToPostfix(infix):
    opStack = Stack()
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    tokenList = list(infix.replace(" ", ""))
    charTokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numTokens = "1234567890"

    print ("token list: ", tokenList)
    for token in tokenList:
        if token in charTokens or token in numTokens:
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.is_empty():
        postfixList.append(opStack.pop())

    return ''.join(postfixList)


def readInput():
    infix = input("Enter valid infix expression: ")
    # validate expr?
    return infix


def main():
    infix = readInput()
    postfix = infixToPostfix(infix)
    print ("Postfix expression: ", postfix)


if __name__ == '__main__':
    main()
