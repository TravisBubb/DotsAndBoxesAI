# Dots and Boxes Game - AI Agent
Console-based dots and boxes implementation with a simple AI agent using Python3

## Table of Contents
* [General info](#general-info)
* [Project Structure](#project-structure)
* [Setup and Execution](#setup-and-execution)
* [AI Implementation](#ai-implementation)
* [AI Results](#ai-results)
* [Project Status](#project-status)

## General info
This project was submitted as a final project for an introductory level artificial intelligence course. This project consists of the infrastructure for the dots and boxes game, as well as an AI agent that plays the game. Dots and boxes is a game that consists of an m x n grid of dots. There are two players who take turns drawing a single line that connects two adjacent dots. Note that diagonal lines are not permitted in this game. The main goal of the game is to complete more squares than the opponent. To complete a square, a player must draw a line that completes the last edge of a 1x1 square of dots. If a player's move completes a square, they will continue to draw one line at a time until they make a move that is not a completion. For more details about the game, visit https://gametable.org/games/dots-and-boxes/ for a list of rules as well as a simple implementation of the game that can be played.  

This project initiates a game between an AI player and a real user and allows them to play against each other. The program takes input from the human player, during their turn, in the form of two integer values separated by a space. These values represent an x and a y value respectively, at which a line is drawn on the board. When it is the AI’s turn to make a move, it looks ahead to see possible branches of the game tree and evaluates the best possible move given the current state of the game. This project falls under the search category of classical artificial intelligence. The goal of the AI program is to be able to easily beat a random player and consistently beat an amateur human player. 

## Project Structure
```
README.md
src/
   |-- ai.py          // The AI player for the game; Can be executed independently
   |-- board.py       // The board class for the game
   |-- dab-engine.py  // The main game logic for dots and boxes
   |-- player.py      // The player class for the game
   |-- test-cases/    
   |   |-- test1.txt
   |   |-- test2.txt
   |-- utils.py       // The utilities library for the project

```

## Setup and Execution
Clone this repository onto your own machine to obtain the code for the project.  

#### Execution (Full Game):
```
$ python dab-engine.py <player num> <board size>
```
Note: Player num is the player number for the user and is either 1 or 2 (player 1 goes first). The recommended board size to use is 3; 4 is playable but it can be slow.  

#### Execution (AI only - 1 move):
```
$ python ai.py <filename>
```
Note: The file should contain a game state. Please see src/test-cases/* for formatting examples of game state files.

## AI Implementation

## AI Results

## Project Status 
