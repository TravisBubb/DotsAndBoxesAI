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
The core of the AI agent is a simple minimax algorithm with alpha-beta pruning. Minimax was used since it is a fairly simply algorithm and supports the structure of the game - two player, turn-based game. The algorithm takes in a game state and desired depth, and it loops through all open board positions and their successors to see which path will yield the most desirable outcome. To evaluate the different possible moves, the outcomes are weighed simply by how many points the AI player will have after a given sequence of moves.

## AI Results
One of the biggest issues that was found with the implementation of the AI agent was that it is not very efficient and doesn't allow for a very large depth as a result of that. For the 3x3 board the AI works great with a maximum tree depth of 3 and 4. For the 4x4 board, a depth of 3 worked well and 4 was playable but not the fastest gameplay. Anything over a board size of 4x4 is too slow to enjoy playing the game.  

Another issue that was discovered with using the minimax approach was that it works well during the mid-to-late game but not so well during the early game. Due to the nature of minimax, and utilizing a depth limit, it is more difficult for the agent to determine what moves are good in the early game when there are little to no moves already present on the board.

## Project Status 
As of now, this project is not being worked on. However, it may be that a different methodology is implemented to form a more desirable AI agent. I am currently in a higher-level artificial intelligence course that covers more advanced topics like reinforcement learning, machine learning, deep learning, and more. It may turn out that I am able to use these new concepts that I learn to create a better agent.  

Something else I would also like to do is implement this project in another language that is more sensitive to speed like C++. It would be interesting to see if merely changing the language the project is written in would affect the depth I am able to go into the tree and thus the agent could make better decisions.
