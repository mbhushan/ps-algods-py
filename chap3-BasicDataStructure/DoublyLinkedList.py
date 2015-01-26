
class Node:

    def __init__(self, data):
        self.data = data
        self.front = None
        self.back = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.N = 0

    def __str__(self):
        dlList = []
        curr = self.head
        count = 0
        while count < self.N:
            dlList.append(curr.data)
            curr = curr.front
            count += 1
        print (dlList)

    def insert(self, data, index):
        if index < 0 or index > self.N:
            print ("Bad index!")
            return False

        node = Node(data)

        # check if first node in DLL
        if self.head is None:
            self.head = node
            self.head.front = self.head
            self.head.back = self.head
        else:
            count = 0
            curr = self.head
            while (count < index):
                curr = curr.front
                count += 1
            node.back = curr
            node.front = curr.front
            curr.front.back = node
            curr.front = node
        self.N += 1
        return True

    def addFront(self, data):
        node = Node(data)
        if self.isEmpty():
            node.front = node
            node.back = node
            self.head = node
        else:
            node.front = self.head
            node.back = self.head.back
            self.head.back.front = node
            self.head.back = node
            self.head = node
        self.N += 1

    def addRear(self, data):
        node = Node(data)
        if self.isEmpty():
            node.front = node
            node.back = node
            self.head = node
        else:
            node.back = self.head.back
            node.front = self.head
            self.head.back.front = node
            self.head.back = node
        self.N += 1

    def size(self):
        return self.N

    def isEmpty(self):
        return self.N == 0
