import timeit


def testList():
    pop_zero = timeit.Timer("popZero()", "from __main__ import popZero")
    pop_end = timeit.Timer("popEnd()", "from __main__ import popEnd")

    print("pop(0) pop()")
    pt = pop_end.timeit(number=1000)
    pz = pop_zero.timeit(number=1000)
    print("POP ZERO: %15.5f" % (pz))
    print("POP  END: %15.5f" % (pt))


def popZero():
    i = 10000
    x = list(range(i))
    # while len(x) > 0:
    for j in range(i):
        x.pop(0)


def popEnd():
    i = 10000
    x = list(range(i))
    # while len(x) > 0:
    for j in range(i):
        x.pop()


def main():
    testList()


if __name__ == '__main__':
    main()
