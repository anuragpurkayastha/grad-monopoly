"""
    Player.py

    Author: Anurag Purkayastha
    Date: 27 September 2021
"""
class Player:

    def __init__(self, name = "", totalMoney = 16):
        self.name = name
        self.totalMoney = totalMoney
        self.currentPos = 0 # Each players current position represented as an index of the square the player is currently on

    def getName(self):
        return self.name

    def getTotalMoney(self):
        return self.totalMoney

    def addMoney(self, amt):

        if ( amt >= 0 ):
            self.totalMoney += amt

    def spendMoney(self, amt):

        if ( amt >= 0 ):
            self.totalMoney -= amt

    def setMoney(self, amt):
        self.totalMoney = amt

    def isBankrupt(self):
        return self.totalMoney <= 0

    def getCurrPos(self):
        return self.currentPos

    def setCurrPos(self, index):
        self.currentPos = index

    def __repr__(self):
        return "Name: " + self.name + ", Total Money: $" + str(self.totalMoney) + ", Current Position: " + str(self.currentPos)

    def __eq__(self, other):
        if other is None:
            return False

        return self.name == other.name and self.totalMoney == other.totalMoney and self.currentPos == other.currentPos
