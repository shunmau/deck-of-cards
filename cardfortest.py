import random

values = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
deck = [v + ' of ' + s for s in suits for v in values]
random.shuffle(deck)
print(', '.join(deck[:2]))