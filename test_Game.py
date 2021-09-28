import unittest
from Game import Game
from Square import Square
from Player import Player

class TestGameMethod(unittest.TestCase):

    maxDiff = None
    def setUp(self):
        self.board = [Square(name = "GO", sqr_type = "go"),
                        Square(name = "The Burvale", price = 1, colour = "Brown", sqr_type = "property"),
                        Square(name = "Fast Kebabs", price = 1, colour = "Brown", sqr_type = "property"),
                        Square(name = "The Grand Tofu", price = 2, colour = "Red", sqr_type = "property"),
                        Square(name = "Lanzhou Beef Noodle", price = 2, colour = "Red", sqr_type = "property"),
                        Square(name = "Betty's Burgers", price = 3, colour = "Green", sqr_type = "property"),
                        Square(name = "YOMG", price = 3, colour = "Green", sqr_type = "property"),
                        Square(name = "Gami Chicken", price = 4, colour = "Blue", sqr_type = "property"),
                        Square(name = "Massizim", price = 4, colour = "Blue", sqr_type = "property")
                    ]

        self.game = Game()
        self.game.createBoard()
        self.game.createPlayers()

    def test_get_board(self):
        self.assertEqual(self.game.getBoard(), self.board)

    def test_get_players(self):
        expected = [Player(name = "Peter"), Player(name = "Billy"), Player(name = "Charlotte"), Player(name = "Sweedal")]

        self.assertEqual(self.game.getPlayers(), expected)

if __name__ == '__main__':
    unittest.main()
