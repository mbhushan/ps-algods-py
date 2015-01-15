from Stack import Stack
from ParenChecker import parenChecker


def infixToPostfix(tokenList):
    opStack = Stack()
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    postfixList = []
    # tokenList = list(infix.split(" "))
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


def validateInput(expr):
    if not expr:
        return False
    expr = expr.strip()

    parenList = []
    for e in expr:
        if e == '(' or e == ')':
            parenList.append(e)
    parenExpr = ''.join(parenList)
    if not parenChecker(parenExpr):
        return False
    tokenList = expr.split(" ")
    sanitizedTokList = []
    for t in tokenList:
        t = t.strip()
        sanitizedTokList.append(t)
        if t.isdigit():
            continue
        elif t == '+' or t == '-' or t == '/' or t == '*' or t == '^':
            continue
        elif t == '(' or t == ')':
            continue
        else:
            return False
    return sanitizedTokList


def readInput():
    print ("Enter infix expression with space.")
    infix = input("infix expression: ")
    tokList = validateInput(infix)
    while not tokList:
        print ("Bad Input! Please enter valid infix expression")
        print ("Enter infix expression with space.")
        infix = input("infix expression: ")

    return tokList


def main():
    infix = readInput()
    postfix = infixToPostfix(infix)
    print ("Postfix expression: ", postfix)


if __name__ == '__main__':
    main()
