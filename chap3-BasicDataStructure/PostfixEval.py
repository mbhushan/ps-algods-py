from Stack import Stack


def postfixEvaluator(pfix):
    pfixList = pfix.split(" ")
    opStack = Stack()

    for tok in pfixList:
        if tok.isdigit():
            opStack.push(int(tok))
        else:
            if opStack.size() < 2:
                print ("Invalid postfix expression")
                return None
            second = opStack.pop()
            first = opStack.pop()
            ans = doMath(tok, first, second)
            if ans is None:
                return ans
            opStack.push(ans)
    return opStack.pop()


def doMath(operator, x, y):
    if operator == '*':
        return (x * y)
    elif operator == "+":
        return (x + y)
    elif operator == '-':
        return (x - y)
    elif operator == "/":
        if y == 0:
            return None
        return (float(x)/y)
    return None


def readInput():
    print ("Enter postfix expression separated by space.")
    pfix = input("Expression: ")
    return pfix


def main():
    postfix = readInput()
    result = postfixEvaluator(postfix)
    print("Result: ", result)


if __name__ == '__main__':
    main()
