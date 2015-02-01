

def readInput():
    print ("Enter space separated data: ")
    nlist = input()
    nlist = nlist.strip()
    nums = nlist.split(" ")
    nlist = [int(n) for n in nums]
    return nlist


def readSearchKey():
    while True:
        key = input("Enter search key: ")
        if isinstance(key, int):
            return key
        if not key.isdigit():
            continue
        key = int(key)
        return key


def binarySearch(numList, key):
    if numList is None or len(numList) < 1:
        return False
    low = 0
    high = len(numList) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if numList[mid] == key:
            return True
        elif key < numList[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def main():
    numList = readInput()
    numListSorted = sorted(numList)
    while True:
        key = readSearchKey()
        result = binarySearch(numListSorted, key)
        print ("Key: %d in the list: %s" % (key, result))
        print (numListSorted)

if __name__ == '__main__':
    main()
