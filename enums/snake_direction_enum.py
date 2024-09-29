from enum import Enum

class SnakeDirection(Enum):
    """
    SnakeDirection is an enumeration representing the direction of movement for a snake in a grid-based game.
    
    Attributes:
        Left (tuple): Represents the direction to the left, denoted by the tuple (0, -1).
        Top (tuple): Represents the direction upwards, denoted by the tuple (-1, 0).
        Right (tuple): Represents the direction to the right, denoted by the tuple (0, 1).
        Bottom (tuple): Represents the direction downwards, denoted by the tuple (1, 0).
    """
    Left = (0, -1)
    Top = (-1, 0)
    Right = (0, 1)
    Bottom = (1, 0)
