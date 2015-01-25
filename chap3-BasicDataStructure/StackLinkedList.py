class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.N = 0

    def __str__(self):
        dataList = []
        curr = self.head
        while curr is not None:
            dataList.append(curr.data)
            curr = curr.next
        print (dataList)

    def pop(self):
        if self.isEmpty():
            print ("Stack is EMPTY!")
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        self.N -= 1
        return node

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.N += 1

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N
