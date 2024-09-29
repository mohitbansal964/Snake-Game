from enum import Enum

class DifficultyLevel(Enum):
    """
    An enumeration to represent different difficulty levels with associated numerical values.
    
    Attributes:
    -----------
    Easy : int
        Represents the 'Easy' difficulty level with a value of 4.
    Medium : int
        Represents the 'Medium' difficulty level with a value of 2.
    Hard : int
        Represents the 'Hard' difficulty level with a value of 1.
    """
    Easy = 4
    Medium = 2
    Hard = 1