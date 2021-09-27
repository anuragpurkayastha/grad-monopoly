# Woven Monopoly

As part of the coding test for Pronto Software Graduate Program, I needed to build a small application that plays a game of woven Monopoly.

# Design

The game will be created using Object Oriented programming. The game will consist of objects described below.

## Player

A Player of the game has the following attributes:

  * name
  * totalMoney

A Player object has the following abilities:

  * Earn money (from rent, or passing GO)
  * Check if bankrupt
  * Spend money (buying property)
  * Check if owns all properties of same colour

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

## Board

A Board object is made up of Square objects, which will be stored in an array.

## Game

A Game consists of a Board and Players. Players are stored in an array.
