from Fraction import Fraction
from gcd import readInt


def readFraction():
    n = readInt('numerator')
    d = readInt('denominator')
    return Fraction(n, d)


def testFractionAddition(x, y):
    ans = x + y
    return ans


def testFractionEquality(x, y):
    return x == y


def main():
    print ("Enter first fraction values")
    x = readFraction()
    print ("Enter second fraction values")
    y = readFraction()
    ans = testFractionAddition(x, y)
    print ("sum of {} and {}: {}".format(x, y, ans))
    ans = testFractionEquality(x, y)
    print ("Are {} and {} equal? {}".format(x, y, ans))


if __name__ == '__main__':
    main()
