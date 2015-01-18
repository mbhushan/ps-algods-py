from Queue import Queue


def radixSort(nums):
    if nums is None or len(nums) < 1:
        return nums
    mainQ = Queue()
    binQs = []
    for n in nums:
        mainQ.enqueue(n)
    for i in range(10):
        binQs.append(Queue())
    maxLen = len(nums[0])
    for i in range(1, len(nums)):
        if len(nums[i]) > maxLen:
            maxLen = len(nums[i])
    for i in range(1, maxLen+1):
        visited = []
        while not mainQ.is_empty():
            val = mainQ.dequeue()
            if i > len(val):
                visited.append(val)
                continue
            r = val[-i]
            r = int(r)
            binQs[r].enqueue(val)
        for v in visited:
            mainQ.enqueue(v)
        for i in range(10):
            while not binQs[i].is_empty():
                mainQ.enqueue(binQs[i].dequeue())
    result = []
    while not mainQ.is_empty():
        result.append(mainQ.dequeue())
    return result


def readInput():
    while True:
        print ("Enter comma separated numbers: ")
        data = input()
        data = data.split(",")
        try:
            nums = [d.strip() for d in data]
            break
        except ValueError:
            print ("Bad input, plz try again..")
    return nums


def printData(nums):
    if nums is None or len(nums) < 1:
        print ("EMPTY LIST - Nothing to print!")
    else:
        for n in nums:
            print (n, end=" ")
    print()


def main():
    nums = readInput()
    nums = radixSort(nums)
    print ("After applying radix sort: ")
    printData(nums)


if __name__ == '__main__':
    main()
