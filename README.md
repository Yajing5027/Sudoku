# SudoSudoku game project, supporting learning gameplay and classic game modes.

## File Structure
- `main.py`: Main program file: game flow, puzzle generate/load, game loop.
- `generator.py`: generating puzzles, generating complete board, random cell remove, loading predefined puzzle.
- `checker.py`: check validity and solution status of Sudoku board, no external dependencies
- `display.py`: displaying board, saving results to file
- `puzzles.txt`: predefined puzzle data file.
- `README.md`: project description.

## Gameplay
1. Run `python main.py`.
2. Choose mode:
   - **Learning gameplay**: generate puzzle 20% blanks, so it's easy to fill, no fixed answer, no unique solution.
   - **Start the game**: select difficulty (Simple to Hell), load predefined puzzles.
3. View the displayed board (_ for blanks, [number] for user inputs).
4. Input format:
   - row,col,number (e.g., 1,2,5) to fill a number
   - r,row,col (e.g., r,1,2) to remove a filled number
5. If valid, board updates; else error message.
6. Continue until completed or enter 'start' to begin the game.
7. When completed, print "Congratulations! Puzzle completed.", save results to `results.txt`.

## Run
Ensure `puzzles.txt` file exists. Run `python main.py` to start.