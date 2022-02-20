import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print(self.value + ' of ' + self.suit)

    def toStr(self):
        return self.value + ' of ' + self.suit


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

    def num_of_cards(self):
        return len(self.cards)

    def showDeck(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()


deck = Deck()
deck.shuffle()
#deck.showDeck()

cards = []
for i in range(2):
    cards.append(deck.drawCard().toStr())

print(', '.join(cards))
