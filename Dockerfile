# syntax=docker/dockerfile:1

FROM python:3.8

LABEL org.opencontainers.image.source="https://github.com/shunmau/deck-of-cards"

ADD deckofcards.py .

CMD [ "python3", "./deckofcards.py"]
