import time


def sumOfN(n):
    start = time.time()

    sumN = 0
    for i in range(1, n+1):
        sumN += i
    end = time.time()

    return (sumN, end-start)


def sumOfNFast(n):
    start = time.time()
    nSum = (n*(n+1))/2
    end = time.time()

    return (nSum, end-start)


def main():
    # n = int(input("Enter integer n: "))

    testNums = [10000, 100000, 1000000, 10000000]

    for n in testNums:
        nSum, ttime = sumOfN(n)
        print ("Summation of %d numbers is %d taking %10.7f seconds"
               % (n, nSum, ttime))
        nSum, ttime = sumOfNFast(n)
        print ("Fast Summation of %d numbers is %d taking %10.7f seconds"
               % (n, nSum, ttime))


if __name__ == '__main__':
    main()
