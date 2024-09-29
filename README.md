# Snake Game

Classic Snake Game implemented in Python.

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Further Enhancements](#further-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project is a classic Snake Game implemented in Python. The game is played on a grid where the player controls a snake to eat food and grow in length. The game ends if the snake runs into the walls or itself. The difficulty level can be adjusted to make the game more challenging.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/mohitbansal964/Snake-Game.git
    cd Snake-Game
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

## Usage

To start the game, run the following command:

```sh
python main.py
```
You will be prompted to enter the snake's direction using the following keys:

* A or a for Left
* W or w for Top
* D or d for Right
* S or s for Bottom
To exit the game, input any other key.


## Code Structure
The project is organized into several modules to adhere to the SOLID principles and enhance maintainability.
```
Snake-Game/
│
├── enums/
│   ├── difficulty_level_enum.py
│   ├── grid_status_enum.py
│   └── snake_direction_enum.py
│
├── models/
│   └── snake_node.py
│
├── services/
│   └── snake_game_service.py
│
├── main.py
└── README.md
```

### Enums
* **difficulty_level_enum.py**: Defines the DifficultyLevel enum for setting game difficulty.
* **grid_status_enum.py**: Defines the GridStatus enum for representing the status of grid cells.
* **snake_direction_enum.py**: Defines the SnakeDirection enum for representing the snake's direction.
### Models
* **snake_node.py**: Defines the SnakeNode class representing a node in the snake's body.
### Services
* **snake_game_service.py**: Contains the SnakeGame class, which encapsulates the main game logic.
### Main
* **main.py**: The entry point of the application. Initializes and starts the game.

## Further Enhancements
1. **Command-Line Arguments**: Modify the script to accept command-line arguments for grid size and difficulty level.
2. **Pause and Resume**: Implement functionality to pause and resume the game.
3. **Score Tracking**: Add a scoring system to track the player's score based on the number of food items eaten.
4. **Save and Load Game**: Implement functionality to save the game state and load it later.
5. **Enhanced User Interface**: Improve the user interface to provide better feedback and controls.
6. **Unit Testing**: Add unit tests to ensure the correctness of the game's behavior.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/mohitbansal964/Snake-Game/blob/main/LICENSE) file for details.

