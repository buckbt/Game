import pygame
from game_parameters import *


#sprite class for plater

class Player(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.forward_image = pygame.image.load('../assets/sprites/alienBlue.png')
        self.backward_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_up(self):
        self.y_velocity = -1 * PLAYER_VELOCITY

    def move_down(self):
        self.y_velocity = PLAYER_VELOCITY

    def move_left(self):
        self.x_velocity = -1 * PLAYER_VELOCITY
        self.image = self.backward_image




    def move_right(self):
        self.x_velocity = PLAYER_VELOCITY
        self.image = self.forward_image




    def stop(self):
        self.x_velocity = 0
        self.y_velocity = 0

    def update(self):
        #TODO Make sure the orange fish stays on screen
        self.x += self.x_velocity
        self.y += self.y_velocity
        if self.x > WIDTH - TILE:
            self.x = WIDTH - TILE
        if self.x < 0:
            self.x = 0
        if self.y > HEIGHT-2*TILE:
            self.y = HEIGHT-2*TILE
        if self.y < 0:
            self.y =  0
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
