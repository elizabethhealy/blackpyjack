from card import Card
from hand import Hand
from card_bank import CardBank, BankError
from player import Player
from game import Game

BASIC_STRAT = {
  1 :[
    [], #0
    [], #1
    [], #2
    [], #3
    # A        2     3        4     5      6      7      8      9      10
     ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"], #4
     ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"], #5
     ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"], #6
     ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"], #7
     ["HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT", "HIT"], #8
     ["HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE","HIT", "HIT", "HIT", "HIT"], #9
     ["HIT", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE","DOUBLE", "DOUBLE", "DOUBLE", "HIT"],#10
     ["DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE","DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE"], #11
     ["HIT", "HIT", "HIT", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT"], #12
     ["HIT", "STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT"], #13
     ["HIT", "STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT"], #14
     ["HIT", "STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT"], #15
     ["HIT", "STAND", "STAND", "STAND", "STAND", "STAND", "HIT", "HIT", "HIT", "HIT"], #16
     ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"], #17
     ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"], #18
     ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"], #19
     ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"] #20
     ],
  2 :[
    [], #0
    [], #1
    # A        2     3        4       5        6        7      8      9      10
    ["HIT", "HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #AA
     ["HIT", "HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #A2
     ["HIT", "HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #A3
     ["HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #A4
     ["HIT", "HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #A5
     ["HIT", "HIT", "DOUBLE", "DOUBLE", "DOUBLE", "DOUBLE", "HIT", "HIT", "HIT", "HIT"], #A6
     ["HIT", "DOUBLE_S", "DOUBLE_S", "DOUBLE_S", "DOUBLE_S", "DOUBLE_S", "STAND", "STAND", "HIT", "HIT"], #A7
     ["STAND", "STAND", "STAND", "STAND", "STAND", "DOUBLE_S", "STAND", "STAND", "STAND", "STAND"], #A8
     ["STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND", "STAND"]  #A9
  ]
}

def bot_move(game, player):
  totals = player.hand.totals
  row = BASIC_STRAT[len(totals)][min(totals)]
  action = row[min(game.dealer.hand.cards[0].values) - 1]
  #if action=="DOUBLE": action="HIT"
  if action=="DOUBLE_S": action="STAND"
  return action