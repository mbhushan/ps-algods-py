from Stack import Stack


def infixToPostfix(infix):
    opStack = Stack()
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    tokenList = list(infix.split(" "))
    charTokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numTokens = "1234567890"

    print ("token list: ", tokenList)
    for token in tokenList:
        if token in charTokens or token in numTokens or token.isdigit():
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

    return ' '.join(postfixList)


def readInput():
    print ("Enter infix expression with space.")
    infix = input("infix expression: ")
    # validate expr?
    return infix


def main():
    infix = readInput()
    postfix = infixToPostfix(infix)
    print ("Postfix expression: ", postfix)


if __name__ == '__main__':
    main()
