# checker.py: check validity and solution status of Sudoku board, no external dependencies

def is_move_valid(board, row, col, num, size):
    # check if a move is valid: ensure numbers in row, column, and 3x3 box, no repetition
    base = int(size**0.5)  # calculate size of 3x3 box (3 for 9x9)
    #checks the row
    if num in set(board[row]):
        return False
    #checks the col
    col_set = set()
    for r in range(size):
        col_set.add(board[r][col])
    if num in col_set:
        return False
    #checks the 3x3 boxes
    box_row = (row // base) * base
    box_col = (col // base) * base
    box_set = set()
    for r in range(box_row, box_row + base):
        for c in range(box_col, box_col + base):
            box_set.add(board[r][c])
    if num in box_set:
        return False
    return True

def is_solved(board, size):
    # check if puzzle is completely solved: ensure each row, column, and 3x3 box contains all numbers from 1 to size, no 0
    base = int(size**0.5)
    # Check each row
    for row in board:
        row_set = set(row)
        if len(row_set) != size or 0 in row_set:
            return False
    # Check each column
    for col in range(size):
        col_set = set(board[r][col] for r in range(size))
        if len(col_set) != size:
            return False
    # Check each 3x3 box
    for box_r in range(0, size, base):
        for box_c in range(0, size, base):
            box_set = set()
            for r in range(box_r, box_r + base):
                for c in range(box_c, box_c + base):
                    box_set.add(board[r][c])
            if len(box_set) != size:
                return False
    return True

def is_board_valid(board, size):
    # check if current board is valid: ignore 0, ensure no repetition in rows, columns, and boxes
    base = int(size**0.5)
    for row in range(size):
        row_list = [x for x in board[row] if x != 0]
        if len(set(row_list)) != len(row_list):
            return False
    for col in range(size):
        col_list = [board[r][col] for r in range(size) if board[r][col] != 0]
        if len(set(col_list)) != len(col_list):
            return False
    for box_r in range(0, size, base):
        for box_c in range(0, size, base):
            box_list = []
            for r in range(box_r, box_r + base):
                for c in range(box_c, box_c + base):
                    if board[r][c] != 0:
                        box_list.append(board[r][c])
            if len(set(box_list)) != len(box_list):
                return False
    return True 
