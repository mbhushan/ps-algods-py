from Tokenizer import tokenizer
from Tokenizer import readInput
from ParenChecker import parenChecker
from InfixToPostfix import infixToPostfix
from PostfixEval import postfixEvaluator


def calculator():
    while True:
        expr = readInput()
        tokens = tokenizer(expr)
        parens = []
        for t in tokens:
            if t == '(' or t == ')':
                parens.append(t)
        if not parenChecker(''.join(parens)):
            print ("Parenthesis mismatch. Please try again..")
            continue

        if (tokens is not None) or (len(tokens) >= 1):
            postfix = infixToPostfix(tokens)
            print ("postfix: ", postfix)
            result = postfixEvaluator(postfix)
            print ("ANS: ", result)
        print ("press any key to continue, \'n\' to exit.")
        ch = input()
        if ch == 'n':
            break


def main():
    calculator()


if __name__ == '__main__':
    main()
