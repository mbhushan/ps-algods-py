from Fraction import Fraction
from gcd import readInt


def readFraction():
    n = readInt('numerator')
    d = readInt('denominator')
    return Fraction(n, d)


def testFractionMultiplication(x, y):
    return x * y


def testFractionAddition(x, y):
    ans = x + y
    return ans


def testFractionEquality(x, y):
    return x == y


def testFractionDivision(x, y):
    return x / y


def testFractionSubtraction(x, y):
    return x - y


def testFractionGreaterThan(x, y):
    return x > y


def testFractionLessThan(x, y):
    return x < y


def main():
    print ("Enter first fraction values")
    x = readFraction()
    print ("Enter second fraction values")
    y = readFraction()
    ans = testFractionAddition(x, y)
    print ("sum of {} and {}: {}".format(x, y, ans))
    ans = testFractionEquality(x, y)
    print ("Are {} and {} equal? {}".format(x, y, ans))

    ans = testFractionMultiplication(x, y)
    print ("multiplication of {} and {} is: {}".format(x, y, ans))

    ans = testFractionDivision(x, y)
    print ("Division of {}  and {} is: {}".format(x, y, ans))

    ans = testFractionSubtraction(x, y)
    print ("Subtract {} and {} equal to: {}".format(x, y, ans))

    ans = testFractionGreaterThan(x, y)
    print ("Is {} greater than {}: {}".format(x, y, ans))

    ans = testFractionLessThan(x, y)
    print ("Is {} less than {}: {}".format(x, y, ans))

    # #1 testing solution for programming exercise 1 from 1.7 module of chap1
    print ("Numerator of first fraction: {}".format(x.get_num()))
    print ("Denominator of first fraction: {}".format(x.get_den()))


if __name__ == '__main__':
    main()
