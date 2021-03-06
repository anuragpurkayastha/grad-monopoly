"""
    Square class represents one square on the board
"""
from Player import Player

class Square:

    def __init__(self, name = "", price = 0, colour= "", sqr_type = "", owner = None, rent = 0):
        self.name = name
        self.price = price
        self.colour = colour
        self.sqr_type = sqr_type
        self.owner = owner
        self.rent = rent
        self.owned = False

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        """Takes a number value for the price"""
        if (isinstance(price, (float, int))):
            self.price = price
        else:
            raise TypeError("Price must be a number")

    def getColour(self):
        return self.colour

    def getType(self):
        return self.sqr_type

    def setType(self, sqr_type):
        """Takes a string as the type parameter (sqr_type)"""
        self.sqr_type = sqr_type

    def getOwner(self):
        return self.owner

    def setOwner(self, player):
        """Takes a Player object for the player"""
        self.owner = player

    def isOwned(self):
        return self.owned

    def setIsOwned(self, owned):

        if (isinstance(owned, bool)):
            self.owned = owned
        else:
            raise TypeError("Expecting a boolean (true or false)")

    def getRent(self):
        return self.rent

    def setRent(self, rent):

        if (isinstance(rent, (int, float))):
            self.rent = rent
        else:
            raise TypeError("Expecting a number (int or float)")

    def __repr__(self):
        return "Name: " + self.name + ", Price: " + str(self.price) + ", Colour: " + self.colour + ", Type: " + self.sqr_type + ", Owner: " + (self.owner.getName() if (self.owner != None) else "") + ", Rent: " + str(self.rent)

    def __eq__(self,other):
        return self.name == other.name and self.price == other.price and self.colour == other.colour and self.sqr_type == other.sqr_type and self.rent == other.rent and self.owned == other.owned
