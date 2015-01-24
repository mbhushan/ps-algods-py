from OrderedList import OrderedList


def testOrderedList():
    ol = OrderedList()
    while True:
        print ("Choose operation: ")
        print (" 1 - Add(data)\n",
               "2 - Pop()\n",
               "3 - Search(key)\n",
               "4 - Remove(data)\n",
               "5 - Size()\n",
               "6 - Pop(pos)\n",
               "7 - exit()\n",
               )
        choice = input()
        if choice == '1':
            ol = add(ol)
            ol.__str__()
        elif choice == '2':
            ol = pop(ol)
            ol.__str__()
        elif choice == '3':
            search(ol)
            ol.__str__()
        elif choice == '4':
            ol = remove(ol)
            ol.__str__()
        elif choice == '5':
            print ("Size of list: %d" % ol.size())
            ol.__str__()
        elif choice == '6':
            ol = popPos(ol)
            ol.__str__()
        elif choice == '7':
            break
        else:
            print ("Bad Choice - choose from valid options")


def remove(ol):
    data = input("Enter data to be removed: ")
    node = ol.remove(data)
    if node:
        print ("Removed: ", node.data)
    else:
        print ("Data: %s NOT FOUND in the list" % data)
    return ol


def search(ol):
    key = input("Enter search key: ")
    index = ol.search(key)
    if index < 0:
        print ("Key: %s NOT FOUND!" % key)
    else:
        print ("Key: %s Found at index: %d" % (key, index))


def popPos(ol):
    key = input("Enter position to be popped: ")
    key = key.strip()
    if not key.isdigit():
        print ("Bad position data")
        return ol
    key = int(key)
    node = ol.popPos(key)
    if node:
        print ("Popped: ", node.data)
    else:
        print ("Popped: None")
    return ol


def pop(ol):
    node = ol.pop()
    if node:
        print ("Popped: ", node.data)
    else:
        print ("Popped: None")
    return ol


def add(ol):
    data = input("Enter data to be added: ")
    ol.add(data)
    return ol


def main():
    testOrderedList()

if __name__ == '__main__':
    main()
