from enum import Enum

class SnakeDirection(Enum):
    Left = (0,-1)
    Top = (-1, 0)
    Right = (0, 1)
    Bottom = (1, 0)