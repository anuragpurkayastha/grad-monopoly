"""
 Run Woven Monopoly
"""
from Game import Game
from Player import Player
from Square import Square
import json

if __name__ == "__main__":

    #=============== SETUP ===========================

    # PLAYERS
    players = list()

    players.append(Player(name = "Peter"))
    players.append(Player(name = "Billy"))
    players.append(Player(name = "Charlotte"))
    players.append(Player(name = "Sweedal"))

    # BOARD
    board = list()
    # Read in the board.json file to create a list of squares
    with open('specs/board.json') as file:
        sqr_data = json.load(file)

    for i in range(0, len(sqr_data)):
        sqr = sqr_data[i]
        if (sqr['type'] != "go"):
            board.append(Square(name = sqr['name'], price = sqr['price'], colour = sqr['colour'], sqr_type = sqr['type']))
        else:
            board.append(Square(name = sqr['name'], sqr_type = sqr['type']))

    # MOVES
    filepath = './specs/rolls_2.json'
    moves = list()
    with open(filepath) as file:
        moves = json.load(file)

    # SETUP THE GAME
    game = Game(board = board, players = players, moves = moves)

    # Loop while game is still valid
    while game.isValid():

        # Set the next player
        game.setCurrentPlayer(game.getPlayers()[game.getCurrentPlayerIndex()])

        # Set the amount of moves to move the current player
        game.setCurrentMove()

        # Move the current player
        game.movePlayer(game.getCurrentPlayer(), game.getCurrentMove())

        # Process transactions
        game.processTransaction()

        # End turn
        game.endTurn()

    game.announceFinalResults()
