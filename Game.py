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
        self.currPlayer = None  #  The current player
        self.move = 0           #  How many moves the current player must move

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

        self.players.append(Player(name = "Peter"))
        self.players.append(Player(name = "Billy"))
        self.players.append(Player(name = "Charlotte"))
        self.players.append(Player(name = "Sweedal"))

    def getPlayers(self):
        return self.players

    def loadMoves(self,filepath='./specs/rolls_1.json'):

        with open(filepath) as file:
            self.moves = json.load(file)

    def getMoves(self):
        return self.moves

    def getMoveIndex(self):
        return self.moveIndex

    def setMoveIndex(self, index):
        self.moveIndex = index

    def isValid(self):
        """
        Check if the game is still in a valid state. This means the two conditions must be met:

        1. No player is bankrupt
        2. More moves are still available
        """
        if( self.moveIndex == len(self.moves)):
            return False

        for player in self.players:

            if player.isBankrupt():
                return False

        return True

    def setCurrentPlayer(self):
        self.currPlayer = self.players[self.playerIndex]

    def getCurrentPlayer(self):
        return self.currPlayer

    def setCurrentMove(self):
        self.move = self.moves[self.moveIndex]

    def getCurrentMove(self):
        return self.move

    def movePlayer(self):
        """
        This method moves the player an amount equal to the moves that is predetermined.
        If it goes beyond the length of the board, then wrap around and earn $1 for the player (for passing GO).
        """
        # Get the current position of the player on the board
        playerCurrentPos = self.currPlayer.getCurrPos()

        if ( (playerCurrentPos + self.move) > (len(self.board) - 1) ):
            # If the player has to wrap around the board then calculate the resulting position.
            # This is done by checking if the end position (without wrap around) exceeds the length of the board.
            # Also earn $1 for passing GO
            self.currPlayer.setCurrPos(self.move - ((len(self.board) - 1) - playerCurrentPos) - 1)
            self.currPlayer.addMoney(1)

        else:
            self.currPlayer.setCurrPos(self.currPlayer.getCurrPos() + self.move)

    def processTransaction(self):

        # Get the Square that the player is currently on
        currentSquare = self.board[self.currPlayer.getCurrPos()]

        # If the Square the player is currently on is not "GO" then process a transaction (either buying property or paying rent
        if currentSquare.getType() != "go":

            if not currentSquare.isOwned():
                # If the Square is owned, then current player buys the property
                # Set rent of Square to non-zero value

                self.currPlayer.spendMoney(currentSquare.getPrice())
                currentSquare.setOwner(self.currPlayer)
                currentSquare.setIsOwned()
                currentSquare.setRent(1)


                # Also check if the current player now owns all of the properties of the same colour.
                if self.isAllPropOwned(currentSquare.getColour(), self.currPlayer):

                    currentSquare.setRent(currentSquare.getRent() * 2)

            else:

                self.currPlayer.spendMoney(currentSquare.getRent())

    def isAllPropOwned(self, colour, player):
        """
        Check if all the properties of a particular colour are owned by one player
        """
        for square in self.board:
            if (square.getColour() == colour and square.getOwner() != player):
                return False

        return True

    def endTurn(self):
        # Next player
        if (self.playerIndex == (len(self.players) - 1)):
            self.playerIndex = 0
        else:
            self.playerIndex += 1

        # Next move
        self.moveIndex += 1

    def getWinner(self):
        max_money = 0
        winner = None

        for player in self.players:
            if player.getTotalMoney() > max_money:
                winner = player

        return winner

    def announceFinalResults(self):
        """
        Method to call when the game is ended (game is no longer valid)
        """
        winningPlayer = self.getWinner()

        print ("The winner is: " + winningPlayer.getName() + " with $" + str(winningPlayer.getTotalMoney()) + "!!")

        print("\nThe other results:")

        for player in self.players:
            player_det = "\nName:\t\t" + player.getName() + "\nTotal Money:\t$" + str(player.getTotalMoney()) + "\nFinal Position:\t" + self.board[player.getCurrPos()].getName()
            print (player_det)
