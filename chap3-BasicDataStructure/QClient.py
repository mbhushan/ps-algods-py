from Queue import Queue


def testQueue():
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print ("Deq: ",  q.dequeue())
    while not q.is_empty():
        print (q.dequeue())


def main():
    testQueue()


if __name__ == '__main__':
    main()
