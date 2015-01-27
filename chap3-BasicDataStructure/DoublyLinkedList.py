
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

    def search(self, key):
        if self.isEmpty():
            print ("List is Empty")
            return -1
        index = 0
        found = False
        curr = self.head
        while index < self.N:
            if curr.data == key:
                found = True
                break
            index += 1
            curr = curr.front
        if found:
            return index
        return -1

    def removeIndex(self, index):
        if self.isEmpty():
            print ("List is Empty!")
            return None
        if index < 0:
            index = index + self.N

        if (index < 0) or (index > (self.N - 1)):
            print ("Bad index value.. exiting")
            return None

        count = 0
        curr = self.head
        while count < index:
            count += 1
            curr = curr.front
        curr.front.back = curr.back
        curr.back.front = curr.front
        if index == 0:
            self.head = self.head.front
        curr.front = None
        curr.back = None
        self.N -= 1
        return curr

    def removeRear(self):
        if self.isEmpty():
            print ("list is empty!")
            return None
        node = self.head.back
        self.head.back.back.front = self.head
        self.head.back = self.head.back.back
        node.front = None
        node.back = None
        self.N -= 1
        return node

    def removeFront(self):
        if self.isEmpty():
            print ("list is empty!")
            return None
        node = self.head
        self.head.front.back = self.head.back
        self.head.back.front = self.head.front
        self.head = self.head.front
        node.front = None
        node.back = None
        self.N -= 1
        return node

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
            while (count < index-1):
                curr = curr.front
                count += 1
            node.back = curr
            node.front = curr.front
            curr.front.back = node
            curr.front = node
            if index == 0:
                self.head = node
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
