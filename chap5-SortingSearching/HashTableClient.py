from HashTable import HashTable


def testHashTable():
    ht = HashTable()
    while True:
        print ("choose Operation: \n",
               "1 - Set Item\n",
               "2 - Get Item\n",
               "3 - GetKeys\n",
               "4 - Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            ht = setItem(ht)
            ht.printHashTable()
        elif choice == '2':
            getItem(ht)
            ht.printHashTable()
        elif choice == '3':
            ht.showSlots()
        elif choice == '4':
            break
        else:
            print ("Bad Choice - Choose Valid Operation")
            continue


def getItem(ht):
    key = input("Enter key: ")
    value = ht.get(key)
    if value:
        print ("%s: %s" % (key, value))
    else:
        print ("No value found corresponding to key: %s" % key)


def setItem(ht):
    key = input("Enter key: ")
    data = input("Enter data: ")
    ht.put(key, data)
    return ht


def main():
    testHashTable()

if __name__ == '__main__':
    main()
