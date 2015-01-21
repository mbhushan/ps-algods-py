from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.N = 0

    def pop(self, i=-1):
        """ Remove the item at the given position in the linked list,
        and return it.
        If no index is specified, a.pop() removes and returns the last item
        in the linked list."""
        if self.isEmpty():
            return None
        if i >= self.size():
            return None
        if (i + self.N) < 0:
            return None
        ind = i + self.N
        curr = self.head
        prev = None
        count = 0
        found = False
        while curr is not None:
            if count == ind:
                found = True
                break
            prev = curr
            curr = curr.next
            count += 1
        if found:
            node = curr.data
            if prev is None:
                self.head = self.head.next
            else:
                prev.next = curr.next
                curr.next = None
            self.N -= 1
            return node
        return None

    def index(self, x):
        """ return the index in the linked list of the first item
        whose value is x.
        Returns "None" if no such item in linked list """
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == x:
                return index
            curr = curr.next
            index += 1
        return None

    def append(self, data):
        """ add the data at the end of the linked list """
        node = Node(data)
        # If first node in the list then both head n tail should point to it
        if self.isEmpty():
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.N += 1

    def size(self):
        return self.N

    def isEmpty(self):
        return self.N == 0

    def __str__(self):
        sll = []
        curr = self.head
        while curr is not None:
            sll.append(curr.data)
            curr = curr.next
        print (sll)
