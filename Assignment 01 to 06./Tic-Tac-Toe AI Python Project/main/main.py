import os
import time

# Function to print the game board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    print("\n🎮 Welcome to Tic-Tac-Toe AI 🤖\n")
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

# Minimax Algorithm for AI
def minimax(board, is_maximizing):
    if check_winner(board, 'O'):  # AI wins
        return 1
    elif check_winner(board, 'X'):  # Player wins
        return -1
    elif is_board_full(board):  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI move
                score = minimax(board, False)
                board[i] = ' '  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:  # Player's turn
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Player move
                score = minimax(board, True)
                board[i] = ' '  # Undo move
                best_score = min(score, best_score)
        return best_score

# AI chooses the best move
def ai_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI move
            score = minimax(board, False)
            board[i] = ' '  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Main game function
def play_game():
    board = [' '] * 9  # Empty board
    game_over = False

    print("🆚 You (X) vs AI (O) 🤖")
    time.sleep(1)

    while not game_over:
        print_board(board)

        # Player's turn
        move = input("🟢 Your turn! Choose a position (1-9): ")
        
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
            else:
                print("❗ Spot already taken! Choose another.")
                time.sleep(2)
                continue
        else:
            print("❗ Invalid input! Choose a number between 1-9.")
            time.sleep(2)
            continue

        # Check if player wins
        if check_winner(board, 'X'):
            print_board(board)
            print("🎉 You Win! 🏆")
            game_over = True
            break
        elif is_board_full(board):
            print_board(board)
            print("😔 It's a Draw!")
            game_over = True
            break

        # AI's turn
        print("\n🤖 AI is thinking...")
        time.sleep(2)
        ai_best_move = ai_move(board)
        board[ai_best_move] = 'O'

        # Check if AI wins
        if check_winner(board, 'O'):
            print_board(board)
            print("😢 AI Wins! Better luck next time! 🤖")
            game_over = True
            break
        elif is_board_full(board):
            print_board(board)
            print("😔 It's a Draw!")
            game_over = True
            break

    # Ask for replay
    play_again = input("🔄 Play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("👋 Thanks for playing! See you next time!")

# Start the game
play_game()

