import pygame
import sys
from game_parameters import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer with Jump")
clock = pygame.time.Clock()

# Set up player
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height - player_height - 10

jump_height = 100
is_jumping = False
jump_count = 13

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x > PLAYER_VELOCITY:
        player_x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player_x < width - player_width - PLAYER_VELOCITY:
        player_x += PLAYER_VELOCITY

    # Jump mechanic
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Update display
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))  # Blue player rectangle

    pygame.display.flip()
    clock.tick(60)
