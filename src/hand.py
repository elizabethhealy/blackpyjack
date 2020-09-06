from card import Card

#STATES = {0: "OPEN", 1: "STAND", 2: "BLACKJACK", 3: "BUST"}

"""Represents a blackjack hand"""
class Hand(object):
  OPEN=0
  STAND=1
  BLACKJACK=21
  BUST=3
  DEALER_STAND=17
  def __init__(self, card1, card2, dealer=False):
    """
    Initializes the hand with two cards
    """
    self.dealer = dealer
    self.cards = [card1, card2]
    self.state = Hand.OPEN
    self.totals = self._totals(self.cards)
    self._calc_states()
    

  def hand_list(self):
    cards = []
    for card in self.cards:
      cards.append(card.name)
    return cards

  def _calc_states(self):
    if Hand.BLACKJACK in self.totals: self.state=Hand.BLACKJACK
    elif not self.totals: self.state=Hand.BUST
    elif self.dealer:
      dealer_stand = False
      for total_i in range(0,len(self.totals)):
        if self.totals[total_i]>=Hand.DEALER_STAND:
          dealer_stand=True
          break
      if dealer_stand: self.state=Hand.STAND

  def _totals(self, cards):
    """get list of possible hand totals"""
    aces=0
    others_total=0
    for card in cards:
      first, second = card.values
      if first==second: others_total += first
      else: aces += 1
    totals=[]
    for i in range(0,aces+1):
      i_total = i*Card.ACE_LOW + (aces-i)*Card.ACE_HIGH + others_total
      if (i_total not in totals) and (i_total<= Hand.BLACKJACK):
        totals.append(i_total)
    return totals

  def hit(self, card):
    """add card to hand"""
    self.cards.append(card)
    self.totals = self._totals(self.cards)
    self._calc_states()
    
    
  def stand(self):
    """stand on hand"""
    if self.state!=Hand.BLACKJACK and self.stand!=Hand.BUST:
      self.state = Hand.STAND

  def splittable(self):
    """check if hand is splittable"""
    if len(self.cards==2) and self.cards[0].values==self.cards[1].values:
      return True
    return False

  def split(self, card1, card2):
    """split into two hands"""
    pass
    #return 2 hands
    