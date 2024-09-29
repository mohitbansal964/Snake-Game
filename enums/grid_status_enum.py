from enum import Enum

class GridStatus(Enum):
    """
    GridStatus is an enumeration representing the status of a cell in a grid.
    
    Attributes:
        Empty (str): Represents an empty cell in the grid, denoted by "-".
        Occupied (str): Represents an occupied cell in the grid, denoted by "S".
        Food (str): Represents a cell containing food in the grid, denoted by "+".
    """
    Empty = "-"
    Occupied = "S"
    Food = "+"
