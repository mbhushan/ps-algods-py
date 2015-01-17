from QueueLinkedList import Queue


def testQueueLinkedList():
    Q = Queue()
    while True:
        print ("Choose operation: ")
        print (" 1 - Enqueue\n",
               "2 - Dequeue\n",
               "3 - Size\n",
               "4 - Exit\n")
        choice = input()
        if choice == '1':
            Q = enqueue(Q)
        elif choice == '2':
            Q = dequeue(Q)
        elif choice == '3':
            getSize(Q)
        elif choice == '4':
            break
        else:
            print ("BAD Choice! Choose from 1 to 4 numbers")


def dequeue(Q):
    if not Q.isEmpty():
        node = Q.dequeue()
        print ("Dequeued: ", node.data)
        Q.qprint()
    else:
        print ("Queue is EMPTY!")
    return Q


def getSize(Q):
    size = Q.size()
    print ("Size of Queue: ", size)


def enqueue(Q):
    data = input("Data to be enqueued: ")
    if (data is not None) or len(data) > 0:
        Q.enqueue(data)
        Q.qprint()
    else:
        print ("Bad data. Plz try again..")
    return Q


def main():
    testQueueLinkedList()


if __name__ == '__main__':
    main()
