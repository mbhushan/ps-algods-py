from hash import hash


class HashTable:

    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    def printHashTable(self):
        for index in range(len(self.slots)):
            key = self.slots[index]
            value = self.data[index]
            print ("%d: %s:%s" % (index, key, value))

    def showSlots(self):
        print (self.slots)

    def showData(self):
        print (self.data)

    def hash_function(self, key, size):
        return hash(key, size)

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        index = start_slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                data = self.data[index]
                break
            else:
                index = self.rehash(index, len(self.slots))
                if index == start_slot:
                    break
        return data

    def put(self, key, data):
        hashVal = self.hash_function(key, len(self.slots))

        if self.slots[hashVal] is None:
            self.slots[hashVal] = key
            self.data[hashVal] = data
        elif self.slots[hashVal] == key:
            self.data[hashVal] = data   # replace
        else:
            next_slot = self.rehash(hashVal, len(self.slots))
            while self.slots[next_slot] is not None and \
                    self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data     # replace
