import os
import sys


class Board:
    def __init__(self, rows, columns, bombs):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board = [["#" for _ in range(columns)] for _ in range(rows)]
        self.complete_board = self.init_complete_board()

    def init_complete_board(self):
        complete_board = [["-" for _ in range(self.columns)] for _ in range(self.rows)]

        for row, col in self.bombs:
            complete_board[row][col] = "*"
            for r_offset in [-1, 0, 1]:
                for c_offset in [-1, 0, 1]:
                    r = row + r_offset
                    c = col + c_offset
                    if (
                        0 <= r < self.rows
                        and 0 <= c < self.columns
                        and complete_board[r][c] != "*"
                    ):
                        if complete_board[r][c] == "-":
                            complete_board[r][c] = "1"
                        else:
                            complete_board[r][c] = str(int(complete_board[r][c]) + 1)

        return complete_board

    def reveal_position(self, pos_row, pos_col):
        try:
            if self.board[pos_row][pos_col] == "#":
                self.board[pos_row][pos_col] = self.complete_board[pos_row][pos_col]

                if self.board[pos_row][pos_col] == "*":
                    clear_console()
                    self.print_board()
                    print("\nBoom! Game Over.")
                    return True

                if self.board[pos_row][pos_col] == "-":
                    for row_displacement in [-1, 0, 1]:
                        for col_displacement in [-1, 0, 1]:
                            row_displaced = pos_row + row_displacement
                            col_displaced = pos_col + col_displacement
                            if (
                                0 <= row_displaced < self.rows
                                and 0 <= col_displaced < self.columns
                            ):
                                self.reveal_position(row_displaced, col_displaced)
        except:
            print("Error: Invalid position.")

        return self.has_won()

    def has_won(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.complete_board[row][col] == "*" and self.board[row][col] != "#":
                    return False
                elif (
                    self.complete_board[row][col] != "*"
                    and self.complete_board[row][col] != self.board[row][col]
                ):
                    return False

        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == "#":
                    self.board[row][col] = "*"
        clear_console()
        self.print_board()
        print("\nVictory!")
        return True

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()


def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value < max_value:
                return value
            print("Invalid input: Value is out of bounds.")
        except ValueError:
            print("Invalid input: Please enter a valid integer.")


def play(game_board: Board):
    end_game = False
    while not end_game:
        clear_console()
        game_board.print_board()
        print("\nSelect a position to reveal...")

        row = get_valid_input("Row: ", 0, game_board.rows)
        col = get_valid_input("Column: ", 0, game_board.columns)

        end_game = game_board.reveal_position(row, col)


def validate_bombs(rows, cols, bombs):
    for bomb in bombs:
        if not all(isinstance(x, int) for x in bomb):
            raise ValueError("\nInvalid bomb position: Non-integer value found.")
        if not (0 <= bomb[0] < rows) or not (0 <= bomb[1] < cols):
            raise ValueError("\nInvalid bomb position: Out of bounds.")


def read_game_configuration_from_file(filename):
    try:
        with open(filename, "r") as file:
            rows = int(file.readline().strip())
            cols = int(file.readline().strip())
            bombs_str = file.readline().strip()
            bombs = [list(map(int, bomb.split(","))) for bomb in bombs_str.split(";")]
            return rows, cols, bombs
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except (ValueError, IndexError):
        print(f"Error: Invalid format in file '{filename}'.")
        sys.exit(1)


def create_game():
    print("Enter the filename containing the game configuration:")

    filename = input("Filename: ")

    rows, cols, bombs = read_game_configuration_from_file(filename)

    print("\nGame configuration loaded successfully:\n")
    print(f"Rows: {rows}")
    print(f"Cols: {cols}")
    print(f"Number of bombs: {len(bombs)}")

    try:
        validate_bombs(rows, cols, bombs)
    except ValueError as error:
        print(error)
        sys.exit(1)

    game_board = Board(rows, cols, bombs)

    print("\nGame created!")
    input("Press any key to continue...")
    return game_board


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    print("--------------------------------")
    print("-------- Minefield Game --------")
    print("--------------------------------")

    game_board = create_game()
    play(game_board)


if __name__ == "__main__":
    main()
