from Numbers import Numbers


def readParams():
    while True:
        minRange = input("Enter min range: ")
        maxRange = input("Enter max range: ")
        nums = input("Enter total numbers to be generated: ")
        if isinstance(minRange, int) and isinstance(maxRange, int) \
                and isinstance(nums, int):
            return minRange, maxRange, nums
        elif minRange.isdigit() and maxRange.isdigit() and nums.isdigit():
            minRange = int(minRange)
            maxRange = int(maxRange)
            nums = int(nums)
            return minRange, maxRange, nums
        else:
            print ("Bad Input. Please try again..")


def bubbleSort(A):
    exchange = True
    numPass = len(A) - 1
    while numPass > 0 and exchange:
        exchange = False
        for i in range(numPass):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                exchange = True
        numPass -= 1
    return A


def main():
    minRange, maxRange, nums = readParams()
    nm = Numbers()
    numbers = nm.getNumbers(minRange, maxRange, nums)
    print ("Random generated %d numbers between %d and %d are: " %
           (nums, minRange, maxRange))
    print (numbers)
    sortedNums = bubbleSort(numbers)
    print ("Sorted numbers are: ")
    print (sortedNums)


if __name__ == '__main__':
    main()
