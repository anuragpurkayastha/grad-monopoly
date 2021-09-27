"""
    Player.py

    Author: Anurag Purkayastha
    Date: 27 September 2021
"""
class Player:

    def __init__(self, name, totalMoney = 16):
        self.name = name
        self.totalMoney = totalMoney

    def __init__(self):
        self.name = ""
        self.totalMoney = 0

    def getName(self):
        return self.name

    def getTotalMoney(self):
        return self.totalMoney

    def addMoney(self, amt):
        """
        Earn money from rent or passing GO.
        """
        self.totalMoney += amt

    def isBankrupt(self):
        return self.totalMoney <= 0

    def spendMoney(self, amt):
        self.totalMoney -= amt
