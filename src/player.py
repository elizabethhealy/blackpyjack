from card import Card
from hand import Hand
from card_bank import CardBank

class BetError(Exception):
  pass


class Player(object):
  def __init__(self, name, dealer=False, chips=0):
    """
    Initializes the player object
    """
    self.name = name
    self.dealer = dealer
    self.chips = chips
    self.pot = 0
    self.hand = None

  def __eq__(self, other):
    return self.name == other.name

  def bet(self, bet):
    if bet>self.chips: raise BetError("You cannot bet more than you have")
    self.chips -= bet
    self.pot += bet
  
  def double_down(self):
    if self.pot>self.chips: raise BetError("You cannot bet more than you have")
    self.chips -= self.pot
    self.pot = 2*self.pot

  def win(self, multiplier=0):
    self.chips += self.pot*(1+multiplier)
    self.pot = 0

  def lose(self):
    self.pot = 0


  