from Stack import Stack


def checkBalancedSymbol(string):
    """ complete parenthesis checker for [,{,(,),},]
    <><>{}([]), (({})), ()[]<>[] are all valid strings.
    <>(({}), {}<>> are not """
    S = Stack()
    index = 0
    balanced = True
    slen = len(string)
    while index < slen:
        if string[index] in "{[(<":
            S.push(string[index])
        else:
            if S.is_empty() or (not checkMatch(S.peek(), string[index])):
                balanced = False
                break
            else:
                S.pop()
        index += 1
    if not S.is_empty():
        balanced = False
    return balanced


def checkMatch(open, close):
    if close == ')' and open == '(':
        return True
    elif close == '}' and open == '{':
        return True
    elif close == ']' and open == '[':
        return True
    elif close == '>' and open == '<':
        return True
    return False


def readInput():
    while True:
        found = True
        symStr = input("Enter String: ")
        for s in symStr:
            if s not in "{([<>])}":
                found = False
                print ("Invalid String. Please try again...")
                break
        if found:
            break
    return symStr


def main():
    symStr = readInput()
    print ("Symbol String: ", symStr)
    print ("Are symbols in string balanced: ", checkBalancedSymbol(symStr))


if __name__ == '__main__':
    main()
