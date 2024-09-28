import sys
from typing import List, Tuple
from difficulty_level import DifficultyLevel
from snake_direction_enum import SnakeDirection
from snake_node import SnakeNode
from grid_status_enum import GridStatus
from random import randint
from threading import Timer

class SnakeGame:
    def __init__(self):
        self.__snake_dir: SnakeDirection = SnakeDirection.Left
        self.__grid: List[List[GridStatus]] = []
        self.__snake_head: SnakeNode = None
        self.__snake_tail: SnakeNode = None
        self.__difficulty_level: DifficultyLevel = DifficultyLevel.Medium
        self.__game_thread: Timer = None
    
    def set_game_parameters(self, m: int, n: int, difficulty_level: DifficultyLevel = DifficultyLevel.Medium):
        self.__grid = [[GridStatus.Empty for _ in range(n)] for _ in range(m)]
        self.__snake_head = self.__snake_tail = SnakeNode(m//2, n//2)
        self.__grid[m//2][n//2] = GridStatus.Occupied
        self.__difficulty_level = difficulty_level
        self.__set_next_food_position()
    
    def play(self):
        print("Enter snake direction: (A for Left, W for Top, D for Right, S for bottom): ")
        self.__continue_snake_movement()
        while True:
            snake_dir_input = input()
            if not self.__game_thread.is_alive():
                break
            match snake_dir_input:
                case "A":
                    self.__snake_dir = SnakeDirection.Left
                case "a":
                    self.__snake_dir = SnakeDirection.Left
                case "W":
                    self.__snake_dir = SnakeDirection.Top
                case "w":
                    self.__snake_dir = SnakeDirection.Top
                case "D":
                    self.__snake_dir = SnakeDirection.Right
                case "d":
                    self.__snake_dir = SnakeDirection.Right
                case "S":
                    self.__snake_dir = SnakeDirection.Bottom
                case "s":
                    self.__snake_dir = SnakeDirection.Bottom
                case _:
                    self.__game_thread.join()
                    break
            

    def __continue_snake_movement(self):
        nxt_r, nxt_c = self.__get_next_node()
        m, n = len(self.__grid), len(self.__grid[0])
        if 0 > nxt_r or nxt_r >= m or 0 > nxt_c or nxt_c >= n or self.__grid[nxt_r][nxt_c] == GridStatus.Occupied:
            print("Game Lost!!")
            sys.exit()
            return
        else:
            if self.__grid[nxt_r][nxt_c] == GridStatus.Food:
                print("Eaten Food!!")
                self.__set_next_food_position()
                self.__move_snake_head(nxt_r, nxt_c)
            else:
                self.__move_snake_head(nxt_r, nxt_c)
                self.__move_snake_tail()
        self.__print_grid()
        self.__game_thread = Timer(self.__difficulty_level.value, self.__continue_snake_movement)
        self.__game_thread.start()
    
    def __print_grid(self):
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[i])):
                print(self.__grid[i][j].value, end=" ")
            print()
        print("*"*20)

    def __get_next_node(self) -> Tuple[int]:
        cur_r, cur_c = self.__snake_head.row_idx, self.__snake_head.col_idx
        return (cur_r + self.__snake_dir.value[0], cur_c + self.__snake_dir.value[1])

    def __move_snake_head(self, new_r_idx, new_c_idx) -> None:
        self.__grid[new_r_idx][new_c_idx] = GridStatus.Occupied
        new_node = SnakeNode(new_r_idx, new_c_idx)
        new_node.next = self.__snake_head
        self.__snake_head.prev = new_node
        self.__snake_head = new_node 

    def __move_snake_tail(self) -> None:
        self.__grid[self.__snake_tail.row_idx][self.__snake_tail.col_idx] = GridStatus.Empty
        prev_node = self.__snake_tail.prev
        if prev_node is not None:
            prev_node.next = None
        self.__snake_tail.prev = None
        del self.__snake_tail
        self.__snake_tail = prev_node

    def __set_next_food_position(self) -> Tuple[int]:
        m, n = len(self.__grid), len(self.__grid[0])
        possible_position = (randint(0, m-1), randint(0, n-1))
        while self.__grid[possible_position[0]][possible_position[1]] != GridStatus.Empty:
            possible_position = (randint(0, m-1), randint(0, n-1))
        self.__grid[possible_position[0]][possible_position[1]] = GridStatus.Food

        
