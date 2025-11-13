class Sudoku:
 def __init__(self):
   self.board=self.generate_board()
 def generate_board(self):
    board = [
        [1, 0, 3, 4],
        [0, 3, 0, 1],
        [3, 4, 1, 0],
        [0, 1, 0, 2]
    ]
    return board
 def display_board(self):
  print("   C1 C2 C3 C4")
  for i in range(4):
    print(f'R{i+1} ',end="")
    for j in range(4):
      value=self.board[i][j]
      if value == 0:
         print("_", end="  ")  # show underscore for blanks
      else:
         print(value, end="  ")

    print()  # move to next li
soduku=Sudoku()
soduku.display_board()
