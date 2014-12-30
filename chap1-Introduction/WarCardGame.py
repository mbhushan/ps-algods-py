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


def nowPlay(player, computer):
    while True:
        tableCards = []
        compCards = computerPlay(computer)
        if compCards is None:
            print ("You terminated the Game!")
            return
        elif len(compCards) == 0:
            print ("YOU WON!! COngratulations :)")
            return
        tableCards.extend(compCards)
        showPlayedCards(compCards, "Computer")

        playerCards = playerPlay(player)

        if playerCards is None:
            print ("You terminated the Game!")
            return
        elif len(playerCards) == 0:
            print ("Computer Won!! Congrats to her :)")
            return
        tableCards.extend(playerCards)
        showPlayedCards(playerCards, "You")

        result = compareCards(compCards, playerCards)
        if result == 1:
            computer.addMultipleCards(tableCards)
        elif result == 2:
            player.addMultipleCards(tableCards)
        elif result == 4:
            print ("Computer Won!! Congrats to her :)")
            return
        elif result == 5:
            print ("YOU WON!! COngratulations :)")
            return
        elif result == 3:
            while True:
                print ("EQUAL Cards - Now each player will put 2 cards on table\
                   - One face down and one face up. Player having high face up\
                   card would win the hand and take all the cards on the \
                   table.")

                compCards = computerPlay(computer)
                if compCards is None:
                    print ("You terminated the Game!")
                    return
                elif len(compCards) == 0:
                    print ("YOU WON!! COngratulations :)")
                    return
                tableCards.extend(compCards)
                showPlayedCards(compCards, "Computer")

                playerCards = playerPlay(player)
                if playerCards is None:
                    print ("You terminated the Game!")
                    return
                elif len(playerCards) == 0:
                    print ("Computer Won!! Congrats to her :)")
                    return
                showPlayedCards(playerCards, "You")
                tableCards.extend(playerCards)

                result = compareCards(compCards, playerCards)

                if result == 1:
                    computer.addMultipleCards(tableCards)
                    break
                elif result == 2:
                    player.addMultipleCards(tableCards)
                    break
                elif result == 4:
                    print ("Computer Won!! Congrats to her :)")
                    return
                elif result == 5:
                    print ("YOU WON!! COngratulations :)")
                    return


def main():
    playwar()


if __name__ == '__main__':
    main()
