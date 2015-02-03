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


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result


def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    result = list(merge(left, right))
    return result


def main():
    minRange, maxRange, nums = readParams()
    nm = Numbers()
    numbers = nm.getNumbers(minRange, maxRange, nums)
    print ("Random generated %d numbers between %d and %d are: " %
           (nums, minRange, maxRange))
    print (numbers)
    sortedNums = merge_sort(numbers)
    print ("Sorted numbers are: ")
    print (sortedNums)


if __name__ == '__main__':
    main()
