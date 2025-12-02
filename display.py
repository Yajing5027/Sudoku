# -*- coding: utf-8 -*-
# display.py: displaying board, saving results to file

class Sudoku:
    def __init__(self):
        # Initialize Sudoku instance (currently no additional set need)
        pass

    def display_board(self, board, original_board=None):
        # print row and column numbers, user inputs display with [ ] (if original_board provided)
        size = len(board)  # get board size
        print("   " + " ".join("C" + str(i+1) for i in range(size)))  # print column headers
        for i in range(size):
            row_str = "R" + str(i+1) + " "  # build row string
            for j in range(size):
                value = board[i][j]
                if value == 0:
                    row_str += "_  "  # show underscore for blanks
                else:
                    if original_board and original_board[i][j] == 0:
                        row_str += "[" + str(value) + "] "  # user inputs display with [ ]
                    else:
                        row_str += str(value) + "  "  # original numbers display normal
            print(row_str)  # print entire row

    def save_to_file(self, board, filename):
        # save board to file
        with open(filename, 'w') as f:
            for row in board:
                f.write(','.join(map(str, row)) + '\n')
