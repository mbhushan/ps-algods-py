from Queue import Queue
import random


def hotPotato(players):
    if players is None or len(players) <= 1:
        return players

    simQ = Queue()
    plsize = len(players)
    for p in players:
        simQ.enqueue(p)

    while simQ.size() > 1:
        r = random.randint(plsize, plsize*2)
        for i in range(r):
            simQ.enqueue(simQ.dequeue())
        simQ.dequeue()
    return simQ.dequeue()


def readInput():
    print ("Enter player names, comma separated")
    names = input()
#    while True:
#        num = input("Enter count: ")
#        if num.isdigit():
#            num = int(num)
#            break
#        else:
#            print ("Bad Input. Please try again.")
    name_list = names.split(",")
    name_list = [n.strip() for n in name_list]
    return (name_list)


def main():
    players = readInput()
    winner = hotPotato(players)
    print ("Winner is: ", winner)


if __name__ == '__main__':
    main()
