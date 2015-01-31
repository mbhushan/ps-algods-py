

def readInput():
    while True:
        row = input("Number of rows in pascal triangle: ")
        if isinstance(row, int):
            return row
        if not row.isdigit():
            print ("Bad Input. Try again..")
            continue
        row = int(row)
        if row < 1:
            print ("Bad Input, please enter positive integer")
            continue
        return row


def printPascalTriangle(nrow):
    printRow([1], nrow)
    pascalTriangle(nrow-1, [1])


def pascalTriangle(nrow, rlist):
    if nrow == 0:
        return
    tmp_row = []
    tmp_row.append(rlist[0])
    for i in range(0, len(rlist)-1):
        # print (rlist)
        tmp_row.append(rlist[i] + rlist[i+1])
    tmp_row.append(rlist[-1])
    printRow(tmp_row, nrow)
    pascalTriangle(nrow-1, tmp_row)


def printRow(rowData, numRow):
    prefix = "  " * numRow
    print (prefix),
    for data in rowData:
        print ("%d  " % data),
    else:
        print


def main():
    nrow = readInput()
    printPascalTriangle(nrow)


if __name__ == '__main__':
    main()
