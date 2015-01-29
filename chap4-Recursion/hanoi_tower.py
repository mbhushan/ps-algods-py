

def readInput():
    while True:
        disks = input("Enter number of disks: ")
        disks = disks.strip()
        if not disks.isdigit():
            print ("Bad input! Try again..")
            continue
        disks = int(disks)
        return disks


def towerOfHanoi(disks):
    moveTower(disks, "A", "B", "C")


def moveTower(height, src, dest, via):
    if height >= 1:
        moveTower(height - 1, src, via, dest)
        moveDisk(src, dest)
        moveTower(height - 1, via, dest, src)


def moveDisk(src, dest):
    print ("Moving disk from: %s to %s" % (src, dest))


def main():
    disks = readInput()
    towerOfHanoi(disks)


if __name__ == '__main__':
    main()
