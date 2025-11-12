def is_move_valid(self,row,col,num):
  #checks the row
  if number in self.board[row]:
    return False
  #checks the col
  for r in range(9):
    if self.board[r][col] == num:
      return False
  #checks the 3x3 boxes
  box_row = (row // 3) * 3
  box_col = (col // 3) * 3
  for r in range(box_row, box_row +3):
    for c in range(box_col, bow_col +3):
      if self.board[r][c] == num:
        return False
      
