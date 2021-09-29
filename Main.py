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
    players_1 = [Player(name = "Peter"),
                Player(name = "Billy"),
                Player(name = "Charlotte"),
                Player(name = "Sweedal")]

    players_2 = [Player(name = "Peter"),
                Player(name = "Billy"),
                Player(name = "Charlotte"),
                Player(name = "Sweedal")]

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
    filepath_1 = './specs/rolls_1.json'
    filepath_2 = './specs/rolls_2.json'
    moves_1 = list()
    moves_2 = list()

    with open(filepath_1) as file:
        moves_1 = json.load(file)

    with open(filepath_2) as file:
        moves_2 = json.load(file)

    # SETUP THE GAME
    game_1 = Game(board = board, players = players_1, moves = moves_1)
    game_2 = Game(board = board, players = players_2, moves = moves_2)

    print()
    print("=" * 50 + "\tGAME ONE\t" + "=" * 50)
    # Loop while game is still valid
    while game_1.isValid():

        # Set the next player
        game_1.setCurrentPlayer(game_1.getPlayers()[game_1.getCurrentPlayerIndex()])

        # Set the amount of moves to move the current player
        game_1.setCurrentMove()

        # Move the current player
        game_1.movePlayer(game_1.getCurrentPlayer(), game_1.getCurrentMove())

        # Process transactions
        game_1.processTransaction()

        # End turn
        game_1.endTurn()

    game_1.announceFinalResults()

    print()
    print("=" * 50 + "\tGAME TWO\t" + "=" * 50)
    while game_2.isValid():

        # Set the next player
        game_2.setCurrentPlayer(game_2.getPlayers()[game_2.getCurrentPlayerIndex()])

        # Set the amount of moves to move the current player
        game_2.setCurrentMove()

        # Move the current player
        game_2.movePlayer(game_2.getCurrentPlayer(), game_2.getCurrentMove())
        # Process transactions
        game_2.processTransaction()

        # End turn
        game_2.endTurn()

    game_2.announceFinalResults()
    print()
