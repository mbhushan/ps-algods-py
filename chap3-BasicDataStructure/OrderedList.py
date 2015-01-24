from Node import Node


class OrderedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        ol = []
        curr = self.head
        while curr is not None:
            ol.append(curr.data)
            curr = curr.next
        print (ol)

    def isEmpty(self):
        return self.head is None

    def popPos(self, key):
        if self.isEmpty():
            print ("List is EMPTY!")
            return False
        front = self.head
        prev = None
        count = 0
        node = None
        found = False
        while front is not None:
            if count == key:
                found = True
                break
            count += 1
            prev = front
            front = front.next
        if not found:
            return node

        if prev is None:
            node = self.head
            self.head = self.head.next
        else:
            node = front
            prev.next = front.next
            front.next = None
        return node

    def pop(self):
        if self.isEmpty():
            print ("List is EMPTY!")
            return None

        # check if the list has single node
        if self.head.next is None:
            node = self.head
            self.head = None
            return node

        front = self.head
        back = None
        while front.next is not None:
            back = front
            front = front.next
        node = front
        back.next = front.next
        return node

    def search(self, key):
        if self.isEmpty():
            print ("List is EMPTY!")
            return -1
        current = self.head
        index = 0

        while not (current is None):
            if current.getData() == key:
                return index
            elif key < current.getData():
                break
            current = current.getNext()
            index += 1
        return -1

    def size(self):
        current = self.head
        count = 0
        while not (current is None):
            count += 1
            current = current.getNext()
        return count

    def add(self, data):
        current = self.head
        prev = None
        while not (current is None):
            if current.getData() > data:
                break
            else:
                prev = current
                current = current.getNext()
        temp = Node(data)
        if prev is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)

    def remove(self, data):
        if self.isEmpty():
            print ("List is EMPTY!")
            return None
        current = self.head
        prev = None
        found = False

        while not found:
            if current.getData() == data:
                found = True
            else:
                prev = current
                current = current.getNext()
        node = None
        if prev is None:
            node = self.head
            self.head = current.getNext()
        else:
            node = current
            prev.setNext(current.getNext())
        return node
