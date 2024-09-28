from difficulty_level import DifficultyLevel
from snake_game import SnakeGame


if __name__ == "__main__":
    game = SnakeGame()
    game.set_game_parameters(10, 10, DifficultyLevel.Medium)
    game.play()