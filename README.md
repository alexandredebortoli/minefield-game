# minefield-game

This project is an implementation of the classic game "Minesweeper" in Python, designed to be played in a terminal environment. Inspired by the Windows Minesweeper game, the objective is to create a fun and challenging gaming experience. The game board is loaded from a configuration file, allowing for customizable gameplay.

## Game Rules

In Minesweeper, the game area consists of a rectangular grid of squares. Each square can be revealed by selecting it. The game revolves around avoiding squares that contain hidden mines, as revealing one of these squares ends the game. If a selected square does not contain a mine, one of the following outcomes occurs:

1. A number appears, indicating the number of adjacent squares that contain mines.
1. No number appears. In this case, the game automatically reveals adjacent squares, as they cannot contain mines.

The objective is to reveal all squares that do not contain mines, ultimately winning the game.

## Features

- Customizable Board: The game allows for different board configurations, including various sizes (N x M) and mine placements. The board configuration is loaded from a text file at the start of the game.

- Interactive Terminal Gameplay: Players interact with the game through the terminal, inputting their choices to reveal squares and navigate the minefield.

- Winning and Losing: The game determines whether the player has won or lost based on their choices. Winning occurs when all non-mine squares are revealed, while revealing a mine results in a loss.

## Getting Started

To run the game locally, follow these steps:

1. Clone the project

    ```bash
      git clone https://github.com/alexandredebortoli/minefield-game.git
    ```

1. Go to the project directory

    ```bash
      cd minefield-game
    ```
    
1. Create a .txt game file in the root directory to contain the board configuration or use the existing example file example-game.txt. The file should have the following structure (without the comments):
   
    ``` txt
    5 # Number of rows
    10 # Number of columns
    1,1;2,2 # Bomb positions, separating row and column by ',' and positions by ';'
    ```
    
1. Run the application with:

    ``` bash
    python3 minefield.py
    ```
    
1. Upon starting the application, you will be prompted to insert the game configuration file path, like this:
   
    ``` bash
    Filename: example-game.txt
    ```
    
1. The game board will load, and you can start playing.

## Dependecies

This Minesweeper project has no external dependencies, ensuring a straightforward setup and gameplay experience.

## Author

This project was developed by [@alexandredebortoli](https://github.com/alexandredebortoli) as part of an academic assignment.
