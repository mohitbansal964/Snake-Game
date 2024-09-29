class SnakeNode:
    """
    SnakeNode represents a node in the snake's body for a grid-based snake game.
    
    Attributes:
        row_idx (int): The row index of the node in the grid.
        col_idx (int): The column index of the node in the grid.
        next (SnakeNode): The next node in the snake's body.
        prev (SnakeNode): The previous node in the snake's body.
    """

    def __init__(self, r_idx: int, c_idx: int):
        """
        Initializes a new instance of the SnakeNode class.

        Args:
            r_idx (int): The row index of the node in the grid.
            c_idx (int): The column index of the node in the grid.
        """
        self.row_idx = r_idx
        self.col_idx = c_idx
        self.next = None
        self.prev = None



    

    