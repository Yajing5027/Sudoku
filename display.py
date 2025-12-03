# display.py: displaying board with row/col index, saving result to file.

class Sudoku:
    # Sudoku class: handle show board and save result
    # Sudoku
    def __init__(self):
        # Init Sudoku instance (no need extra setting now)
        pass

    def display_board(self, board, original_board=None):
        # Show sudoku board: print row number, col number, user input use [ ] wrap (if original_board give)
        size = len(board)  # get board size
        print("   " + " ".join("C" + str(i+1) for i in range(size)))  # print col title
        for i in range(size):
            row_str = "R" + str(i+1) + " "  # build row string
            for j in range(size):
                value = board[i][j]
                if value == 0:
                    row_str += "_  "  # empty show _
                else:
                    if original_board and original_board[i][j] == 0:
                        row_str += "[" + str(value) + "] "  # user input use [ ]
                    else:
                        row_str += str(value) + "  "  # original number normal show
            print(row_str)  # print whole row

    def save_to_file(self, board, filename):
        # Save board to file: each row one line
        with open(filename, 'w') as f:
            for row in board:
                f.write(','.join([str(x) for x in row]) + '\n')  # change row , separate string
