Author:           Travis Bubb
Professor:        Dr. Schwesinger
File:             README
Date:             December 15, 2021


This project is an implementation of the game Dots and Boxes. It allows the user to play against an
AI agent that uses the minimax algorithm to select its moves.


Execution (Full Game):
	python dab-engine.py <user player num> <board size>


Execution (AI - 1 move):
	python ai.py <filename>		: the file should contain a game state; see test-cases/* for formatting examples


Project Structure:
	ai.py			- The AI player for the game used in dab-engine; can also be run independently
	player.py		- The player class for the game
	board.py		- The board class for the game
	dab-engine.py	- The main game engine for dots and boxes
	utils.py		- The utilities library for the project
	test-cases/		- Folder to put test cases into
	