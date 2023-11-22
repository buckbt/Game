import pygame
from game_parameters import *
import random
from fish import Fish, fishes
from enemy import Enemy, enemies

def draw_background(screen):

    #load our tiles

    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()


    #use png transparency

    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))


    #fill screen

    for x in range(0,WIDTH,TILE):
        for y in range(0,HEIGHT,TILE):
            screen.blit(water,(x,y))

    #sand draw

    for x in range(0,WIDTH,TILE):
        screen.blit(sand,(x,HEIGHT-TILE))

    #add seagrass random
    for _ in range(7):
        x = random.randint(0,WIDTH)
        screen.blit(seagrass,(x, HEIGHT-2*TILE))

    custom_font = pygame.font.Font('../assets/fonts/CHECKBK0.ttf', 64)
    text = custom_font.render('Chomp', True,(255,0,0))
    screen.blit(text, ((WIDTH/2) - (text.get_width()/2), HEIGHT/40))