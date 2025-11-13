# still lack backdate to ensure only solution

import random

class Board:
    def __init__(self,size):
        self.size = size        # outer box size (4 or 9)
        self.base = int(size**0.5)       # inner box size = root of outer one (2 or 3), but will output floar, so must add int for later % operate
        self.board = []     # save final 2D list - answer
        self.blank_board = []   # save blanked 2D list - puzzle
        
    def complete_board(self):
        size = self.size
        base = self.base

        nums = [i for i in range(1,size+1)]        # set sudoku available numbers range and first row
        random.shuffle(nums)    # shuffle numbers of first row, to make different board each time

        # make 2D list
        row_list =[]        # involve all row
        for row in range(size):
            each_row = []       # involve all col of one row
            for col in range(size):
                value = nums[((row * base + row // base + col) % size)]      # get index of nums by formula, then get value
                each_row.append(value)
            row_list.append(each_row)
         
        self.board = row_list       # renew board
        return self.board

    def remove_cells(self):
        size = self.size
        base = self.base

        blank_num = (self.size * self.size // 2) // size      # set how many cells will be removed each row
        self.blank_board = [row[:] for row in self.board]      # make a deep copy, save original board as answer 

        for row in range(size):
            row_blank = random.sample(range(size),blank_num)      # get random index of blank cells
            for i in row_blank:
                self.blank_board[row][i] = 0      # blank the cell by signal to 0

        return self.blank_board


if __name__ == "__main__":
    board1 = Board(9)
    print(board1.complete_board())
    print(board1.remove_cells())
             

