import sys
from copy import deepcopy


class Utils:
    """Library class with useful functions for the project"""

    def is_completion(state, move):
        """Checks if a move makes a completion and counts how many completions are made

        Parameters:
            state (dict): The game state object
            move (tuple): A tuple of two integers that represents the (x,y) of a move

        Return:
            completions (int): The number of completions made by the given move in the given state

        """

        completions = 0
        lines = set(state[1]) | set(state[2])
        (x, y) = move

        # Horizontal Line
        if x % 2 == 1:
            # Bottom completion
            if (
                (x - 1, y - 1) in lines
                and (x + 1, y - 1) in lines
                and (x, y - 2) in lines
            ):
                completions += 1
            # Top completion
            if (
                (x - 1, y + 1) in lines
                and (x + 1, y + 1) in lines
                and (x, y + 2) in lines
            ):
                completions += 1

        # Vertical Line
        if x % 2 == 0:
            # Left-side completion
            if (
                (x + 1, y - 1) in lines
                and (x + 1, y + 1) in lines
                and (x + 2, y) in lines
            ):
                completions += 1
            # Right-side completion
            if (
                (x - 1, y - 1) in lines
                and (x - 1, y + 1) in lines
                and (x - 2, y) in lines
            ):
                completions += 1

        return completions

    def make_move(state, move, player, ai_prev_score, player_prev_score):
        """Add a move to the game state and increment score as needed

        Parameters:
            state (dict): The current game state object
            move (tuple): A tuple of two integers that represents the (x,y) of a move
            player (Player | AI): The player object or AI object who is making the move
            ai_prev_score (int): The AI player's score before the move occurs
            player_prev_score (int): The human player's score before the move occurs

        Return:
            result (dict): The new game state object after the move has been added,
            completions (int): The number of completions that were made as a result of the move

        """

        result = deepcopy(state)
        completions = Utils.is_completion(state, move)
        result[result["player"]].append(move)

        if player.get_nick() == "AI":
            total = ai_prev_score + completions
            player.set_score(max(total, player.get_score()))
        else:
            total = player_prev_score + completions
            player.set_score(max(total, player.get_score()))

        # player.set_score(player.get_score() + completions)
        return result, completions

    def terminal_test(state, moves):
        """Determine whether or not there are any valid moves left on the board

        Parameters:
            state (dict): The current game state object
            moves (list): All of the valid moves left on the board

        Return:
            True if no valid moves left, otherwise False

        """

        return len(moves) == 0

    def valid_moves(state):
        """Generate all of the valid moves given a game state

        Parameters:
            state (dict): The current game state object

        Return:
            result (list): A list of tuples where each tuple is a valid move (x,y)

        """

        result = []
        [x_dim, y_dim] = state["board_size"]

        # Create a list of all possible moves regardless of the state
        for i in range(0, (x_dim * 2) + 1):
            for j in range(0, (y_dim * 2) + 1):
                if (i % 2 == 0 and j % 2 == 1) or i % 2 == 1 and j % 2 == 0:
                    result.append((i, j))

        # Remove any moves that are already taken in the game state
        result = [
            m
            for m in result
            if (m not in state[1]) and (m not in state[2]) and m != ("0", "0")
        ]
        return result

    def process_data(data, line, player_num):
        """Process given data and add the player's current positions to the state

        Parameters:
            data (dict): The game state that is being built from a state file
            line (str): A line of text from a state file to process
            player_num (int): The number that ties a player to the given board positions (1 or 2)

        Return:
            data (dict): The game state that was represented in the given file

        """

        # Verify that the given data line corresponds with the desired player
        if f"p{player_num}:" in line:
            positions = line.split(f"p{player_num}: ")
            if len(positions) == 2:  # If there is n >= 1 board position for the player

                # Add the board positions for the player to the state.
                # Turn the ordered pairs into tuples (e.g., "(1, 2)" -> tuple('1', '2'))
                data[player_num] = list(
                    map(
                        lambda x: tuple(x.replace("(", "").replace(")", "").split(",")),
                        positions[1].split(" "),
                    )
                )
                # Cast all of the board position values to tuples of ints from strings
                data[player_num] = list(
                    map(lambda x: (int(x[0]), int(x[1])), data[player_num])
                )
            else:  # There are no given board positions for the player
                data[player_num] = []
        return data

    def read_state_file(file):
        """Read a file and parse the game state information contained within

        Parameters:
            file (str): The name of the file that contains game state information

        Return:
            data (dict): The game state that was represented in the given file

        """

        try:  # Attempt to open the game state file
            f = open(file)
        except Exception as err:
            print(err)
            print(f"Error opening game-state file: {file}")
            sys.exit(0)

        data = {}

        # Read through the file and parse the information
        for line in f.readlines():
            line = line.strip()

            # Add the board dimensions to the state - [x_dim, y_dim]
            if "B=" in line:
                data["board_size"] = list(
                    map(lambda x: int(x), line.split("=")[1].split("x"))
                )

            # Add player one's current board positions
            data = Utils.process_data(data.copy(), line, 1)

            # Add player two's current board positions
            data = Utils.process_data(data.copy(), line, 2)
        f.close()

        # Add the current player's turn
        if len(data[1]) == len(data[2]):
            data["player"] = 1
        else:
            data["player"] = 2

        return data
