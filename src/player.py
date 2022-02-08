import random
from utils import Utils


class Player:
    """Class to represent a player object

    Attributes:
        Score (int): The player's score for the game
        Player_num (int): The player's number for the game (either 1 or 2)
        Positions (list): A list of tuples where each tuple is a line the player has made
        Nick (str): The player's nickname

    """

    def __init__(self, player_no, nick="Human", positions=[]):
        """Create a new player object and initialize attributes

        Parameters:
            player_no (int): The player's number for the game
            nick (str): The player's nickname (default = 'Human')
            positions (list): The player's current positions (default = [])

        """

        self.Score = 0
        self.Player_num = player_no
        self.Positions = positions
        self.Nick = nick

    def get_random_move(self, state):
        """Generate a random move to make

        Parameters:
            state (dict): The current game state

        Return:
            A tuple of two integers - a random selection from the valid moves list

        """

        return random.choice(Utils.valid_moves(state))

    def get_move(self, state):
        """Get the player's move selection from standard input

        Parameters:
            state (dict): The current game state

        Return:
            (x,y): The coordinates of the move the player wants to make

        """

        # Get the valid moves
        moves = Utils.valid_moves(state)
        x, y = -1, -1

        # Loop until valid input is provided by the player
        while True:
            valid = True
            are_ints = True
            m = input("Make a move - x y (e.g. 2 5):\t")

            move = m.split()

            # Check that the input is only 2 values
            if len(move) != 2:
                print(
                    "Incorrect number of inputs. Please enter 2 integer values separated by a space."
                )
                valid = False
                continue

            # check that the input is only integer values
            for s in move:
                if not (
                    s.isdigit()
                    and int(s) >= 0
                    and int(s) <= (state["board_size"][0] * 2) + 1
                ):
                    print(
                        "Please only enter integer values in the proper range of the board."
                    )
                    valid = False
                    are_ints = False
                    break

            # Check that the values are within the correct bounds for the board size
            if are_ints:
                move = [int(i) for i in move]
                if tuple(move) not in moves:
                    print(
                        f"({move[0]}, {move[1]}) is not a valid move. Please enter a new move."
                    )
                    valid = False
                    continue

            # If the input is valid, break out of the loop and return the move
            if valid:
                x, y = move
                break
        return (x, y)

    def get_positions(self):
        """Get the list of moves the player has made

        Return:
            Positions (int): The player's Positions attribute

        """

        return self.Positions

    def get_nick(self):
        """Get the player's nickname

        Return:
            Nick (str): The player's Nick attribute

        """

        return self.Nick

    def set_score(self, new_score):
        """Set the player's score attribute

        Parameters:
            new_score (int): The player's new score

        """

        self.Score = new_score

    def get_score(self):
        """Get the player's current score

        Return:
            Score (int): The player's current score attribute

        """

        return self.Score

    def get_player_num(self):
        """Get the player's player number

        Return:
            Player_num (int): The player's Player_num attribute

        """

        return self.Player_num