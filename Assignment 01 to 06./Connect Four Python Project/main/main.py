import numpy as np
import pygame
import sys
import math

# Initialize Pygame
pygame.init()
pygame.font.init()  # Explicitly initialize the font system

# Define constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
myfont = pygame.font.SysFont("monospace", 75)

# Create the board using numpy
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), int)

# Drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if the column is valid for a drop
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Get the next available row for a piece to fall in a column
def get_next_available_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Print the board (For debugging purposes)
def print_board(board):
    print(np.flip(board, 0))

# Check if there is a win (4 in a row)
def winning_move(board, piece):
    # Horizontal check
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Vertical check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Positive diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True

    # Negative diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

# Draw the game board
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (c * SQUARESIZE + SQUARESIZE // 2, r * SQUARESIZE + SQUARESIZE + SQUARESIZE // 2), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARESIZE + SQUARESIZE // 2, HEIGHT - (r * SQUARESIZE + SQUARESIZE // 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARESIZE + SQUARESIZE // 2, HEIGHT - (r * SQUARESIZE + SQUARESIZE // 2)), RADIUS)

    pygame.display.update()

# Main game loop
def main():
    global screen, WIDTH, HEIGHT
    WIDTH = COLUMN_COUNT * SQUARESIZE
    HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Connect Four")

    board = create_board()
    print_board(board)
    draw_board(board)

    game_over = False
    turn = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, RED if turn % 2 == 0 else YELLOW, (posx, SQUARESIZE // 2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                col = posx // SQUARESIZE

                if is_valid_location(board, col):
                    row = get_next_available_row(board, col)
                    piece = 1 if turn % 2 == 0 else 2
                    drop_piece(board, row, col, piece)

                    if winning_move(board, piece):
                        label = myfont.render(f"Player {piece} wins!", 1, RED if piece == 1 else YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        board = create_board()
                        draw_board(board)
                        turn = 0
                        continue

                    draw_board(board)
                    turn += 1

# Corrected entry point
if __name__ == "__main__":
    main()


