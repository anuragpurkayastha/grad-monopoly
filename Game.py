"""
    Main.py
"""
import Player
import Square

if __name__ == "__main__":

    player_1 = Player.Player("Anu")
    square_1 = Square.Square("The Burvale", 1, "Brown", "property", player_1, 100)

    print(square_1.getOwner().getName())
    
