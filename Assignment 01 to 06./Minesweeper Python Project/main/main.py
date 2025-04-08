import random
import os

# Game Settings
GRID_SIZE = 8  # Grid size (8x8)
NUM_MINES = 10  # Number of mines

# Symbols
MINE = "💣"
FLAG = "🚩"

# Function to create the Minesweeper board
def create_board():
    board = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    return board

# Function to place mines randomly
def place_mines(board):
    mine_positions = set()
    while len(mine_positions) < NUM_MINES:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        mine_positions.add((row, col))

    return mine_positions

# Function to count adjacent mines
def count_adjacent_mines(board, mine_positions, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if (nr, nc) in mine_positions:
            count += 1
    return count

# Function to reveal a cell
def reveal_cell(board, mine_positions, row, col, revealed):
    if (row, col) in revealed:
        return
    if (row, col) in mine_positions:
        board[row][col] = MINE  # Show mine
        return

    num_mines = count_adjacent_mines(board, mine_positions, row, col)
    board[row][col] = str(num_mines) if num_mines > 0 else "."

    # If no mines nearby, recursively reveal neighboring cells
    if num_mines == 0:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),         (0, 1),
                      (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                reveal_cell(board, mine_positions, nr, nc, revealed)

    revealed.add((row, col))

# Function to display the board
def print_board(board, show_mines=False):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print("\n🎮 **Minesweeper Game** 💣\n")

    # Column numbers
    print("   " + " ".join([str(i) for i in range(GRID_SIZE)]))
    print("  " + "---" * GRID_SIZE)

    for i, row in enumerate(board):
        row_display = f"{i} | " + " ".join(row)
        print(row_display)

    print("\n🚩 Use 'F row col' to flag a cell (e.g., 'F 2 3')")
    print("📍 Enter row & column to reveal (e.g., '2 3')")

# Function to check win condition
def check_win(board, mine_positions):
    safe_cells = GRID_SIZE * GRID_SIZE - NUM_MINES
    revealed_count = sum(row.count(".") + row.count("1") + row.count("2") + row.count("3") +
                         row.count("4") + row.count("5") + row.count("6") + row.count("7") +
                         row.count("8") for row in board)
    return revealed_count == safe_cells

# Main game function
def play_game():
    board = create_board()
    mine_positions = place_mines(board)
    revealed = set()
    flagged = set()

    while True:
        print_board(board)

        # Player input
        user_input = input("\n👉 Enter row & col (or flag 'F row col'): ").strip().split()

        if len(user_input) == 3 and user_input[0].upper() == "F":
            try:
                row, col = int(user_input[1]), int(user_input[2])
                if (row, col) in flagged:
                    flagged.remove((row, col))
                    board[row][col] = " "
                else:
                    flagged.add((row, col))
                    board[row][col] = FLAG
            except ValueError:
                print("❗ Invalid input! Try again.")
                continue

        elif len(user_input) == 2:
            try:
                row, col = int(user_input[0]), int(user_input[1])
                if (row, col) in mine_positions:
                    print_board(board, show_mines=True)
                    print("\n💥 BOOM! You hit a mine! Game Over. 💀\n")
                    break
                reveal_cell(board, mine_positions, row, col, revealed)
            except ValueError:
                print("❗ Invalid input! Try again.")
                continue

        else:
            print("❗ Invalid command! Use 'row col' or 'F row col'.")
            continue

        # Check win condition
        if check_win(board, mine_positions):
            print_board(board)
            print("\n🎉 Congratulations! You cleared the minefield! 🎯🏆\n")
            break

# Run the game
play_game()

