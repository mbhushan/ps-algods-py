import random


class Numbers:

    def __init__(self):
        self.num_list = []

    def getNumbers(self, minRange, maxRange, nums):
        if not isinstance(nums, int):
            print ("ERROR: Bad input - \"nums\"")
        elif not isinstance(minRange, int):
            print ("ERROR: Bad input - \"minRange\"")
        elif not isinstance(maxRange, int):
            print ("ERROR: Bad input - \"maxRange\"")
        elif minRange > maxRange:
            print ("ERROR: expected minRange < maxRange")

        else:
            for i in range(nums):
                data = random.randint(minRange, maxRange)
                self.num_list.append(data)
        return self.num_list
