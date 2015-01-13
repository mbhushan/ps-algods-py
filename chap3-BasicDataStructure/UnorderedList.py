from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while not (current is None):
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        while not (current is None):
            if current.getData() == data:
                return True
            current = current.getNext()
        return False

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
