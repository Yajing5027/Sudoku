from generator import Board
from checker import is_valid_move, is_solved
from display import display_board
def main():
    game = Board(9)
    game.complete_board()
    board = game.remove_cells()

    print("Welcome to Sudoku!")
    display_board(board)

    while not is_solved(board):
        print("\nMake a move:")
        row = int(input("Row (0-8): "))
        col = int(input("Column (0-8): "))
        num = int(input("Number (1-9): "))

        if is_valid_move(board, row, col, num):
            board[row][col] = num
            print("\nUpdated Board:")
            display_board(board)
        else:
            print("❌ Invalid move, try again!")

    print("\n🎉 You solved the Sudoku! 🎉")

if __name__ == "__main__":
    main()



