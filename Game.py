"""
    Game.py
"""
from Player import Player
from Square import Square
import json

class Game:

    def __init__(self):
        self.board = list()
        self.players = list()
        self.moves = list()
        self.playerIndex = 0    #  Index of the current player
        self.moveIndex = 0      #  Index of the current move

    def createBoard(self):
        # Read in the board.json file to create a list of squares
        with open('specs/board.json') as file:
            sqr_data = json.load(file)

        for i in range(0, len(sqr_data)):
            sqr = sqr_data[i]
            if (sqr['type'] != "go"):
                self.board.append(Square(name = sqr['name'], price = sqr['price'], colour = sqr['colour'], sqr_type = sqr['type']))
            else:
                self.board.append(Square(name = sqr['name'], sqr_type = sqr['type']))

    def createPlayers(self):

        self.players.append(Player(name = "Peter"))
        self.players.append(Player(name = "Billy"))
        self.players.append(Player(name = "Charlotte"))
        self.players.append(Player(name = "Sweedal"))

    def getPlayers(self):
        return self.players

    def loadMoves(self,filepath='./specs/rolls_1.json'):

        with open(filepath) as file:
            self.moves = json.load(file)

    def isValid(self):
        """
        Check if the game is still in a valid state. This means the two conditions must be met:

        1. No player is bankrupt
        2. More moves are still available
        """
        if( self.moveIndex == len(self.moves)):
            return False

        for i in range(len(self.players)):

            if self.players[i].isBankrupt():
                return False

        return True
