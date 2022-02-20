# syntax=docker/dockerfile:1

FROM python:3.8

ADD deckofcards.py .

CMD [ "python3", "./deckofcards.py"]
