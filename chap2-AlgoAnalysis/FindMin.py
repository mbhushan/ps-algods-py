

def findMinN2(nums):
    if nums is None or len(nums) < 1:
        return None
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                # tmp = nums[i]
                # nums[i] = nums[j]
                # nums[j] = tmp
                nums[i], nums[j] = nums[j], nums[i]
    return nums[0]


def findMinFast(nums):
    if nums is None or len(nums) < 1:
        return None
    minN = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < minN:
            minN = nums[i]
    return minN


def readInput():
    print ("Enter list of numbers - comma separated: ")
    inp = input()
    st = inp.split(",")
    return [int(s.strip()) for s in st]


def main():
    inp = readInput()
    minN = findMinN2(inp)
    print ("Minimum(O(n^2)) is: {}".format(minN))
    minN = findMinFast(inp)
    print ("Minimum(O(n)) is: {}".format(minN))


if __name__ == '__main__':
    main()
