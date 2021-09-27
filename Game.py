"""
    Game.py
"""
import Player import Player
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

        players.append(Player("Peter"))
        players.append(Player("Billy"))
        players.append(Player("Charlotte"))
        players.append(Player("Sweedal"))

    def getPlayers(self):
        return self.players

        

if __name__ == "__main__":

    game = Game()
    game.createBoard()

    board = game.getBoard()

    for i in range(0, len(board)):
        print(board[i].toString())
