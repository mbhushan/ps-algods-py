def tokenizer(expr):
    if expr is None:
        return None
    expr = expr.strip()
    tokenList = []
    accum = []
    for t in expr:
        if t.isdigit():
            accum.append(t)
            continue
        elif len(accum) > 0:
            tokenList.append(''.join(accum))
            accum = []
        if t == '+' or t == '-' or t == '/' or t == '*' or t == '^':
            tokenList.append(t)
        elif t == '(' or t == ')':
            tokenList.append(t)
    if len(accum) > 0:
        tokenList.append(''.join(accum))
    return tokenList


def readInput():
    print ("Enter expression for calculator: ")
    expr = input()
    return expr


def main():
    expr = readInput()
    tknList = tokenizer(expr)
    print ("TokenList: ", tknList)


if __name__ == '__main__':
    main()
