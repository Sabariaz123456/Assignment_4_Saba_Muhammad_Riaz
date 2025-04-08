import pygame
import random

# Initialize Pygame
pygame.init()

# Screen size
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Grid size
COLS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],                # I
    [[1, 0, 0], [1, 1, 1]],        # J
    [[0, 0, 1], [1, 1, 1]],        # L
    [[1, 1], [1, 1]],              # O
    [[0, 1, 1], [1, 1, 0]],        # S
    [[0, 1, 0], [1, 1, 1]],        # T
    [[1, 1, 0], [0, 1, 1]],        # Z
]

# Helper function to rotate the shape
def rotate(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

# Class to represent a Tetromino block
class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def image(self):
        return self.shape

    def rotate(self):
        self.shape = rotate(self.shape)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Initialize grid
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# Check if move is valid
def valid_space(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = off_x + x
                new_y = off_y + y
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return False
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return False
    return True

# Clear completed rows
def clear_rows(grid, locked):
    cleared = 0
    for y in range(ROWS - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared += 1
            del_row(grid, locked, y)
    return cleared

def del_row(grid, locked, row):
    for x in range(COLS):
        del locked[(x, row)]
    for y in range(row - 1, -1, -1):
        for x in range(COLS):
            if (x, y) in locked:
                locked[(x, y + 1)] = locked.pop((x, y))

# Draw the grid
def draw_grid(surface, grid):
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for x in range(COLS):
        pygame.draw.line(surface, GRAY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(ROWS):
        pygame.draw.line(surface, GRAY, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))

# Draw current piece
def draw_piece(surface, piece):
    for y, row in enumerate(piece.image()):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    surface,
                    piece.color,
                    ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )

# Get a random new piece
def get_new_piece():
    index = random.randint(0, len(SHAPES) - 1)
    return Tetromino(3, 0, SHAPES[index], COLORS[index])

# Main game loop
def main():
    grid = create_grid()
    locked_positions = {}

    current_piece = get_new_piece()
    next_piece = get_new_piece()
    fall_time = 0
    fall_speed = 0.5
    run = True

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            current_piece.y += 1
            if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.image()):
                    for x, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = next_piece
                next_piece = get_new_piece()
                if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                    print("Game Over!")
                    run = False
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece.image(), grid, (current_piece.x, current_piece.y)):
                        # reverse rotate if invalid
                        for _ in range(3): current_piece.rotate()

        clear_rows(grid, locked_positions)

        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_piece(screen, current_piece)
        pygame.display.update()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()

