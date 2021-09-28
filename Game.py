"""
    Game.py
"""
class Game:

    def __init__(self, board = list(), players = list(), moves = list(), currPlayer = None):
        self.board = board      # A board is a list of Squares
        self.players = players  # Players
        self.moves = moves      # Predetermined moves
        self.playerIndex = 0    #  Index of the current player
        self.moveIndex = 0      #  Index of the current move
        self.currPlayer = currPlayer  #  The current player
        self.move = 0           #  How many moves the current player must move

    def getBoard(self):
        return self.board

    def getPlayers(self):
        return self.players

    def setPlayers(self, players):
        self.players = players

    def getMoves(self):
        return self.moves

    def setMoves(self, moves):
        self.moves = moves

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

    def getCurrentPlayerIndex(self):
        return self.playerIndex

    def setCurrentPlayerIndex(self, index):
        self.playerIndex = index

    def setCurrentPlayer(self, player):
        self.currPlayer = player

    def getCurrentPlayer(self):
        return self.currPlayer

    def setCurrentMove(self):
        self.move = self.moves[self.moveIndex]

    def getCurrentMove(self):
        return self.move

    def movePlayer(self, player, moves):
        """
        This method moves the player an amount equal to the moves that is predetermined.
        If it goes beyond the length of the board, then wrap around and earn $1 for the player (for passing GO).
        This function takes in two parameters:

            1. player - the player to move
            2. moves - how many steps the player should move
        """
        # Get the current position of the player on the board
        playerCurrentPos = player.getCurrPos()

        if ( (playerCurrentPos + moves) > (len(self.board) - 1) ):
            # If the player has to wrap around the board then calculate the resulting position.
            # This is done by checking if the end position (without wrap around) exceeds the length of the board.
            # Also earn $1 for passing GO
            player.setCurrPos(moves - ((len(self.board) - 1) - playerCurrentPos) - 1)
            player.addMoney(1)

        else:
            player.setCurrPos(playerCurrentPos + moves)

    def processTransaction(self):

        # Get the Square that the player is currently on
        currPlayer = self.getCurrentPlayer()
        currentSquare = self.board[currPlayer.getCurrPos()]

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
