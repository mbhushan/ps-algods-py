

def findSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    return numlist[0] + findSum(numlist[1:])


def readInput():
    while True:
        print("Enter list of numbers comma spearated: ")
        numlist = input()
        numlist = numlist.strip()
        numlist = numlist.split(",")
        try:
            numlist = [int(n.strip()) for n in numlist]
            return numlist
        except:
            print ("Bad Input. Try Again..")
            continue


def main():
    numlist = readInput()
    ans = findSum(numlist)
    print ("Sum is: ", ans)


if __name__ == '__main__':
    main()
