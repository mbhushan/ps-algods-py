from SLList import LinkedList


def testLinkedList():
    ll = LinkedList()
    while True:
        print ("Choose operation: ")
        print (" 1 - Append\n",
               "2 - Index\n",
               "3 - Pop\n",
               "4 - Search\n",
               "5 - Size\n",
               "6 - Exit\n")
        choice = input()
        if choice == '1':
            ll = addll(ll)
            ll.__str__()
        elif choice == '2':
            index(ll)
            ll.__str__()
        elif choice == '3':
            ll = pop(ll)
            # searchKey(ll)
            ll.__str__()
        elif choice == '4':
            ll = pop(ll)
            # searchKey(ll)
            ll.__str__()
        elif choice == '5':
            size(ll)
            ll.__str__()
        elif choice == '6':
            break
        else:
            print ("BAD Choice! Choose from 1 to 4 numbers")


def pop(ll):
    print ("Enter index to be popped: ")
    index = input()
    data = ll.pop(index)
    if data is None:
        print ("No data found for index: ", index)
    else:
        print("Popped: ", data)


def index(ll):
    print ("Enter data for which index needs to be found: ")
    data = input()
    ind = ll.index(data)
    if ind is not None:
        print ("Index is: ", ind)
    else:
        print ("Data NOT FOUND!")


def addll(ll):
    print ("Enter data: ")
    data = input()
    ll.append(data)
    return ll


def removell(ll):
    print ("Data to remove: ")
    data = input()
    result = ll.remove(data)
    if result:
        print("REMOVED: ", data)
    else:
        print("Not Found in linked list!")


def searchKey(ll):
    print ("Enter data to be searched: ")
    data = input()
    result = ll.search(data)
    if result:
        print ("FOUND!")
    else:
        print ("Not Found!")


def size(ll):
    print("Size: ", ll.size())


def main():
    testLinkedList()

if __name__ == '__main__':
    main()
