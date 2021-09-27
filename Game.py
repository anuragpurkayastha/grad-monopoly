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

    def getBoard(self):
        return self.board

    def createPlayers(self):

        self.players.append(Player.withParams(name = "Peter"))
        self.players.append(Player.withParams(name = "Billy"))
        self.players.append(Player.withParams(name = "Charlotte"))
        self.players.append(Player.withParams(name = "Sweedal"))

    def getPlayers(self):
        return self.players

        

if __name__ == "__main__":

    game = Game()

    game.createBoard()
    game.createPlayers()

    board = game.getBoard()
    players = game.getPlayers()

    print(players)

    for i in range(0, len(board)):
        print(board[i].toString())

    print("=" * 50)

    for i in range(0, len(players)):
        print(players[i].toString())
