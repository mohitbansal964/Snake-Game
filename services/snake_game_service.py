import sys
from typing import List, Tuple
from enums.difficulty_level_enum import DifficultyLevel
from enums.snake_direction_enum import SnakeDirection
from models.snake_node import SnakeNode
from enums.grid_status_enum import GridStatus
from random import randint
from threading import Timer

class SnakeGame:
    """
    SnakeGame represents the main game logic for a grid-based snake game.
    
    Attributes:
        __snake_dir (SnakeDirection): The current direction of the snake.
        __grid (List[List[GridStatus]]): The grid representing the game board.
        __snake_head (SnakeNode): The head node of the snake.
        __snake_tail (SnakeNode): The tail node of the snake.
        __difficulty_level (DifficultyLevel): The difficulty level of the game.
        __game_thread (Timer): The timer controlling the snake's movement.
    """

    def __init__(self):
        """
        Initializes a new instance of the SnakeGame class.
        """
        self.__snake_dir: SnakeDirection = SnakeDirection.Left
        self.__grid: List[List[GridStatus]] = []
        self.__snake_head: SnakeNode = None
        self.__snake_tail: SnakeNode = None
        self.__difficulty_level: DifficultyLevel = DifficultyLevel.Medium
        self.__game_thread: Timer = None
    
    def set_game_parameters(self, m: int, n: int, difficulty_level: DifficultyLevel = DifficultyLevel.Medium) -> None:
        """
        Sets the game parameters including grid size and difficulty level.

        Args:
            m (int): Number of rows in the grid.
            n (int): Number of columns in the grid.
            difficulty_level (DifficultyLevel): The difficulty level of the game.
        """
        self.__grid = [[GridStatus.Empty for _ in range(n)] for _ in range(m)]
        self.__snake_head = self.__snake_tail = SnakeNode(m // 2, n // 2)
        self.__grid[m // 2][n // 2] = GridStatus.Occupied
        self.__difficulty_level = difficulty_level
        self.__set_next_food_position()
    
    def play(self) -> None:
        """
        Starts the game and handles user input for snake direction.
        """
        print("Enter snake direction: (A for Left, W for Top, D for Right, S for Bottom): ")
        self.__continue_snake_movement()
        while True:
            snake_dir_input = input().strip().upper()
            if not self.__game_thread.is_alive():
                break
            if snake_dir_input in ['A', 'W', 'D', 'S']:
                self.__snake_dir = self.__map_input_to_direction(snake_dir_input)
            else:
                self.__game_thread.join()
                break

    def __map_input_to_direction(self, input_char: str) -> SnakeDirection:
        """
        Maps the input character to the corresponding SnakeDirection.

        Args:
            input_char (str): The input character representing the direction.

        Returns:
            SnakeDirection: The corresponding SnakeDirection.
        """
        direction_map = {
            'A': SnakeDirection.Left,
            'W': SnakeDirection.Top,
            'D': SnakeDirection.Right,
            'S': SnakeDirection.Bottom
        }
        return direction_map[input_char]

    def __continue_snake_movement(self):
        """
        Continues the snake's movement in the current direction.
        """
        nxt_r, nxt_c = self.__get_next_node()
        m, n = len(self.__grid), len(self.__grid[0])
        if 0 > nxt_r or nxt_r >= m or 0 > nxt_c or nxt_c >= n or self.__grid[nxt_r][nxt_c] == GridStatus.Occupied:
            print("Game Lost!!")
            sys.exit()
            return
        else:
            if self.__grid[nxt_r][nxt_c] == GridStatus.Food:
                print("Food Eaten!!")
                self.__set_next_food_position()
                self.__move_snake_head(nxt_r, nxt_c)
            else:
                self.__move_snake_head(nxt_r, nxt_c)
                self.__move_snake_tail()
        self.__print_grid()
        self.__game_thread = Timer(self.__difficulty_level.value, self.__continue_snake_movement)
        self.__game_thread.start()
    
    def __print_grid(self):
        """
        Prints the current state of the grid.
        """
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                print(self.__grid[i][j].value, end=" ")
            print()
        print("*" * 20)

    def __get_next_node(self) -> Tuple[int, int]:
        """
        Gets the next node position based on the current direction.

        Returns:
            Tuple[int, int]: The row and column indices of the next node.
        """
        cur_r, cur_c = self.__snake_head.row_idx, self.__snake_head.col_idx
        return (cur_r + self.__snake_dir.value[0], cur_c + self.__snake_dir.value[1])

    def __move_snake_head(self, new_r_idx: int, new_c_idx: int) -> None:
        """
        Moves the snake's head to a new position.

        Args:
            new_r_idx (int): The new row index for the snake's head.
            new_c_idx (int): The new column index for the snake's head.
        """
        self.__grid[new_r_idx][new_c_idx] = GridStatus.Occupied
        new_node = SnakeNode(new_r_idx, new_c_idx)
        new_node.next = self.__snake_head
        self.__snake_head.prev = new_node
        self.__snake_head = new_node 

    def __move_snake_tail(self) -> None:
        """
        Moves the snake's tail forward.
        """
        self.__grid[self.__snake_tail.row_idx][self.__snake_tail.col_idx] = GridStatus.Empty
        prev_node = self.__snake_tail.prev
        if prev_node is not None:
            prev_node.next = None
        self.__snake_tail.prev = None
        del self.__snake_tail
        self.__snake_tail = prev_node

    def __set_next_food_position(self) -> None:
        """
        Sets the next food position on the grid.
        """
        m, n = len(self.__grid), len(self.__grid[0])
        possible_position = (randint(0, m - 1), randint(0, n - 1))
        while self.__grid[possible_position[0]][possible_position[1]] != GridStatus.Empty:
            possible_position = (randint(0, m - 1), randint(0, n - 1))
        self.__grid[possible_position[0]][possible_position[1]] = GridStatus.Food
