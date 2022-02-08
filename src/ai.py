#!/usr/bin/env python

import sys

from utils import Utils
from player import Player
from board import Board


class AI:
    """Class to represnt an AI player object

    Attributes:
        Score (int): The AI's score for the game
        Player_num (int): The AI's number for the game (either 1 or 2)
        Positions (list): A list of tuples where each tuple is a line the AI has made
        Nick (str): The AI's nickname

    """

    def __init__(self, player_no, positions=[]):
        """Create a new AI object and initialize attributes

        Parameters:
            player_no (int): The AI's number for the game
            positions (list): The AI's current positions (default = [])

        """

        self.Score = 0
        self.Player_num = player_no
        self.Positions = positions
        self.Nick = "AI"

    def minimax(
        self,
        state,
        depth,
        opponent,
        ai_prev_score,
        player_prev_score,
        maximize=True,
        alpha=-float("inf"),
        beta=float("inf"),
    ):
        """Minimax algorithm to determine what the agent's next move should be by comparing its own score
        and its opponent's score after the investigated sequence of moves

        Inspiration from pseudocode at https://en.wikipedia.org/wiki/Minimax

        Parameters:
            state (dict): The current game state object
            depth (int): The number of levels to go into the game tree
            opponent (Player): The opposing player object
            ai_prev_score (int): The AI's score before the function call
            player_prev_score (int): The opponent's score before the function call
            maximize (bool): Represents if maximizing or minimizing in the call (default = True)
            alpha (float): The "alpha" in alpha-beta pruning (default = -inf)
            beta (float): The "beta" in alpha-beta pruning (default = inf)

        Return:
          [
            move (tuple): The (x,y) coordinates of the best move,
            value (int): The score of the move; AI score - opponent score
          ]

        """

        moves = Utils.valid_moves(state)
        move = ()

        # Terminal test
        if len(moves) == 0 or depth == 0:
            return [move, self.get_score() - opponent.get_score()]

        move = moves[0]

        if maximize:
            # Initialize a variable to hold the best score and move
            v = -100
            good_move = move

            # Loop through all valid moves and attempt to find the best move
            for m in moves:
                s, completion = Utils.make_move(
                    state, m, self, ai_prev_score, player_prev_score
                )
                next_score = self.minimax(
                    s,
                    depth - 1,
                    opponent,
                    ai_prev_score,
                    player_prev_score,
                    completion,
                    alpha,
                    beta,
                )

                # Update the values for the best move and best score if the score is higher than previous
                if next_score[1] > v:
                    v = next_score[1]
                    good_move = m

                # Update alpha to be the current move's score if it is greater
                alpha = max(v, alpha)

                # If alpha is greater than beta, break out of the loop
                if alpha > beta:
                    break

            # Return the move and v+depth to incentivise earlier completions rather than later
            return [good_move, v + depth]
        else:
            # Variables to hold the worst score and move
            v = 100
            bad_move = move

            # Loop through all valid moves and attempt to find the best move for the opponent
            for m in moves:
                s, completion = Utils.make_move(
                    state, m, opponent, ai_prev_score, player_prev_score
                )
                next_score = self.minimax(
                    s,
                    depth - 1,
                    opponent,
                    ai_prev_score,
                    player_prev_score,
                    not completion,
                    alpha,
                    beta,
                )

                # Update the values for the worst move and score if the score is lower than the previous
                if next_score[1] < v:
                    v = next_score[1]
                    bad_move = m

                # Update beta
                beta = min(beta, v)

                # If alpha is greater than beta, break out of the loop
                if alpha > beta:
                    break

            return [bad_move, v - depth]

    def get_positions(self):
        """Get the list of moves the AI has made

        Return:
            Positions (int): The AI's Positions attribute

        """

        return self.Positions

    def set_score(self, new_score):
        """Set the AI's score attribute

        Parameters:
            new_score (int): The AI's new score

        """

        self.Score = new_score

    def get_score(self):
        """Get the AI's current score

        Return:
            Score (int): The AI's current score attribute

        """

        return self.Score

    def get_move(self, state, opp):
        """Get the AI's move selection by calling the minimax algorithm

        Parameters:
            state (dict): The current game state
            opp (Player): The opposing player object

        Return:
            move (tuple): The coordinates of the move the AI wants to make

        """

        prev_score = self.get_score()
        opp_score = opp.get_score()

        # Call minimax to get the best move - can change the depth to what is needed
        depth = 4
        move = self.minimax(state, depth, opp, prev_score, opp_score)

        self.set_score(prev_score)
        opp.set_score(opp_score)

        return move

    def get_player_num(self):
        """Get the AI's player number

        Return:
            Player_num (int): The AI's Player_num attribute

        """

        return self.Player_num

    def get_nick(self):
        """Get the AI's nickname

        Return:
            Nick (str): The AI's Nick attribute

        """

        return self.Nick


# If the ai.py file is being executed as main, output a single move for the AI
# given the name of a file containing a game state as a command-line argument
if __name__ == "__main__":
    # Usage clause
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <state file>")
        sys.exit(0)

    s = Utils.read_state_file(sys.argv[1])

    ai = AI("p2", s[2])
    player = Player("p1", s[1])
    B = Board(s["board_size"][0])
    B.update(s)
    print(B)
    [move, v] = ai.get_move(s, player)
    print("AI would choose move:", move)