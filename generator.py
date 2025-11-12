import random

class board:
    def __init__(self,size):
        self.size = size
        self.base = size**0.5
        num = []
        
    def complete_board(self):
        col_list =[i + 1 for i in range(self.size)]
        row_list =[i + 1 for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                (i * base + i // base + j) % size


        def shuffle_board(self):
            random.shuffle()

    def blank_board(self):
        

board1 = board(9)


