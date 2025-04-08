import os
import time

# Function to print the board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console (works on both Windows and Unix)
    print("Tic-Tac-Toe 🎮\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Function to check for a winner
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([spot != ' ' for spot in board])

# Game logic
def play_game():
    board = [' '] * 9  # Empty board
    current_player = 'X'  # Player X starts
    game_over = False

    print("Welcome to **Tic-Tac-Toe** 🏆")
    print("Instructions: Choose a position (1-9) to place your mark (X or O).")

    while not game_over:
        print_board(board)

        # Ask for player's move
        move = input(f"Player {current_player}, choose a position (1-9): ")

        # Check if the move is valid (between 1-9 and not taken)
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1  # Convert to 0-based index
            if board[move] == ' ':
                board[move] = current_player
            else:
                print("❗ This spot is already taken. Choose another one.")
                time.sleep(2)
                continue
        else:
            print("❗ Invalid input. Choose a number between 1 and 9.")
            time.sleep(2)
            continue

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🏆")
            game_over = True
        elif is_board_full(board):
            print_board(board)
            print("It's a draw! 😔")
            game_over = True
        else:
            # Switch to the next player
            current_player = 'O' if current_player == 'X' else 'X'

        time.sleep(1)

    # Ask if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing! 👋")

# Start the game
play_game()


