from Stack import Stack


def testStackAPIs():
    stack = Stack()
    print ("stack is empty? {}".format(stack.is_empty()))
    stack.push(4)
    stack.push('dog')
    print (stack.peek())
    stack.push(True)
    print ("stack is empty? {}".format(stack.is_empty()))
    stack.push(8.4)
    print (stack.pop())
    print (stack.pop())
    print (stack.size())


def main():
    testStackAPIs()


if __name__ == '__main__':
    main()
