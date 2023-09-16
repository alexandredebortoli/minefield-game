class Board:
    def __init__(self, rows, columns, bombs):
        self.rows = rows
        self.columns = columns
        self.bombs = bombs
        self.board = [["#" for _ in range(columns)] for _ in range(rows)]
        self.complete_board = self.init_complete_board()

    def init_complete_board(self):
        complete_board = [["-" for _ in range(self.columns)] for _ in range(self.rows)]

        for pos in self.bombs:
            row = pos[0]
            col = pos[1]
            complete_board[row][col] = "*"

            for row_displacement in [-1, 0, 1]:
                for col_displacement in [-1, 0, 1]:
                    row_displaced = row + row_displacement
                    col_displaced = col + col_displacement

                    if (
                        0 <= row_displaced < self.rows
                        and 0 <= col_displaced < self.columns
                    ):
                        if complete_board[row_displaced][col_displaced] != "*":
                            if complete_board[row_displaced][col_displaced] == "-":
                                complete_board[row_displaced][col_displaced] = "1"
                            else:
                                complete_board[row_displaced][col_displaced] = str(
                                    int(complete_board[row_displaced][col_displaced])
                                    + 1
                                )

        return complete_board

    def reveal_position(self, pos_row, pos_col):
        try:
            if self.board[pos_row][pos_col] == "#":
                self.board[pos_row][pos_col] = self.complete_board[pos_row][pos_col]

                if self.board[pos_row][pos_col] == "*":
                    print("Boom! You lose.")
                    self.print_board()
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

        print("Victory!")
        return True

    def print_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()


def create_game():
    print("Loading board configuration...\n")

    rows = 5
    cols = 6
    bombs = [[1, 2], [0, 1]]
    num_bombs = len(bombs)
    print(f"Rows: { rows }")
    print(f"Cols: { cols }")
    print(f"Number of bombs: { num_bombs }")
    game_board = Board(rows, cols, bombs)

    print("\nBoard successfully created!")
    return game_board


def play(game_board: Board):
    end_game = False
    while not end_game:
        print("\n--------------------------------")
        game_board.print_board()
        print("\nSelect a position to reveal...")
        col = int(input("Column: "))
        row = int(input("Row: "))
        end_game = game_board.reveal_position(row - 1, col - 1)


def main():
    print("--------------------------------")
    print("-------- Minefield Game --------")
    print("--------------------------------")

    game_board = create_game()
    play(game_board)


if __name__ == "__main__":
    main()
