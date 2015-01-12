import random
from Printer import Printer
from Task import Task
from Queue import Queue


def simulation(numSeconds, pagePerMin):
    labPrinter = Printer(pagePerMin)
    printQ = Queue()
    waitTime = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQ.enqueue(task)

        if (not labPrinter.busy()) and (not printQ.is_empty()):
            nextTask = printQ.dequeue()
            waitTime.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()
    avgWait = sum(waitTime)/len(waitTime)
    print ("Avg wait: %6.2f secs, Tasks remaining: %3d"
           % (avgWait, printQ.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def readInput():
    while True:
        pagerate = input("Please enter page rate: ")
        if pagerate.isdigit():
            return int(pagerate)
        else:
            print ("Bad Input! Try again..")


def main():
    pagerate = readInput()
    for i in range(10):
        # simulating for 1 hour with input pagerate
        simulation(3600, pagerate)

if __name__ == '__main__':
    main()
