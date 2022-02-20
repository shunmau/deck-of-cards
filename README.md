# deck-of-cards

This project will build a deck of cards system with Python.

Deliverables:
1) To create a deck of cards including the faces, 52 cards in total
2) Shuffle the cards.
3) Return two random cards each time the program is run, there is no state that persists between runs.
4) The output look something like this: Two of Hearts, Jack of Diamonds

To begin with, I have created two class, one is a class "Card" contains suit and value, another is a class "Deck" contains 52 cards of 4 suits from Ace to King.
Then I start with initialize an attribute called cards and append with 52 cards in the create method to create our deck.
I also created a shuffle method to randomly reorder the cards in the deck.
Finally I return two random cards each time the program is run.


A public docker image in Github Package Storage is created. Just run:
```
docker pull ghcr.io/shunmau/deckofcards:latest

docker run ghcr.io/shunmau/deckofcards:latest
```
The output should look something like this: Two of Hearts, Jack of Diamonds


We should always run the program in an UAT system first before running in a production system. And to run the prograam in a production system, we should keep logging the activities and write to log file each time the program run, as well as logging any error message. Regularly doing health check is also very important to avoid any problem occur.

I haven't add any test case yet as I am not quite familiar with writing test case and can't think of how to test my code and run them through github actions.
