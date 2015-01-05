import timeit


# D = {i: i for i in range(100000)}
D = {}
# L = [j for j in range(100000)]
L = []
n = 100000


def main():
    for n in range(100000, 1000001, 100000):
        print ("Executing %d deletes on dict" % (n))
        dictDel = timeit.Timer("""
                               D = {i: i for i in range(n)}
                               for i in range(n):
                                   del D[i]
                               """,
                               "from __main__ import D, n")
        ddit = dictDel.timeit(1)
        print ("Dict del time per operation: %12.12f secs" % (ddit/float(n)))
    print ("\n")
    for n in range(100000, 1000001, 100000):
        print ("Executing %d deletes on list" % (n))
        listDel = timeit.Timer("""
                               L = [i for i in range(n)]
                               for i in range(n-1):
                                   del L[0]
                               """,
                               "from __main__ import L, n")
        ldit = listDel.timeit(1)
        print ("List Del Time per operation: %12.12f secs" % (ldit/float(n)))


if __name__ == '__main__':
    main()
