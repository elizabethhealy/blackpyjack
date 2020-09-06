from card import Card
from hand import Hand
from card_bank import CardBank, BankError
from player import Player, BetError


class Game():
  BLACKJACK_PAY = 3/2
  WIN_PAY = 1
  TABLE_MIN = 5
  TABLE_MAX = 100
  STARTER_CHIPS = 200
  states = {Hand.BLACKJACK:"Blackjack",
            Hand.BUST:"Bust",
            Hand.STAND:"Stand",
            Hand.OPEN:"Open"}
  def __init__(self, names, num_decks):
    self.dealer = Player("Dealer", True)
    self.num_decks = num_decks
    self.players = []
    for i in range(0,len(names)):
      self.players.append(Player(names[i], chips=Game.STARTER_CHIPS))
    self.bank = CardBank(num_decks)
    self.bank.shuffle_bank()
    self.pile = CardBank(0)

  def dealer_action(self):
    self.print_game()
    try:
      self.dealer.hand.hit(self.bank.take_card())
    except BankError:
      self.bank_restock()
      self.dealer.hand.hit(self.bank.take_card())

  def player_action(self, player, action):
    if action=="HIT" or action=="DOUBLE":
      try: 
        player.hand.hit(self.bank.take_card())
      except BankError:
        game.bank_restock()
        player.hand.hit(self.bank.take_card())
      if(action=="DOUBLE"):
        player.double_down()
        if player.hand.state==Hand.OPEN: player.hand.stand()
    else: player.hand.stand()

  def deal_round(self):
    for player in [self.dealer]+self.players:
      if player != self.dealer and player.chips < Game.TABLE_MIN:
        self.remove_player(player)
        continue
      try:
        card1, card2 = self.bank.take_card(), self.bank.take_card()
        player.hand = Hand(card1, card2, dealer = player.dealer)
      except BankError:
        self.bank_restock()
        card1, card2 = self.bank.take_card(), self.bank.take_card()
        player.hand = Hand(card1, card2, dealer=player.dealer)
  
  def remove_player(self, player):
    self.players.remove(player)

  def bank_restock(self):
    self.pile = self.bank
    self.bank = CardBank(self.num_decks)
    self.bank.shuffle_bank()

  def print_game_full(self):
    print("------------")
    print("Dealer: "+ str(self.dealer.hand.hand_list())+ " {"+str(self.dealer.hand.totals)+"}")
    for player in self.players:
      print(player.name + ": [chips="+str(player.chips)+", pot="+
      str(player.pot)+"]\n"+ str(player.hand.hand_list())+ 
      " {"+str(player.hand.totals)+"}")
    print("------------")
  
  def print_game(self):
    print("------------")
    print("Dealer: "+ str(self.dealer.hand.hand_list()[0]))
    for player in self.players:
      print(player.name + ": [chips="+str(player.chips)+", pot="+
      str(player.pot)+"]\n"+ str(player.hand.hand_list())+ " {"+
      str(player.hand.totals)+"}")
    print("------------")


