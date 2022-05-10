from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = PLAYER_DEFAULT_POSITION
        self.angle = PLAYER_VIEW_ANGLE

    @property
    def position(self):
        return self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED
        if keys[pygame.K_q]:
            self.angle -= PLAYER_VIEW_ANGLE_SPEED
        if keys[pygame.K_e]:
            self.angle += PLAYER_VIEW_ANGLE_SPEED
