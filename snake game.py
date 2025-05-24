import pygame
import sys
import random

# Initialize
pygame.init()
WIDTH, HEIGHT = 400, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake setup
snake = [(100, 100)]
dx, dy = CELL, 0
food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

def show_game_over():
    msg = font.render("Game Over!", True, RED)
    screen.blit(msg, (WIDTH//2 - 80, HEIGHT//2 - 20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -CELL
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, CELL
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -CELL, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = CELL, 0

    # Move snake
    head = (snake[0][0] + dx, snake[0][1] + dy)
    if head in snake or not (0 <= head[0] < WIDTH and 0 <= head[1] < HEIGHT):
        show_game_over()
    snake.insert(0, head)

    # Eat food
    if head == food:
        food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()

    draw_snake()
    draw_food()

    pygame.display.flip()
    clock.tick(10)
