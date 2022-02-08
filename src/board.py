class Board:
    """Class to represent the Dots and Boxes game board

    Attributes:
        size (int): The size of the board
        state (dict): The game state that the board uses for display purposes

    """

    def __init__(self, size=4):
        """Initialize a new board object; Initialize the board's attributes

        Parameters:
            size (int): The desired size of the board - default=4

        """

        self.size = size
        self.state = {}

    def __str__(self):
        """Compute and return a string representation of the board object

        Return:
            res (str): A string representing the board; Used to display the game board

        """

        res = ""

        # Combine both players' moves into one set
        lines = set(self.state[1]) | set(self.state[2])

        # Add the top x-axis labels to the result string
        res += "{:2}".format("")  # Add the offset to the column label row
        for x in range(0, (self.size * 2) + 1):
            res += "{x:>3}".format(x=x)
        res += "\n" * 2

        # Add the rest of the grid to the result string
        label = 0
        for row in range(0, (self.size * 2) + 1):
            # Add the row labels to the string
            res += "{row_num:<4}".format(row_num=row)
            for col in range(0, (self.size * 2) + 1):
                if col % 2 == 0 and row % 2 == 1 and (col, row) not in lines:
                    res += "{:6}".format("")
                if (col, row) in lines:
                    if col % 2 == 0 and row % 2 == 1:
                        res += "{:6}".format("|")
                    elif col % 2 == 1 and row % 2 == 0:
                        res += "-----"
                elif (col + 1, row) in lines and row % 2 == 0:
                    res += "*"
                elif col % 2 == 0 and row % 2 == 0:
                    res += "{:6}".format("*")
            res += "\n" * 2
        return res

    def update(self, state):
        """Update the board with a new game state

        Parameters:
            state (dict): The new game state object

        """

        self.state = state