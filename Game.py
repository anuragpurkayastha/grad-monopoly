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
                print(player.getName() + " went bankrupt!")
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
            # This is done by checking if the end position (without wrap around) is beyond the last indicie of the board.
            # Also earn $1 for passing GO
            player.setCurrPos(moves - ((len(self.board) - 1) - playerCurrentPos) - 1)
            player.addMoney(1)
        else:
            player.setCurrPos(playerCurrentPos + moves)

    def processTransaction(self):

        # Get the Square that the player is currently on
        currPlayer = self.currPlayer
        currentSquare = self.board[currPlayer.getCurrPos()]

        # If the Square the player is currently on is not "GO" then process a transaction (either buying property or paying rent
        if currentSquare.getType() != "go":

            if not currentSquare.isOwned():

                self.buyProperty(currentSquare, currPlayer)

                # Also check if the current player now owns all of the properties of the same colour.
                if self.isAllPropOwned(currentSquare.getColour(), currPlayer):
                    # Increase the rent of all the properties
                    self.doubleRent(currentSquare.getColour())

            elif (currentSquare.getOwner().getName() != currPlayer.getName()):
                self.spendRent(currentSquare, currPlayer)

    def buyProperty(self, prop, player):
        """
        Function to buy property provided by 'prop' owned by player with rent set to the price of the property.
        """
        player.spendMoney(prop.getPrice())
        prop.setOwner(player)
        prop.setIsOwned()
        prop.setRent(prop.getPrice())

    def doubleRent(self, colour):
        """
        Double the rent of all properties of a particular colour
        """
        for square in self.board:
            if (square.getColour() == colour):
                square.setRent(square.getRent() * 2)

    def spendRent(self, prop, renter):
        """
        Process rent payments for property prop from renter to owner
        """
        renter.spendMoney(prop.getRent())
        owner = prop.getOwner()
        owner.addMoney(prop.getRent())

    def isAllPropOwned(self, colour, player):
        """
        Check if all the properties of a particular colour are owned by one player
        """
        for square in self.board:

            if (square.getColour() == colour and square.getOwner() != player):
                return False

        return True

    def endTurn(self):
        """
        Ending turn means move the player and move indices to the next player and move, respectively.
        """

        # Next player - wrap around if needed.
        if (self.playerIndex == (len(self.players) - 1)):
            self.playerIndex = 0
        else:
            self.playerIndex += 1

        # Next move
        self.moveIndex += 1

    def getWinner(self):
        """
        Get the winner of the game - determined by the player with the most money.
        """
        max_money = 0
        winner = None

        for player in self.players:

            if (player.getTotalMoney() > max_money):

                winner = player
                max_money = player.getTotalMoney()

        return winner

    def announceFinalResults(self):
        """
        Method to call when the game is ended (game is no longer valid)
        """
        winningPlayer = self.getWinner()

        print ("The winner is: " + winningPlayer.getName() + " with $" + str(winningPlayer.getTotalMoney()) + "!!")

        print("\nThe results:")

        for player in self.players:

            player_det = "\tName: " + player.getName() + "\tTotal Money:\t$" + str(player.getTotalMoney()) + "\tFinal Position: " + self.board[player.getCurrPos()].getName()

            print (player_det)
