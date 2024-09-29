from enums.difficulty_level_enum import DifficultyLevel
from services.snake_game_service import SnakeGame

if __name__ == "__main__":
    """
    Main entry point for the Snake game.
    
    This script initializes the SnakeGame with specified parameters and starts the game.
    """
    # Initialize the game
    game = SnakeGame()
    
    # Set game parameters: grid size (10x10) and difficulty level (Medium)
    game.set_game_parameters(10, 10, DifficultyLevel.Medium)
    
    # Start the game
    game.play()
