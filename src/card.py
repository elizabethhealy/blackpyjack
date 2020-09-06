
"""Represents a playing card"""
class Card(object):
  ACE_LOW=1
  ACE_HIGH=11
  FACE=10
  def __init__(self, suit_rank):
    """
    Initializes the card object
    suit_rank_tup: a tuple of integers representing suit and rank
    """
    self.suit = suit_rank[0]
    self.rank = suit_rank[1]
    self.name, self.values = self._translate_card()
    self.image_path = ""
    self.image_obj = None

  def __eq__(self, other):
    return self.rank == other.rank and self.suit == other.suit

  def __lt__(self, other):
    return self.rank < other.rank

  def __gt__(self, other):
    return self.rank > other.rank

  @staticmethod
  def _assign_names(rank):
    """
    Assigns card names according to rank
    :param rank: rank of the card
    :return: string of the card's name
    """
    if isinstance(rank, int):

      if rank == 1:
        return "Ace", (Card.ACE_LOW,Card.ACE_HIGH)

      elif rank == 11:
        return "Jack", (Card.FACE,Card.FACE)

      elif rank == 12:
        return "Queen", (Card.FACE,Card.FACE)

      elif rank == 13:
        return "King", (Card.FACE,Card.FACE)

      else:
        return str(rank), (rank,rank)

    else:
      raise TypeError("The argument for the method must be an integer")

  def _translate_card(self):
    """
    Creates a human-readable name for the card
    :return: full name of the card
    """
    if isinstance(self.suit, int):

      if self.suit == 0:
        name, self.values = self._assign_names(self.rank)
        self.name = "{} of spades".format(name)

      elif self.suit == 1:
        name, self.values = self._assign_names(self.rank)
        self.name = "{} of hearts".format(name)

      elif self.suit == 2:
        name, self.values = self._assign_names(self.rank)
        self.name = "{} of diamonds".format(name)

      elif self.suit == 3:
        name, self.values = self._assign_names(self.rank)
        self.name = "{} of clubs".format(name)

      else:
        raise ValueError("The integer passed to the method must be 0, 1, 2, 3")

    else:
      raise TypeError("The argument for the method must be an integer")

    return self.name, self.values

