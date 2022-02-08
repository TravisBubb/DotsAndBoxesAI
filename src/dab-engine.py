#!/usr/bin/python3

# Author:           Travis Bubb
# Description:      The game engine to play Dots and Boxes
# Professor:        Dr. Schwesinger
# File:             dab-engine.py
# Date:             December 15, 2021

from ai import AI
from player import Player
from utils import Utils
from board import Board
import sys


def play_game(B: Board, state, player: Player, ai: AI):
    """Execute the main game loop for Dots and Boxes
    
    Parameters:
        B (Board): The instance of the Board object being used for the game
        state (dict): The current game state data structure storing the size
                        of the board and all of the moves made by either player
        player (Player): The human/random player that is opposing the AI
        ai (AI): The artificial intelligence agent playing the game
                  
    Returns:
        None: Prints out the final score of the game
    
    """

    curr_player = player if player.get_player_num() == 1 else ai
    other_player = player if player.get_player_num() == 2 else ai
    print(B)
    
    # Main loop to run the game; run until the game is over
    while True:   
        if Utils.terminal_test(state, Utils.valid_moves(state)):
            break
        
        # Get player's move           
        if curr_player == player:
            move = curr_player.get_move(state)          # Comment to enable randome player & uncomment below line
            # move = curr_player.get_random_move(state) # Uncomment to enable the random player & comment above line
            print(f"Player made a line at {move}")
        
        # Calculate AI move
        else:
            [move, move_score] = curr_player.get_move(state, other_player)
            print(f"AI made a line at {move}")

        ai_prev_score = 0
        player_prev_score = 0
        
        # If it is the AI's turn, get appropriate previous scores
        if curr_player.get_nick() == 'AI':
            ai_prev_score = curr_player.get_score()
            player_prev_score = other_player.get_score()
        
        # If it is the player's turn, get appropriate previous scores
        else:
            ai_prev_score = other_player.get_score()
            player_prev_score = curr_player.get_score()
            
        # Make the move and update the game state
        state, completions = Utils.make_move(state, move, curr_player, ai_prev_score, player_prev_score)
        
        # If it is the AI's turn, set appropriate scores
        if curr_player.get_nick() == 'AI':
            curr_player.set_score(ai_prev_score + completions)
            other_player.set_score(player_prev_score)
         
        # If it is the player's turn, set appropriate scores
        else:
            curr_player.set_score(player_prev_score + completions)
            other_player.set_score(ai_prev_score)
        
        # If a completion was made, print a message stating such
        if completions > 0:
            print("-->A completion was made!")
            
        # If there was no completion made, switch to the next player's turn
        else:
            curr_player, other_player = other_player, curr_player
            state['player'] = 1 if state['player'] == 2 else 2
        
        # Print out the reuslts of the last move
        print(f'Player: {player.get_score()} | AI: {ai.get_score()}\n')
        B.update(state)
        print(B)
        
    # Print out the game's final scores
    print("\n\nFinal Scores:\n")
    print(f"AI: {ai.get_score()} | Player: {player.get_score()}")
    
    
def main():
    """Main function for the game engine; Collect the CLAs and start the game
    
    """

    # Verify command-line argument count
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <player num> <board size>')
        exit(-1)

    # Determine if the human player will be player 1 or 2
    P_NUM = int(sys.argv[1])
    if not(P_NUM == 1 or P_NUM == 2):
        print('ERROR: player number must be either 1 or 2.')
        exit(-1)
    
    # Set the AIs player number to what the player's number is not
    AI_NUM = 1 if P_NUM == 2 else 2

    # Create the board object
    BOARD_SIZE = int(sys.argv[2])
    if not(BOARD_SIZE > 2 and BOARD_SIZE < 7):
        print('ERROR: board size must be between 3-6 inclusive.')
        exit(-1)
    B = Board(BOARD_SIZE)
    
    # Create an AI player
    ai = AI(AI_NUM)
    
    # Create a human player
    player = Player(P_NUM)
    
    # Create an initial game state
    state = {
        'board_size': [BOARD_SIZE, BOARD_SIZE],
        'player': 1, 
        P_NUM: player.get_positions(), 
        AI_NUM: ai.get_positions()
        }
    B.update(state)
    print('Game Created...')
    print(f'Board Size: {BOARD_SIZE}')
    print(f'P_NUM: {P_NUM}')
    print(f'AI_NUM: {AI_NUM}')
    print(f'Starting State: {state}')
    
    
    # Run the game loop
    play_game(B, state, player, ai)
        
    
if __name__ == '__main__':
    exit(main())