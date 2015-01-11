from Queue import Queue


def hotPotato(players, num):
    simQ = Queue()
    for p in players:
        simQ.enqueue(p)

    while simQ.size() > 1:
        for i in range(num):
            simQ.enqueue(simQ.dequeue())
        simQ.dequeue()
    return simQ.dequeue()


def readInput():
    print ("Enter player names, comma separated")
    names = input()
    while True:
        num = input("Enter count: ")
        if num.isdigit():
            num = int(num)
            break
        else:
            print ("Bad Input. Please try again.")
    name_list = names.split(",")
    name_list = [n.strip() for n in name_list]
    return (name_list, num)


def main():
    players, num = readInput()
    winner = hotPotato(players, num)
    print ("Winner is: ", winner)


if __name__ == '__main__':
    main()
