from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.N = 0

    def __str__(self):
        llist = []
        curr = self.head
        while curr is not None:
            llist.append(curr.data)
            curr = curr.next
        print (llist)

    def search(self, key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def add(self, ndata):
        node = Node(ndata)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.N += 1

    def remove(self, ndata):
        curr = self.head
        prev = None
        found = False
        while curr is not None:
            if curr.data == ndata:
                found = True
                break
            else:
                prev = curr
                curr = curr.next
        if found:
            if prev is None:
                self.head = self.head.next
            else:
                prev.next = curr.next
                curr.next = None
            self.N -= 1
        return found

    def size(self):
        return self.N

    def isEmtpy(self):
        return self.N == 0
