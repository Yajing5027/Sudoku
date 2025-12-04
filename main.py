# Main program file: game flow, puzzle generate/load, game loop.

from generator import Board  
from checker import is_move_valid, is_solved
from display import Sudoku

def start_game():
    # Start game function: let user select difficulty, load predefined puzzles, and game loop
    difficulty_names = {0: 'Simple', 1: 'Easy', 2: 'Hard', 3: 'Expert', 4: 'Hell'}  # Dictionary for difficulty names
    print("\nStart game, please select difficulty:")
    print("1. Simple")
    print("2. Easy")
    print("3. Hard")
    print("4. Expert")
    print("5. Hell")
    
    diff_choice = input("Please select difficulty (1-5): ")
    try:
        difficulty = int(diff_choice) - 1  # transfer to index (0-4)
        if 0 <= difficulty < 5:
            print(f"You selected: {difficulty_names[difficulty]}")  # Use dictionary to get name
            board_obj = Board(9)  # create 9x9 Board object
            puzzles = board_obj.load_puzzles()  # load predefined puzzles
            selected = puzzles[difficulty]  # select puzzle based on difficulty
            puzzle = selected[0]  # puzzle board (blanks)
            answer = selected[1]  # answer board (complete)
            
            display = Sudoku()  # create display object
            original_puzzle = [row[:] for row in puzzle]  # deep copy original puzzle
            display.display_board(puzzle, original_puzzle)  # display initial board
            
            while not (is_solved(puzzle, 9) and puzzle == answer):
                try:
                    inp = input("Please make a move: ").split(',')  # get user input, split to list
                    if len(inp) == 3 and inp[0].strip() != 'r':
                        # Handle filling number: row,col,number
                        row, col, num = [int(x.strip()) for x in inp]
                        row -= 1  # transfer to 0-based index
                        col -= 1
                        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9 and puzzle[row][col] == 0:
                            if is_move_valid(puzzle, row, col, num, 9):  # check if move is valid
                                puzzle[row][col] = num  # fill in number
                                display.display_board(puzzle, original_puzzle)  # update display
                                if is_solved(puzzle, 9) and puzzle == answer:  # check completed
                                    print("Congratulations! Puzzle completed.")
                                    display.save_to_file(puzzle, "results.txt")  # save results
                                    with open("results.txt", "r") as f:
                                        print("Saved result:")
                                        print(f.read())
                                    return
                            else:
                                print("Invalid: conflict")
                        else:
                            print("Error: position already filled or invalid")
                    elif len(inp) == 3 and inp[0].strip() == 'r':
                        # Handle removing number: r,row,col
                        row, col = [int(x) for x in inp[1:]]
                        row -= 1
                        col -= 1
                        if 0 <= row < 9 and 0 <= col < 9 and puzzle[row][col] != 0 and puzzle[row][col] != original_puzzle[row][col]:
                            puzzle[row][col] = 0  # remove
                            display.display_board(puzzle, original_puzzle)
                        else:
                            print("Cannot remove original numbers")
                    else:
                        print("Format error")
                except ValueError:
                    print("Invalid input, please try again")
        else:
            print("Invalid input, please try again")
            start_game() 
    except ValueError:
        print("Invalid input, please try again")
        start_game()

def main():
    # Main function: display welcome message, mode selection
    print("Welcome to Sudoku Game!")
    print("Please choose:")
    print("1. Learn the gameplay")
    print("2. Start the game")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        # Learn gameplay mode: generate simple puzzle for teaching
        # Sorry, I don't wanna remove my previous code, it spend my so long time, even though it couldn't make sure unique solution. So I just put it here as a demo for user learn gameplay.
        print("\nLearn the gameplay:")
        print("Rules: Numbers 1-9 cannot repeat in each row, column, or 3x3 block.")
        print("Input format:")
        print("  - row,col,number (e.g., 1,2,5) to fill a number")
        print("  - r,row,col (e.g., r,1,2) to remove a filled number")
        print("This board can be tried freely, no need to fully solve, no fixed answer, no unique solution.")
        print("Learned it? Then let's start.")
        
        board_obj = Board(9)  # create Board object
        puzzle = board_obj.generate_puzzle(blank_percent=0.2)  # generate puzzle 20% blanks, so it's easy to fill
        answer = None  # no fixed answer
        
        display = Sudoku()  # create display object
        original_puzzle = [row[:] for row in puzzle]  # record original puzzle
        display.display_board(puzzle, original_puzzle)  # display board
        
        # User input loop, can enter 'start' to begin the game
        while True:
            try:
                inp = input("Please make a move or enter 'start' to begin the game: ")
                if inp == 'start':
                    print("Entering the game...")
                    start_game()  # jump to start_game function
                    return
                inp = inp.split(',')
                if len(inp) == 3 and inp[0].strip() != 'r':
                    # Handle filling number: row,col,number
                    row, col, num = [int(x.strip()) for x in inp]
                    row -= 1
                    col -= 1
                    if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9 and puzzle[row][col] == 0:
                        if is_move_valid(puzzle, row, col, num, 9):
                            puzzle[row][col] = num
                            display.display_board(puzzle, original_puzzle)
                        else:
                            print("Invalid: conflict")
                    else:
                        print("Error: position already filled or invalid")
                elif len(inp) == 3 and inp[0].strip() == 'r':
                    # Handle removing number: r,row,col
                    row, col = [int(x) for x in inp[1:]]
                    row -= 1
                    col -= 1
                    if 0 <= row < 9 and 0 <= col < 9 and puzzle[row][col] != 0 and puzzle[row][col] != original_puzzle[row][col]:
                        puzzle[row][col] = 0
                        display.display_board(puzzle, original_puzzle)
                    else:
                        print("Cannot remove original numbers")
                else:
                    print("Format error")
            except ValueError:
                print("Invalid input, please try again")
    
    elif choice == "2":
        start_game()  # directly start the game
    else:
        print("Invalid choice, please try again")
        main()

if __name__ == "__main__":
    main()
