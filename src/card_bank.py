from random import shuffle, choice
from card import Card

class BankError(Exception):
  pass

"""Represents a card bank"""
class CardBank(object):

  DECK = [(i%3, 13 if i%13==0 else i%13) for i in range(1,53)]

  def __init__(self, num_decks):
    """
    Initializes the card bank object with num_decks decks
    """
    deck = [Card(tup) for tup in self.DECK]
    self.decks = deck*num_decks

  def __len__(self):
    return len(self.decks)

  def is_empty(self):
    """
    Checks if the bank is empty
    """
    if len(self.decks) < 1:
        return True
    else:
        return False

  def shuffle_bank(self):
    """
    Shuffles the cards in the bank
    """
    shuffle(self.decks)

  def take_card(self):
    """
    Take card from the top of the bank
    """
    if self.is_empty():
      raise BankError("Cannot retrieve a card from an empty deck")

    return self.decks.pop(0)

  def add_card(self, card):
    """
    Add card to the end of the bank
    """
    if isinstance(card, Card):
      return self.decks.append(card)
    else:
      raise TypeError("card must be a Card object")