from SLList import LinkedList


def testLinkedList():
    ll = LinkedList()
    while True:
        print ("Choose operation: ")
        print (" 1 - Append\n",
               "2 - Index\n",
               "3 - Pop\n",
               "4 - Search\n",
               "5 - Insert\n",
               "6 - Size\n",
               "7 - Exit\n")
        choice = input()
        if choice == '1':
            ll = addll(ll)
            ll.__str__()
        elif choice == '2':
            index(ll)
            ll.__str__()
        elif choice == '3':
            ll = pop(ll)
            ll.__str__()
        elif choice == '4':
            searchKey(ll)
            ll.__str__()
        elif choice == '5':
            insert(ll)
            ll.__str__()
        elif choice == '6':
            size(ll)
            ll.__str__()
        elif choice == '7':
            break
        else:
            print ("BAD Choice! Choose from 1 to 4 numbers")


def insert(ll):
    print ("Enter data to be inserted: ")
    data = input()
    print ("Index at which data to be inserted: ")
    index = input()
    index = index.strip()
    if not index.isdigit():
        print ("Bad Index!")
    index = int(index)
    if index < 0 or index > ll.size():
        print ("Index out of range!")
    ll.insert(data, index)
    return ll


def pop(ll):
    print ("Enter index to be popped: ")
    index = input()
    index = index.strip()
    try:
        index = int(index)
    except:
        print ("Bad Input for Index")
        return ll
    data = ll.pop(index)
    if data is None:
        print ("No data found for index: ", index)
    else:
        print("Popped: ", data)
    return ll


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


def searchKey(ll):
    print ("Enter data to be searched: ")
    data = input()
    result = ll.search(data)
    if result >= 0:
        print ("FOUND at index: ", result)
    else:
        print ("Not Found!")


def size(ll):
    print("Size: ", ll.size())


def main():
    testLinkedList()

if __name__ == '__main__':
    main()
