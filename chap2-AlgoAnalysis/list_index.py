import random
import timeit

testList = list(range(10000))
k = 10000
def verifyListIndexOrderOne(testList, n):
    # testList = list(range(n))
    # n = len(testList)
    for i in range(k):
        index = random.randint(0, k-1)
        testList[index]


def main():
    # verifyListIndexOrderOne(1000000)
    for n in range(1000000, 10000001, 1000000):
        testList = list(range(n))
        indexTime = timeit.Timer("verifyListIndexOrderOne(testList,"+str(n)+")",
                                 "from __main__ import testList,\
                                 verifyListIndexOrderOne")
        it = indexTime.timeit(number=1)
        print ("TOTAL TIME for %d index access in %d list of"\
               "numbers :%15.9f seconds" % (k, n, it))


if __name__ == '__main__':
    main()
