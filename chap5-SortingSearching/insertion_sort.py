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


def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def main():
    minRange, maxRange, nums = readParams()
    nm = Numbers()
    numbers = nm.getNumbers(minRange, maxRange, nums)
    print ("Random generated %d numbers between %d and %d are: " %
           (nums, minRange, maxRange))
    print (numbers)
    sortedNums = insertionSort(numbers)
    print ("Sorted numbers are: ")
    print (sortedNums)


if __name__ == '__main__':
    main()
