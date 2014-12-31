from Deck import Deck
from Deck import Hand


def playwar():
    deck = Deck()
    deck.shuffle()
    n = deck.size()
    playerHand = Hand()
    compHand = Hand()

    deck.moveCards(playerHand, (n//2))
    deck.moveCards(compHand, (n//2))
    # playerHand.sort()
    # compHand.sort()
    print ("Cards in computer hand: ")
    print(compHand)
    print("Cards in player hands: ")
    print(playerHand)
    nowPlay(playerHand, compHand)


def computerPlay(compDeck, n=1):
    key = input("Computer turn, any key for play: <n> to abort game:")
    if key == 'n':
        return None
    cards = []
    if compDeck.size() < n:
        return cards
    for i in range(n):
        cards.append(compDeck.popCard())
    return cards


def playerPlay(playerDeck, n=1):
    key = input("Player turn, any key for play: <n> to abort game:")
    if key == 'n':
        return None
    cards = []
    if playerDeck.size() < n:
        return cards
    for i in range(n):
        cards.append(playerDeck.popCard())
    return cards


def compareCards(computer, player):
    """ Assumes computer and player are list of cards
    here we compare the topmost card of each computer and player
    Return:
        1 - if computer wins the hand
        2 - if player wins the hand
        3 - Tie
        4 - computer wins the game.
        5 - player wins the game.
        if one of them has less card left than the other then they loose and
        other wins the game.
    """
    clen = len(computer)
    plen = len(player)
    if clen == plen:
        if computer[clen-1].getRank() > player[plen-1].getRank():
            return 1
        elif computer[clen-1].getRank() < player[plen-1].getRank():
            return 2
        else:
            return 3
    elif clen > plen:
        return 4
    else:
        return 5


def showPlayedCards(cards, subject):
    print (subject + " played: ")
    for card in cards:
        print (str(card))


def applyResults(computer, player, tableCards, result):
    if result == 1:
        print("Computer Won Hand! :)")
        computer.addMultipleCards(tableCards)
    elif result == 2:
        print("You Won Hand! :)")
        player.addMultipleCards(tableCards)
    elif result == 4:
        print ("Computer Won the Game!! Congrats to her :)")
        return None
    elif result == 5:
        print ("YOU WON the Game!! COngratulations :)")
        return None
    return (computer, player)


def checkCompCards(compCards):
    if compCards is None:
        print ("You terminated the Game!")
        return 0
    elif len(compCards) == 0:
        print ("YOU WON!! COngratulations :)")
        return 0
    else:
        return 1


def checkPlayerCards(playerCards):
    if playerCards is None:
        print ("You terminated the Game!")
        return 0
    elif len(playerCards) == 0:
        print ("Computer Won!! Congrats to her :)")
        return 0
    else:
        return 1


def nowPlay(player, computer):
    result = 0
    while True:
        if result == 3:
            n = 2
            print ("EQUAL Cards in Rank - Now each player will put 2 cards\n" +
                   "on table. One face down and one face up. Player having\n" +
                   "high face up card would win the hand and take all the\n"
                   + "cards on the table.")
        else:
            n = 1
            tableCards = []
        compCards = computerPlay(computer, n)
        check = checkCompCards(compCards)
        if check == 0:
            return
        tableCards.extend(compCards)
        showPlayedCards(compCards, "Computer")

        playerCards = playerPlay(player, n)
        check = checkPlayerCards(playerCards)
        if check == 0:
            return

        tableCards.extend(playerCards)
        showPlayedCards(playerCards, "You")

        result = compareCards(compCards, playerCards)
        if result != 3:
            result = applyResults(computer, player, tableCards, result)
            if result is not None:
                computer, player = result
                result = 0
            else:
                return


def main():
    playwar()


if __name__ == '__main__':
    main()
