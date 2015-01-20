from LinkedList import LinkedList


def testLinkedList():
    ll = LinkedList()
    while True:
        print ("Choose operation: ")
        print (" 1 - Add\n",
               "2 - Remove\n",
               "3 - Search\n",
               "4 - Size\n",
               "5 - Exit\n")
        choice = input()
        if choice == '1':
            ll = addll(ll)
            ll.__str__()
        elif choice == '2':
            ll == removell(ll)
            ll.__str__()
        elif choice == '3':
            searchKey(ll)
            ll.__str__()
        elif choice == '4':
            size(ll)
            ll.__str__()
        elif choice == '5':
            break
        else:
            print ("BAD Choice! Choose from 1 to 4 numbers")


def addll(ll):
    print ("Enter data: ")
    data = input()
    ll.add(data)
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
