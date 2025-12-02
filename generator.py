# -*- coding: utf-8 -*-
# generator.py: generating puzzles, generating complete board, random cell remove, loading predefined puzzle.
 
import random

class Board:
    def __init__(self, size):
        self.size = size        # outer box size (4 or 9)
        self.base = int(size**0.5)       # inner box size = root of outer one (2 or 3), but will output floar, so must add int for later % operate
        self.board = []     # save final 2D list - answer
        self.blank_board = []   # save blanked 2D list - puzzle
        
    def complete_board(self):
        size = self.size
        base = self.base

        nums = [i for i in range(1, size+1)]        # set sudoku available numbers range and first row
        random.shuffle(nums)    # shuffle numbers of first row, to make different board each time

        # make 2D list
        row_list = []        # involve all row
        for row in range(size):
            each_row = []       # involve all col of one row
            for col in range(size):
                value = nums[((row * base + row // base + col) % size)]      # get index of nums by formula, then get value
                each_row.append(value)
            row_list.append(each_row)
         
        self.board = row_list       # renew board
        return self.board

    def load_puzzles(self):
        # loading predefined puzzles
        puzzles = [
            [[[8,7,0,0,0,0,1,2,6],[6,4,2,7,0,0,0,3,9],[5,0,0,2,6,0,0,4,0],[0,0,0,0,7,0,4,9,0],[0,0,5,9,0,2,6,0,0],[0,2,9,0,1,0,0,0,0],[0,1,0,0,5,6,0,0,4],[2,6,0,0,0,7,3,8,5],[3,5,7,0,0,0,0,6,1]], [[8,7,3,5,4,9,1,2,6],[6,4,2,7,8,1,5,3,9],[5,9,1,2,6,3,7,4,8],[1,3,6,8,7,5,4,9,2],[4,8,5,9,3,2,6,1,7],[7,2,9,6,1,4,8,5,3],[9,1,8,3,5,6,2,7,4],[2,6,4,1,9,7,3,8,5],[3,5,7,4,2,8,9,6,1]]],
            [[[0,6,4,0,0,0,5,8,0],[7,0,0,8,0,3,0,0,2],[8,0,0,0,5,0,0,0,9],[0,2,0,7,0,8,0,5,0],[0,0,7,0,0,0,2,0,0],[0,1,0,2,0,4,0,9,0],[9,0,0,0,2,0,0,0,5],[6,0,0,1,0,5,0,0,7],[0,7,5,0,0,0,8,1,0]], [[1,6,4,9,7,2,5,8,3],[7,5,9,8,4,3,1,6,2],[8,3,2,6,5,1,4,7,9],[4,2,6,7,9,8,3,5,1],[3,9,7,5,1,6,2,4,8],[5,1,8,2,3,4,7,9,6],[9,8,1,4,2,7,6,3,5],[6,4,3,1,8,5,9,2,7],[2,7,5,3,6,9,8,1,4]]],
            [[[0,0,0,2,0,0,8,0,1],[0,9,5,0,0,0,0,0,3],[0,0,0,9,0,4,0,0,7],[0,8,0,0,2,0,5,0,0],[0,0,2,0,7,0,9,0,0],[0,0,3,0,9,0,0,7,0],[8,0,0,6,0,3,0,0,0],[6,0,0,0,0,0,4,8,0],[7,0,1,0,0,9,0,0,0]], [[4,7,6,2,3,5,8,9,1],[2,9,5,1,8,7,6,4,3],[3,1,8,9,6,4,2,5,7],[9,8,7,3,2,1,5,6,4],[1,4,2,5,7,6,9,3,8],[5,6,3,4,9,8,1,7,2],[8,2,4,6,5,3,7,1,9],[6,3,9,7,1,2,4,8,5],[7,5,1,8,4,9,3,2,6]]],
            [[[2,0,4,0,5,0,0,0,0],[3,0,0,0,9,0,1,0,2],[0,7,0,8,1,0,0,0,0],[1,3,0,0,0,5,9,0,4],[6,0,0,0,0,0,0,0,3],[4,0,5,9,0,0,0,6,1],[0,0,0,0,4,1,0,5,0],[8,0,2,0,3,0,0,0,7],[0,0,0,0,2,0,6,0,9]], [[2,1,4,3,5,7,8,9,6],[3,5,8,4,9,6,1,7,2],[9,7,6,8,1,2,3,4,5],[1,3,7,2,6,5,9,8,4],[6,8,9,1,7,4,5,2,3],[4,2,5,9,8,3,7,6,1],[7,9,3,6,4,1,2,5,8],[8,6,2,5,3,9,4,1,7],[5,4,1,7,2,8,6,3,9]]],
            [[[4,0,7,0,0,0,0,0,0],[0,0,0,0,3,7,0,8,0],[5,0,3,0,0,0,0,2,0],[0,0,0,0,0,8,0,1,7],[0,5,0,0,0,0,0,0,6],[0,0,0,6,0,9,0,0,0],[0,0,2,0,5,0,8,0,0],[7,1,0,0,0,0,4,0,0],[0,0,0,2,0,0,6,0,0]], [[4,2,7,5,1,6,3,8,9],[9,6,1,4,3,7,5,8,2],[5,8,3,9,7,2,1,2,6],[3,9,5,2,4,8,6,1,7],[2,5,8,7,1,3,9,4,6],[1,7,4,6,2,9,8,3,5],[6,3,2,1,5,4,8,7,9],[7,1,9,8,6,5,4,2,3],[8,4,5,2,9,1,6,5,8]]]
        ]
        return puzzles

    def remove_cells(self, blank_percent):
        # Randomly remove a specified percentage of cells to create a puzzle
        size = self.size
        total_cells = size * size  # total number of cells
        to_remove = int(total_cells * blank_percent)  # number of cells to remove
        cells = [(r, c) for r in range(size) for c in range(size)]  # all cell coordinates
        random.shuffle(cells)  # shuffle coordinates randomly
        self.blank_board = [row[:] for row in self.board]      # deep copy the complete board as puzzle base
        for r, c in cells[:to_remove]:  # remove the first to_remove cells
            self.blank_board[r][c] = 0
        return self.blank_board
    

    def generate_puzzle(self, blank_percent=0.2):  # Added to integrate
        # generate puzzle
        self.complete_board()  # generate complete board
        self.remove_cells(blank_percent)  # remove percentage of cells
        return self.blank_board  # return puzzle board
        

if __name__ == "__main__":
    board1 = Board(9)
    print(board1.complete_board())
    print(board1.remove_cells(0.1))

