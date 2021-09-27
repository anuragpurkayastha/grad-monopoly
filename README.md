# Woven Monopoly

As part of the coding test for Pronto Software Graduate Program, I needed to build a small application that plays a game of woven Monopoly.

# Design

The game will be created using Object Oriented programming using Python. Python was chosen for ease of reading JSON files, and faster implementation.

I initially tried in Java, however, because Python has builtin libraries to read in JSON files, I picked Python.

The design of the game will involve objects, mainly:

  1. Players
  2. Squares - the squares of the game board
  3. Game - This is the main object which instantatiates Player and Square objects.

These objects are explained further below.

## Player

A Player of the game has the following attributes:

  * name
  * totalMoney

A Player object has the following abilities:

  * Earn money (from rent, or passing GO)
  * Check if bankrupt
  * Spend money (buying property)

## Square

A Square object represents one square of the board. A Square has the following attributes:

  * name
  * price (except for GO)
  * colour (except for GO)
  * type
  * owner
  * rent (except for GO) - If the Square is of type "property" and is owned, then rent attribute is positive.

A Square has the following abilities:

  * Being bought by a player (change the owner attribute)
  * Increase rent - if a Player owns all properties of the same colour.

## Board

A Board object is made up of Square objects, which will be stored in an array.

## Game

A Game consists of a list of Squares and Players.

Game has following attributes:

  * Check if any player is bankrupt
  * Announce the winning player when game ends - determined by the Player with the most money.
  * Determine next player - to make the next move
  * Determine next move - how many moves should the player move?
  * Check if any player owns all properties of one colour => set rent accordingly for all corresponding squares

A Game is played until one of the two occurs:

  1. A player is bankrupt
  2. There are no more moves to play

# Game Play
The game logic will be implemented as follows.

  1. First check if any player is bankrupt or if there are no more moves to play.
    a. If either condition is met => Quit the game and announce the winner.
  2. Get the Player whose turn it is.
  3. Get the amount of moves [x] that the Player must take.
  4. Move the Player to the Square [x] units away from the Player's current position.
    a. If the destination Square is beyond the total number of squares (length of the list of Squares) then wrap around.
  5. Check the Square for a pre-existing owner:
    a. If Square is owned, charge current Player rent => Reduce current players totalMoney by amount equal to 'rent' attribute of Square.
    b. If Square is not owned, then Player buys property => Reduce current player's totalMoney by amount equal to "price" attribute of Square.
