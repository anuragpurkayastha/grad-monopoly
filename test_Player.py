import unittest
from Player import Player

class TestPlayerMethods(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player()
        self.player_2 = Player(name = "Mike", totalMoney = 20)

    def test_get_name(self):
        self.assertEqual(self.player_1.getName(), "")
        self.assertEqual(self.player_2.getName(), "Mike")

    def test_get_total_money(self):
        self.assertEqual(self.player_1.getTotalMoney(), 16)
        self.assertEqual(self.player_2.getTotalMoney(), 20)

    def test_add_money(self):
        self.player_1.addMoney(2)
        self.player_2.addMoney(10)

        self.assertEqual(self.player_1.getTotalMoney(), 18)
        self.assertEqual(self.player_2.getTotalMoney(), 30)

    def test_spend_money(self):
        self.player_1.spendMoney(5)
        self.player_2.spendMoney(6)

        self.assertEqual(self.player_1.getTotalMoney(), 11)
        self.assertEqual(self.player_2.getTotalMoney(), 14)

    def test_set_money(self):
        self.player_1.setMoney(35)

        self.assertEqual(self.player_1.getTotalMoney(), 35)

    def test_is_bankrupt(self):
        self.player_1.setMoney(2)
        self.player_2.setMoney(-15)

        self.assertEqual(self.player_1.isBankrupt(), False)
        self.assertEqual(self.player_2.isBankrupt(), True)

    def test_get_curr_pos(self):
        self.assertEqual(self.player_1.getCurrPos(), 0)
        self.assertEqual(self.player_2.getCurrPos(), 0)

    def test_set_curr_pos(self):
        self.player_1.setCurrPos(4)

        self.assertEqual(self.player_1.getCurrPos(), 4)

    def test_to_string(self):
        result_1 = "Name:\t\t\nTotal Money:\t$16\nCurrent Position:\t\t0"
        result_2 = "Name:\t\tMike\nTotal Money:\t$20\nCurrent Position:\t\t0"

        self.assertEqual(self.player_1.toString(), result_1)
        self.assertEqual(self.player_2.toString(), result_2)

if __name__ == '__main__':
    unittest.main()
