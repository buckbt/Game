import pygame
import sys
from player import Player
from game_parameters import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The adventures of sentient brick")
clock = pygame.time.Clock()

# Set up player
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height - player_height - 10
player_speed = 5
jump_height = 11
is_jumping = False
jump_count = 11
# Adjust gravity as needed

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT] and player_x > player_speed:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width - player_speed:
        player_x += player_speed

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

    # Apply gravity
    if player_y < height - 2*player_height:
        player_y += GRAVITY
    if player_y > height - player_height:
        player_y = height - player_height

    # Update display
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, player_width, player_height))  # Blue player rectangle

    pygame.display.flip()
    clock.tick(60)
