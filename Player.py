"""
    Player.py

    Author: Anurag Purkayastha
    Date: 27 September 2021
"""
class Player:

    def __init__(self, name = "", totalMoney = 16):
        self.name = name
        self.totalMoney = totalMoney

    def getName(self):
        return self.name

    def getTotalMoney(self):
        return self.totalMoney

    def addMoney(self, amt):

        if ( amt >= 0 ):
            self.totalMoney += amt

    def isBankrupt(self):
        return self.totalMoney <= 0

    def spendMoney(self, amt):

        if ( amt >= 0 ):
            self.totalMoney -= amt

    def toString(self):
        return "Name:\t\t" + self.name + "\nTotal Money:\t$" + str(self.totalMoney)
