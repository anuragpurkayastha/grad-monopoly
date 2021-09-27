"""
    Square.py
    Author: Anurag Purkayastha
"""
from Player import Player

class Square:

    def __init__(self, name, price = 0, colour= "", sqr_type = "", owner = Player(), rent = 0):
        self.name = name
        self.price = price
        self.colour = colour
        self.sqr_type = sqr_type
        self.owner = owner
        self.rent = rent
        self.owned = False

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getColour(self):
        return self.colour

    def getType(self):
        return self.sqr_type

    def getOwner(self):
        return self.owner

    def setOwner(self, player):
        self.owner = player

    def isOwned(self):
        return self.owned

    def setIsOwned(self):
        self.owned = True

    def getRent(self):
        return self.rent

    def setRent(self, rent):
        self.rent = rent

    def toString(self):
        return "Name:\t" + self.name + "\nPrice:\t" + str(self.price) + "\nColour:\t" + self.colour + "\nType:\t" + self.sqr_type + "\nOwner:\t" + self.owner.getName() + "\nRent:\t" + str(self.rent)
