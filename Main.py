"""
 Run Woven Monopoly
"""
from Game import Game

if __name__ == "__main__":

    game = Game()

    game.createBoard()
    game.createPlayers()
    game.loadMoves('./specs/rolls_2.json')

    # Loop while game is still valid
    while game.isValid():

        # Get the next player
        game.setCurrentPlayer()

        # Get the amount of moves to move the current player
        game.setCurrentMove()

        # Move the player
        game.movePlayer()

        # Process transactions
        game.processTransaction()

        # End turn
        game.endTurn()

    game.announceFinalResults()
