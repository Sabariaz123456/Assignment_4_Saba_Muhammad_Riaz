# 🧩 Sudoku Solver using Backtracking Algorithm

def print_board(board):
    """Prints the Sudoku board in a readable format."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty_cell(board):
    """Finds an empty cell (0) in the Sudoku board."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # Return row, col
    return None  # No empty cells

def is_valid(board, num, pos):
    """Checks if a number is valid in a given position."""
    row, col = pos

    # Check row
    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True  # Valid move

def solve(board):
    """Solves the Sudoku puzzle using backtracking."""
    empty_cell = find_empty_cell(board)
    
    if not empty_cell:
        return True  # Solved!
    
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # Try placing the number

            if solve(board):  # Recursive call
                return True

            board[row][col] = 0  # Reset if invalid

    return False  # Backtrack

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("\n🔢 **Sudoku Puzzle:**")
print_board(sudoku_board)

if solve(sudoku_board):
    print("\n✅ **Solved Sudoku:**")
    print_board(sudoku_board)
else:
    print("\n❌ No solution found.")

