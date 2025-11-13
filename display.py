class Sudoku:
 def __init__(self):
   self.board=self.generate_board()
 def generate_board(self):
    board = [
    [0, 2, 7, 1, 0, 4, 3, 9, 0],
    [0, 6, 5, 3, 2, 0, 1, 0, 8],
    [3, 4, 1, 0, 0, 8, 7, 0, 2],
    [5, 0, 3, 4, 0, 1, 0, 2, 7],
    [4, 7, 2, 8, 3, 5, 9, 6, 1],
    [6, 0, 8, 9, 7, 0, 4, 3, 5],
    [7, 8, 0, 0, 1, 9, 5, 0, 4],
    [1, 5, 0, 7, 8, 6, 2, 0, 9],
    [2, 0, 9, 5, 4, 0, 6, 7, 0]
]
        

    return board
 def display_board(self):
  print("   C1 C2 C3 C4 C5 C6 C7 C8 C9")
  for i in range(9):
    print(f'R{i+1} ',end="")
    for j in range(9):
      value=self.board[i][j]
      if value == 0:
         print("_", end="  ")  # show underscore for blanks
      else:
         print(value, end="  ")

    print()  # move to next li
soduku=Sudoku()
soduku.display_board()
