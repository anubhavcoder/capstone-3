from card import Card
from src.deck import Deck
from termcolor import colored


test = Deck()

test.draw(n=2)

Card.print_pretty_cards(test.draw(n=2))