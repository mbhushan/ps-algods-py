from QueueADT import Queue
import datetime as dt
import time


def testQueueADT():
    Q = Queue()
    times = []
    NUMS = [1000, 10000, 100000, 1000000]
    for N in NUMS:
        Q = Queue()
        start = dt.datetime.now()
        for i in range(N):
            Q.enqueue(i)
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds*1000)/N
        print ("Enqueue for %d items: %d" % (1000, elapsed))

    print ("==================================================")
    times = []
    for N in NUMS:
        Q = Queue()
        for i in range(N):
            Q.enqueue(i)
        start = dt.datetime.now()
        for i in range(N):
            Q.dequeue()
        end = dt.datetime.now()
        elapsed = ((end - start).microseconds*1000)/N
        print ("Dequeue for %d items: %d" % (1000, elapsed))


def main():
    testQueueADT()

if __name__ == '__main__':
    main()
