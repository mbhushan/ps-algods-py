from Node import Node


class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def search(self, key):
        current = self.head

        while not (current is None):
            if current.getData() == key:
                return True
            elif key < current.getData():
                return False
            current = current.getNext()
        return False

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
        current = self.head
        prev = None
        found = False

        while not found:
            if current.getData() == data:
                found = True
            else:
                prev = current
                current = current.getNext()
        if prev is None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
