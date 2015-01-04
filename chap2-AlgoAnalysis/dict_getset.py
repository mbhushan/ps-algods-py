import timeit

D = {}


def timeDictSetFn(n):
    global D
    for i in range(n):
        D[i] = i


def timeDictGetFn(n):
    global D
    for i in range(n):
        x = D[i]


def main():

    k = 10
    print ("Lets check the dict set times: ")
    for n in range(100000, 1000001, 100000):
        setTime = timeit.Timer("timeDictSetFn("+str(n)+")",
                               "from __main__ import timeDictSetFn")
        sit = setTime.timeit(k)
        print ("Time for {} dict inserts: {}".format(n, sit))
        print ("Time for {} dict inserts: {}".format(1, sit/float(k*n)))

    print ("Now lets check the dict get times: ")
    for n in range(100000, 1000001, 100000):
        setTime = timeit.Timer("timeDictSetFn("+str(n)+")",
                               "from __main__ import timeDictSetFn")
        getTime = timeit.Timer("timeDictGetFn("+str(n)+")",
                               "from __main__ import timeDictGetFn")
        git = getTime.timeit(k)
        print ("Time for {} dict gets: {}".format(n, git))
        print ("Time for {} dict gets: {}".format(1, git/float(k*n)))

if __name__ == '__main__':
    main()
