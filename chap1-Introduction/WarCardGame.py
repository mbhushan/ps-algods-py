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
    play(playerHand, compHand)


def play(player, computer):

    while True:
        battleCards = []
        compCard = computer.popCard()
        print ("Computer played: ", str(compCard))
        key = input ("press any key to play your turn, <n> key to abort: ")
        if key == 'n':
            return
        playerCard = player.popCard()
        print ("You played: ", str(playerCard))
        result = compCard.getRank() > playerCard.getRank()
        if compCard.getRank() > playerCard.getRank():
            print ("COMPUTER WON THIS HAND!!!")
            computer.addMultipleCards([compCard, playerCard])
        elif compCard.getRank() < playerCard.getRank():
            print ("Congrats! YOU WON THIS HAND!!!")
            player.addMultipleCards([compCard, playerCard])
        else:
            print ("Equal Cards - Done with game!")
            return


def main():
    playwar()


if __name__ == '__main__':
    main()

