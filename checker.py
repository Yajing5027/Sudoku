def is_move_valid(board,row,col,num):
  #checks the row
  if num in self.board[row]:
    return False
  #checks the col
  for r in range(9):
    if self.board[r][col] == num:
      return False
  #checks the 3x3 boxes
  box_row = (row // 3) * 3
  box_col = (col // 3) * 3
  for r in range(box_row, box_row +3):
    for c in range(box_col, box_col +3):
      if self.board[r][c] == num:
        return False
  return True

def is_solved(board):
    # Check each row
    for row in board:
        if sorted(row) != list(range(1, 10)):
            return False

    # Check each column
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if sorted(column) != list(range(1, 10)):
            return False

    # Check each 3x3 box
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for r in range(3):
                for c in range(3):
                    box.append(board[box_row + r][box_col + c])
            if sorted(box) != list(range(1, 10)):
                return False

    return True

    
    


