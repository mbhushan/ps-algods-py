from InfixToPostfix import infixToPostfix
from InfixToPostfix import readInput
from PostfixEval import postfixEvaluator


def infixCalc(infixExpr):
    postfix = infixToPostfix(infixExpr)
    print ("Postfix: ", postfix)
    ans = postfixEvaluator(postfix)
    return ans


def main():
    infixExpr = readInput()
    ans = infixCalc(infixExpr)
    print ("Result: ", ans)


if __name__ == '__main__':
    main()
