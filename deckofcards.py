# Build a deck of cards with Object-Orientated Programming.
import random


# A class Card contains a suit and value
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print(self.value + ' of ' + self.suit)

    def toStr(self):
        return self.value + ' of ' + self.suit


# A class Deck contains 52 cards of 4 suits from Ace to King when initialize
class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        values = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                  'King']
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        for s in suits:
            for v in values:
                self.cards.append(Card(v, s))

    # Return the number of cards remaining in the Deck
    def num_of_cards(self):
        return len(self.cards)

    # Show all the card that it has
    def showDeck(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    # To draw a card from the deck, it will then remove the last card from the top of the deck
    def drawCard(self):
        return self.cards.pop()


# Begin of the task
deck = Deck()
deck.shuffle()
# deck.showDeck()

# return two random cards
cards = []
for i in range(2):
    cards.append(deck.drawCard().toStr())
print(', '.join(cards))
