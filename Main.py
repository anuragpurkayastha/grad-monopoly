"""
 Run Woven Monopoly
"""
from Game import Game

if __name__ == "__main__":

    game = Game()

    game.createBoard()
    game.createPlayers()
    game.loadMoves()

    # Loop while game is still valid
    while game.isValid():

        # Get the next player

        # Move the player

        # Process any money tranfers
