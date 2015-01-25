from StackLinkedList import Stack


def testStackAPIs():
    stack = Stack()
    while True:
        print ("Choose Operation\n",
               "1 - Push(data)\n",
               "2 - Pop()\n",
               "3 - Size()\n",
               "4 - Exit()")
        choice = input("Choice: ")
        if choice == '1':
            stack = pushStack(stack)
            stack.__str__()
        elif choice == '2':
            stack = popStack(stack)
            stack.__str__()
        elif choice == '3':
            stackSize(stack)
            stack.__str__()
        elif choice == '4':
            break
        else:
            print ("Bad Choice. Please choose a valid operation")
            continue


def stackSize(stack):
    size = stack.size()
    print("Stack Size: ", size)


def pushStack(stack):
    data = input("Enter data: ")
    stack.push(data)
    return stack


def popStack(stack):
    node = stack.pop()
    if node is not None:
        print ("Popped: ", node.data)
    else:
        print ("Popped: ", node)
    return stack


def main():
    testStackAPIs()

if __name__ == '__main__':
    main()
