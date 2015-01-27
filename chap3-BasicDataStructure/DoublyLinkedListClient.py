from DoublyLinkedList import DoublyLinkedList


def testDoublyLinkedList():
    dll = DoublyLinkedList()
    while True:
        print("Choose Operations:\n",
              "1 - addFront(data)\n",
              "2 - addRear(data)\n",
              "3 - insert(data, index)\n",
              "4 - removeFront()\n",
              "5 - removeRear()\n",
              "6 - remove(index)\n",
              "7 - search(key)\n",
              "8 - size()\n",
              "9 - exit()")
        choice = input("Enter Choice: ")
        if choice == '1':
            dll = addFront(dll)
            dll.__str__()
        elif choice == '2':
            dll = addRear(dll)
            dll.__str__()
        elif choice == '3':
            dll = insertDLL(dll)
            dll.__str__()
        elif choice == '4':
            dll = removeFront(dll)
            dll.__str__()
        elif choice == '5':
            dll = removeRear(dll)
            dll.__str__()
        elif choice == '6':
            dll = removeIndex(dll)
            dll.__str__()
        elif choice == '7':
            search(dll)
            dll.__str__()
        elif choice == '8':
            dll.__str__()
            print ("Doubly Linked List Size: ", dll.size())
        elif choice == '9':
            break
        else:
            print ("Bad Choice. Choose valid operation!")
            continue


def search(dll):
    key = input("Enter search key: ")
    index = dll.search(key)
    if index >= 0:
        print ("Key: %s -> found at index: %d" % (key, index))
    else:
        print ("Key: %s -> Not Found in list" % key)


def removeIndex(dll):
    index = input("Enter index: ")
    index = index.strip()
    if not index.isdigit():
        print ("Bad Index Value")
        return dll
    index = int(index)
    node = dll.removeIndex(index)
    if node:
        print ("Removed: ", node.data)
    else:
        print ("Remove Failed!")
    return dll


def removeRear(dll):
    node = dll.removeRear()
    if node:
        print ("Removed: ", node.data)
    else:
        print ("Rear remove failed!")
    return dll


def removeFront(dll):
    node = dll.removeFront()
    if node:
        print ("Removed: ", node.data)
    else:
        print ("Front Remove Failed!")
    return dll


def insertDLL(dll):
    data = input("Enter data: ")
    index = input("Enter index for data insert: ")
    index = index.strip()
    if not index.isdigit():
        print ("Bad Index Data.. aborting insert")
        return dll
    index = int(index)
    result = dll.insert(data, index)
    if result:
        print ("Insert successful!")
    else:
        print ("Insert FAILED!")
    return dll


def addRear(dll):
    data = input("Enter data: ")
    dll.addRear(data)
    return dll


def addFront(dll):
    data = input("Enter data: ")
    dll.addFront(data)
    return dll


def main():
    testDoublyLinkedList()


if __name__ == '__main__':
    main()
