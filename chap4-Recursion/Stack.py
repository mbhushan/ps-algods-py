

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[self.size - 1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
