
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:

    def __init__(self):
        self.head = None
        self.tail = None
        self.N = 0

    def __str__(self):
        plist = []
        curr = self.head
        while curr is not None:
            plist.append(curr.data)
            curr = curr.next
        print (plist)

    def addFront(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head
        self.N += 1

    def removeFront(self):
        if self.isEmpty():
            print ("Deque is Empty!")
            return None
        node = self.head
        self.head = self.head.next
        node.next = None
        if self.head is None:
            self.tail = None
        self.N -= 1
        return node

    def addRear(self, data):
        node = Node(data)
        if self.isEmpty():
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.N += 1

    def removeRear(self):
        if self.isEmpty():
            print ("Deque is Empty!")
            return None
        # check if size is 1
        if self.size() == 1:
            node = self.tail
            self.tail = None
            self.head = None
            self.N -= 1
            return node
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        node = curr.next
        self.tail = curr
        self.tail.next = None
        self.N -= 1
        return node

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N
