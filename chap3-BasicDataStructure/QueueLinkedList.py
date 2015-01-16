from QNode import Node


class Queue:

    def __init__(self):
        self.front = None
        self.back = None
        self.N = 0

    def add(self, data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
            self.back = self.front
        else:
            self.back.setNext(temp)
            self.back = self.back.next
        self.N += 1

    def isEmpty(self):
        return self.N == 0

    def size(self):
        return self.N
