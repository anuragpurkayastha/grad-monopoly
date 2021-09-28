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

if __name__ == '__main__':
    unittest.main()
