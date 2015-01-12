class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, data):
        self.items.append(data)

    def addRear(self, data):
        self.items.insert(0, data)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
