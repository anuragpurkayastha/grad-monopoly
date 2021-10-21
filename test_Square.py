import unittest
from Square import Square
from Player import Player

class TestSquareMethods(unittest.TestCase):

    def setUp(self):
        self.player = Player(name = "Michael")
        self.square_1 = Square()
        self.square_2 = Square(name = "Betty's Burgers", price = 10, colour = "Green", sqr_type = "property", owner = self.player, rent = 5)

    def test_get_name(self):
        self.assertEqual(self.square_1.getName(), "")
        self.assertEqual(self.square_2.getName(), "Betty's Burgers")

    def test_set_name(self):
        self.square_2.setName("Test Name")
        self.assertEqual(self.square_2.getName(), "Test Name")

    def test_get_price(self):
        self.assertEqual(self.square_1.getPrice(), 0)
        self.assertEqual(self.square_2.getPrice(), 10)

    def test_set_price(self):
        self.square_1.setPrice(15)
        self.assertEqual(self.square_1.getPrice(), 15)

    def test_set_price_error(self):
        """Test that the setPrice() method throws an error when given a non-number as a parameter"""
        self.assertRaises(TypeError, self.square_1.setPrice, "bubbles")

    def test_get_colour(self):
        self.assertEqual(self.square_1.getColour(), "")
        self.assertEqual(self.square_2.getColour(), "Green")

    def test_get_type(self):
        self.assertEqual(self.square_1.getType(), "")
        self.assertEqual(self.square_2.getType(), "property")

    def test_set_type(self):
        self.square_1.setType("go")
        self.assertEqual(self.square_1.getType(), "go")

    def test_get_owner(self):
        self.assertEqual(self.square_1.getOwner(), None)
        self.assertEqual(self.square_2.getOwner(), self.player)

    def test_set_owner(self):
        self.square_1.setOwner(self.player)
        self.assertEqual(self.square_1.getOwner(), self.player)

    def test_is_owned(self):
        self.assertEqual(self.square_1.isOwned(), False)
        self.assertEqual(self.square_2.isOwned(), False)

    def test_set_is_owned(self):

        self.square_1.setIsOwned(True)
        self.assertEqual(self.square_1.isOwned(), True)

        self.square_1.setIsOwned(False)
        self.assertEqual(self.square_1.isOwned(), False)

    def test_set_is_owned_error(self):
        """Test if the method throws an Exception when given a non-boolean argument"""
        self.assertRaises(TypeError, self.square_1.setIsOwned, 42)

    def test_get_rent(self):
        self.assertEqual(self.square_1.getRent(), 0)
        self.assertEqual(self.square_2.getRent(), 5)

    def test_set_rent(self):
        self.square_1.setRent(17)
        self.assertEqual(self.square_1.getRent(), 17)

if __name__ == '__main__':
    unittest.main()
