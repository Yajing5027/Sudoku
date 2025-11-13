import random

class Board:
    def __init__(self,size):
        self.size = size        # outer box size (4 or 9)
        self.base = int(size**0.5)       # inner box size = root of outer one (2 or 3), but will output floar, must add int for later % operate
        self.board = []     # save final 2D list
        
    def complete_board(self):
        size = self.size
        base = self.base

        nums = [i for i in range(1,size+1)]        # set sudoku available numbers range

        # make 2D list
        row_list =[]        # involve all row
        for row in range(size):
            each_row = []       # involve all col of one row
            for col in range(size):
                value = ((row * base + row // base + col) % size) + 1
                each_row.append(value)
            row_list.append(each_row)
        
        self.board = row_list       # renew board
        return self.board

'''        def shuffle_board(self):
        random.shuffle()

    def blank_board(self):'''
        

board1 = Board(9)
print(board1.complete_board())


