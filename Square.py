"""
    Square.py
    Author: Anurag Purkayastha
"""
import Player

class Square:

    def __init__(self, name, price = 0, colour= "", sqr_type = "", owner = "", rent = 0):
        self.name = name
        self.price = price
        self.colour = colour
        self.sqr_type = sqr_type
        self.owner = owner
        self.rent = rent

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

    def getRent(self):
        return self.rent

    def setRent(self, rent):
        self.rent = rent
