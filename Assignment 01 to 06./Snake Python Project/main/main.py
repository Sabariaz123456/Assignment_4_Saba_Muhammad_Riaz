import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set window size
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake block size and speed
block_size = 20
snake_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_display(score):
    value = score_font.render("Score: " + str(score), True, red)
    win.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], block_size, block_size])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            win.fill(blue)
            msg = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            win.blit(msg, [width / 6, height / 3])
            score_display(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Check boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        score_display(snake_length - 1)

        pygame.display.update()

        # Check food collision
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

