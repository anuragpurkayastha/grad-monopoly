import unittest
from Game import Game
from Square import Square
from Player import Player
import json

class TestGameMethod(unittest.TestCase):

    def setUp(self):

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

        for i in range(len(sqr_data)):
            sqr = sqr_data[i]

            if (sqr['type'] != "go"):
                board.append(Square(name = sqr['name'], price = sqr['price'], colour = sqr['colour'], sqr_type = sqr['type']))
            else:
                board.append(Square(name = sqr['name'], sqr_type = sqr['type']))

        # MOVES
        filepath = './specs/rolls_1.json'
        moves = list()
        with open(filepath) as file:
            moves = json.load(file)

        # SETUP THE GAME
        self.game = Game(board = board, players = players, moves = moves)

    def test_get_board(self):

        expected = [Square(name = "GO", sqr_type = "go"),
                        Square(name = "The Burvale", price = 1, colour = "Brown", sqr_type = "property"),
                        Square(name = "Fast Kebabs", price = 1, colour = "Brown", sqr_type = "property"),
                        Square(name = "The Grand Tofu", price = 2, colour = "Red", sqr_type = "property"),
                        Square(name = "Lanzhou Beef Noodle", price = 2, colour = "Red", sqr_type = "property"),
                        Square(name = "Betty's Burgers", price = 3, colour = "Green", sqr_type = "property"),
                        Square(name = "YOMG", price = 3, colour = "Green", sqr_type = "property"),
                        Square(name = "Gami Chicken", price = 4, colour = "Blue", sqr_type = "property"),
                        Square(name = "Massizim", price = 4, colour = "Blue", sqr_type = "property")
                    ]
        self.assertEqual(self.game.getBoard(), expected)

    def test_get_players(self):
        expected = [Player(name = "Peter"), Player(name = "Billy"), Player(name = "Charlotte"), Player(name = "Sweedal")]

        self.assertEqual(self.game.getPlayers(), expected)

    def test_load_moves(self):
        expected_1 = [1, 3, 1, 1, 1, 2, 4, 2, 6, 3, 5, 2, 2, 2, 4, 4, 6, 1, 4, 2, 6, 2, 1, 5, 4, 5, 6, 5, 6, 3, 6, 4, 4, 3, 5, 6, 2, 1, 6, 5, 1, 1, 6, 4, 5, 2, 2, 3, 5, 6]

        self.assertEqual(self.game.getMoves(), expected_1)

    def test_get_move_index(self):
        self.assertEqual(self.game.getMoveIndex(), 0)

    def test_set_move_index(self):
        self.game.setMoveIndex(17)
        self.assertEqual(self.game.getMoveIndex(), 17)

    def test_is_valid(self):
        self.assertEqual(self.game.isValid(), True)

        # Test if a player is bankrupt
        player = self.game.getPlayers()[0]
        player.setMoney(0)

        self.assertEqual(self.game.isValid(), False)

        # Test if no more moves left
        self.game.setMoveIndex(len(self.game.getMoves()) + 1)
        self.assertEqual(self.game.isValid(), False)

    def test_move_player(self):
        player = self.game.getPlayers()[0]
        player.setCurrPos(0)
        self.game.setCurrentPlayer(player)

        # Test if player is in bounds
        self.game.movePlayer(player, 3)

        self.assertEqual(player.getCurrPos(), 3)

        # Test if player is going to wrap around
        player.setCurrPos(len(self.game.getBoard()) - 1)
        self.game.movePlayer(player, 2)

        self.assertEqual(player.getCurrPos(), 1)

    def test_process_transaction_buy(self):

        """ Test transaction for buying a property"""
        player = self.game.getPlayers()[0]
        player.setCurrPos(1)

        square = self.game.getBoard()[player.getCurrPos()]

        self.game.setCurrentPlayer(player)
        self.game.processTransaction()

        self.assertEqual(player.getTotalMoney(), 15)
        self.assertEqual(square.isOwned(), True)
        self.assertEqual(square.getOwner(), player)

    def test_process_transaction_rent(self):

        """Test transaction for a renter"""
        # Players
        owner = self.game.getPlayers()[0]
        renter = self.game.getPlayers()[1]
        renter.setCurrPos(1)

        # Setup the current player
        self.game.setCurrentPlayer(renter)

        # Owner buys the square
        square = self.game.getBoard()[renter.getCurrPos()]
        self.game.buyProperty(square, owner)

        # Main method to test
        self.game.processTransaction()

        self.assertEqual(renter.getTotalMoney(), 15)
        self.assertEqual(owner.getTotalMoney(), 16)
        self.assertEqual(square.isOwned(), True)

    def test_process_trans_rent_owner(self):
        """ Test if an owner pays himself rent """
        owner = self.game.getPlayers()[0]
        owner.setCurrPos(1)

        self.game.setCurrentPlayer(owner)

        # Setup the square so that it is already owned by the player
        square = self.game.getBoard()[owner.getCurrPos()]
        self.game.buyProperty(square, owner)

        # Now process the transaction as if the owner just landed on their own property
        self.game.processTransaction()

        self.assertEqual(owner.getTotalMoney(), 15)

    def test_process_transaction_all_property_owned(self):
        """Test the process transaction fo all property of one colour owned"""
        player = self.game.getPlayers()[0]
        self.game.setCurrentPlayer(player)
        player.setCurrPos(2)

        square_1 = self.game.getBoard()[1]
        square_2 = self.game.getBoard()[2]

        # Set square 1 as bought by player
        self.game.buyProperty(square_1, player)
        self.game.processTransaction()

        self.assertEqual(square_2.getOwner(), player)
        self.assertEqual(square_1.isOwned(), True)
        self.assertEqual(self.game.isAllPropOwned(square_1.getColour(), player), True)
        self.assertEqual(square_1.getRent(), 2)
        self.assertEqual(square_2.getRent(), 2)

    def test_is_all_prop_owned(self):
        square_1 = self.game.getBoard()[1]
        square_2 = self.game.getBoard()[2]

        player = self.game.getPlayers()[0]

        square_1.setOwner(player)
        square_2.setOwner(player)

        self.assertEqual(self.game.isAllPropOwned(square_1.getColour(), player), True)

if __name__ == '__main__':
    unittest.main()
