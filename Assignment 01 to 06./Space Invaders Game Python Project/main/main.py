import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Set icon (use placeholder if image not found)
try:
    icon = pygame.image.load('spaceship.png')  # Replace with your actual icon
except:
    icon = pygame.Surface((32, 32))
    icon.fill((255, 255, 255))  # White square
pygame.display.set_icon(icon)

# Player
try:
    player_img = pygame.image.load('player.png')  # Replace with actual image
except:
    player_img = pygame.Surface((64, 64))
    player_img.fill((0, 255, 0))  # Green block
player_x = 370
player_y = 480
player_x_change = 0

# Enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    try:
        enemy_img.append(pygame.image.load('enemy.png'))
    except:
        temp_img = pygame.Surface((64, 64))
        temp_img.fill((255, 0, 0))  # Red block
        enemy_img.append(temp_img)
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

# Bullet
try:
    bullet_img = pygame.image.load('bullet.png')
except:
    bullet_img = pygame.Surface((8, 32))
    bullet_img.fill((255, 255, 0))  # Yellow bullet
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"

# Score
score = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Functions
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 28, y + 10))

def is_collision(ex, ey, bx, by):
    distance = math.hypot(ex - bx, ey - by)
    return distance < 27

# Game Loop
running = True
while running:
    screen.fill((0, 0, 30))  # Dark background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_x_change = 0

    # Update player position
    player_x += player_x_change
    player_x = max(0, min(player_x, 736))

    # Enemy movement
    for i in range(num_of_enemies):
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over = pygame.font.Font(None, 64).render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over, (250, 250))
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= 736:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        # Collision
        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    player(player_x, player_y)
    show_score()
    pygame.display.update()

