from card import Card
from hand import Hand
from card_bank import CardBank, BankError
from player import Player, BetError
from bot import bot_move
from game import Game

def start_game():
  names = input("Names of players seperated by comma: ")
  names = names.split(", ")
  num_decks = int(input("Number of decks: "))
  if len(names)<1 or num_decks<1: 
    print("Please enter at least one player name and decks >= 1")
    return start_game()
  else:
    print("+++++++++++NEW GAME++++++++++++++\nTALBE MINUMUM: "+
    str(Game.TABLE_MIN)+"\nTABLE MAXIMUM: "+ str(Game.TABLE_MAX)+
    "\nBLACKJACK'S PAY: "+str(Game.BLACKJACK_PAY)+"\nSTARTING CHIPS: "+
    str(Game.STARTER_CHIPS))
    return Game(names, num_decks)
    
def collect_initial_bets(game: Game):
  for player in game.players:
    if player.name=="BOT":
      try: player.bet(Game.TABLE_MIN)
      except BetError: game.remove_player(player)
    else:
      bad_bet = True
      while bad_bet:
        bet = float(input(player.name+" ["+str(player.chips)+"] \nHow much would you like to bet: "))
        if bet < Game.TABLE_MIN or bet> Game.TABLE_MAX: print("Bet must be >= table min"); continue
        try: 
          player.bet(bet)
          bad_bet=False
        except BetError: continue

def collect_bets(game: Game):
  for player in game.players:
    if player.name!="BOT" and player.hand.state!=Hand.BLACKJACK:
      bad_bet = True
      while bad_bet:
        bet = float(input(player.name+" ["+str(player.chips)+"] \nHow much would you like to add: "))
        if bet < Game.TABLE_MIN or bet> Game.TABLE_MAX: print("Bet must be >= table min"); continue
        try: 
          player.bet(bet)
          bad_bet=False
        except BetError: continue

def play_round(game: Game):
  game.deal_round()
  collect_initial_bets(game)
  game.print_game()
  collect_bets(game)
  for player in game.players:
    while player.hand.state == Hand.OPEN:
      game.print_game()
      if player.name != "BOT": action = input(player.name+" choose action [HIT, DOUBLE, or STAND]: ")
      else: action = bot_move(game, player); print(player.name+": "+action)
      game.player_action(player, action)
    print(player.name+": "+Game.states[player.hand.state])
  while game.dealer.hand.state == Hand.OPEN:
    game.dealer_action()
    print(game.dealer.name+": "+Game.states[game.dealer.hand.state])

def finish_round(game: Game):
  dealer_score = max(game.dealer.hand.totals) if game.dealer.hand.totals else 0
  for player in game.players:
    player_score = max(player.hand.totals) if player.hand.totals else 0
    if not player_score:
      player.lose()
      print(player.name+": "+"LOSE")
    elif player.hand.state==Hand.BLACKJACK:
      player.win(Game.BLACKJACK_PAY)
      print(player.name+": "+"WIN")
    elif player_score>dealer_score:
      player.win(Game.WIN_PAY)
      print(player.name+": "+"WIN")
    elif player_score==dealer_score:
      player.win()
      print(player.name+": "+"TIE")
    else:
      player.lose()
      print(player.name+": "+"LOSE")
    player.hand = None
  game.dealer.hand = None


game = start_game()
#game.deal_round()
while True:
  print("================ NEW ROUND ==================")
  play_round(game)
  game.print_game_full()
  finish_round(game)