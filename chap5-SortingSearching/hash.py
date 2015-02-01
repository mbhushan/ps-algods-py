

def readTableSize():
    while True:
        tsize = input("Enter table size: ")
        if isinstance(tsize, int):
            return tsize
        tsize = tsize.strip()
        if not tsize.isdigit():
            print ("Bad table size - please input integer values")
            continue
        tsize = int(tsize)
        return tsize


def readString():
    string = input("Enter string: ")
    string = string.strip()
    return string


def hash(string, tableSize):
    totalSum = 0
    for index in range(len(string)):
        totalSum += ord(string[index])
    # print ("Total Ordinal Sum: ", totalSum)
    return totalSum % tableSize


def hashWeighted(string, tableSize):
    totalSum = 0
    for index in range(len(string)):
        totalSum += ord(string[index])*(index+1)
    return totalSum % tableSize


def main():
    string = readString()
    tableSize = readTableSize()
    hashVal = hash(string, tableSize)
    wtdHashVal = hashWeighted(string, tableSize)
    print ("Hash Value: %s" % hashVal)
    print ("Hash Weighted Value: %s" % wtdHashVal)


if __name__ == '__main__':
    main()
