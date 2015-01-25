from DequeLinkedList import Deque


def testDeque():
    dq = Deque()
    while True:
        print ("Choose Operation\n",
               "1 - AddFront(data)\n",
               "2 - RemoveFront()\n",
               "3 - AddRear(data)\n",
               "4 - RemoveRear()\n",
               "5 - Size()\n",
               "6 - Exit()")
        choice = input("Enter choice: ")
        if choice == '1':
            dq = addFront(dq)
            dq.__str__()
        elif choice == '2':
            dq = removeFront(dq)
            dq.__str__()
        elif choice == '3':
            dq = addRear(dq)
            dq.__str__()
        elif choice == '4':
            dq = removeRear(dq)
            dq.__str__()
        elif choice == '5':
            dequeSize(dq)
            dq.__str__()
        elif choice == '6':
            break
        else:
            print ("Bad Choice - please choose valid operation")
            continue


def dequeSize(deque):
    print ("Deque Size: ", deque.size())


def removeRear(deque):
    node = deque.removeRear()
    if node:
        print ("Removed: ", node.data)
    else:
        print ("Removed: ", node)
    return deque


def addRear(deque):
    data = input("Enter data: ")
    deque.addRear(data)
    return deque


def removeFront(deque):
    node = deque.removeFront()
    if node is not None:
        print ("Removed: ", node.data)
    else:
        print ("Removed: ", node)
    return deque


def addFront(deque):
    data = input("Enter data: ")
    deque.addFront(data)
    return deque


def main():
    testDeque()

if __name__ == '__main__':
    main()
