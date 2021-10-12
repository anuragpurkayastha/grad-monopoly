# Woven Monopoly
As part of a coding test for a Graduate Program, I needed to build a small application that plays a game of Woven Monopoly.

The rules can be found in the `README.md` file in the `specs` folder.

# Usage
The game was written using Python version 3.9.7.

The files are described below.

  * **Main.py** - The file that executes the game. Loads in the moves and creates players.
  * **Game.py** - Contains the game logic.
  * **Square.py** - Contains the Square class which represents each square on the board.
  * **Player.py** - Player class which represents a player of the game.

Execute the following command to run the program.

`
python Main.py
`

The output should resemble the output below.

```
$ python Main.py 

==================================================      GAME ONE        ==================================================
The winner is: Peter with $40!!

The results:
        Name: Peter     Total Money:    $40     Final Position: Massizim
        Name: Billy     Total Money:    $14     Final Position: GO
        Name: Charlotte Total Money:    $-1     Final Position: Gami Chicken
        Name: Sweedal   Total Money:    $1      Final Position: Gami Chicken

==================================================      GAME TWO        ==================================================
The winner is: Peter with $10!!

The results:
        Name: Peter     Total Money:    $10     Final Position: YOMG
        Name: Billy     Total Money:    $8      Final Position: GO
        Name: Charlotte Total Money:    $-1     Final Position: Lanzhou Beef Noodle
        Name: Sweedal   Total Money:    $7      Final Position: GO
```

There are a few test files named in the form "test_<Module>.py". These run some tests against the methods of the corresponding module.

# Design
The game was created using Object Oriented programming using Python. Python was chosen for ease of reading JSON files, and faster implementation.

I initially tried in Java, however, because Python has builtin libraries to read in JSON files, I picked Python.

The design of the game will involve objects, mainly:

  1. Players
  2. Squares - the squares of the game board
  3. Game - This is the main object which creates the game with Player and Square objects.

These objects are explained further below.

## Player
A Player of the game has the following attributes:

  * name
  * totalMoney
  * currentPos - current position on the board. Everyone starts on GO so initially this is set to 0.

A Player object has the following abilities:

  * Earn money (from rent, or passing GO)
  * Check if bankrupt
  * Spend money (buying property or paying rent)

## Square
A Square object represents one square of the board. A Square has the following attributes:

  * name
  * price (except for GO)
  * colour (except for GO)
  * type - type of square either "go" or "property"
  * owner - None initially.
  * rent (except for GO) - If the Square is of type "property" and is owned, then rent attribute is positive.

A Square has the following abilities:

  * Being bought by a player
  * Double rent - if a Player owns all properties of the same colour.
  * Check if owned - is the property on the Square currently owned?

## Game
A Game consists of a list of Squares and Players.

Game has following attributes:

  * Check if any player is bankrupt
  * Announce the winning player and the final results when game ends - determined by the Player with the most money.
  * Keep track of the current player
  * Keep track of the current move (this is a predetermined game)
  * Move the current player by a specified amount of moves
  * Check if any player owns all properties of one colour => set rent accordingly for all corresponding squares

A Game is played until one of the following two occurs:

  1. A player is bankrupt
  2. There are no more moves to play

The Squares on the board have a corresponding index, with "GO" being at index 0 and "Massizim" being at index 8.

# Game Play
The game logic will be implemented as follows.

  1. First check if any player is bankrupt or if there are no more moves to play.
     a. If either condition is met => Quit the game and announce the winner and final results.
  2. Get the next Player whose turn it is.
  3. Get the amount of moves [x] that the Player must take.
  4. Move the Player to the Square [x] units away from the Player's current position => update Player's current position.
    a. If the destination Square is beyond the total number of squares (length of the list of Squares) then wrap around.
  5. Check the Square for a pre-existing owner:
    a. If Square is owned, charge current Player rent => Reduce current player's totalMoney by amount equal to 'rent' attribute of Square and increase owner's money by the rent amount.
    b. If Square is not owned, then Player buys property => Reduce current player's totalMoney by amount equal to "price" attribute of Square => change ownership property of Square and initialise rent of the property (default set to the price of the property).
  6. Go to step 1.

## Main
The file `Main.py` runs the game. It is the file that assigns the turns and moves each player. It also instructs the game to process any transactions (buying property or paying rent).

This file also creates the players, loads the moves and initialises a game with the newly created players and moves.

## Assumptions
  * Initial rent was not specified in the specifications so the rent of a bought property is set to the price of the property. For example, when property "YOMG" is bought by a player for $3, the rent for "YOMG" will be set to $3.
