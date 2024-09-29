from enums.difficulty_level_enum import DifficultyLevel
from services.snake_game_service import SnakeGame


if __name__ == "__main__":
    game = SnakeGame()
    game.set_game_parameters(10, 10, DifficultyLevel.Medium)
    game.play()