from Numbers import Numbers
import random


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


def quickSort(A):
    if len(A) <= 1:
        return A
    less = []
    more = []
    pivot = random.choice(A)
    for a in A:
        if a < pivot:
            less.append(a)
        if a > pivot:
            more.append(a)
    less = quickSort(less)
    more = quickSort(more)
    return less + [pivot] * A.count(pivot) + more


def main():
    minRange, maxRange, nums = readParams()
    nm = Numbers()
    numbers = nm.getNumbers(minRange, maxRange, nums)
    print ("Random generated %d numbers between %d and %d are: " %
           (nums, minRange, maxRange))
    print (numbers)
    sortedNums = quickSort(numbers)
    print ("Sorted numbers are: ")
    print (sortedNums)

if __name__ == '__main__':
    main()
