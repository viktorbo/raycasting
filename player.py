import math

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
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if keys[pygame.K_w]:
            self.x += PLAYER_SPEED * cos_a
            self.y += PLAYER_SPEED * sin_a
        if keys[pygame.K_s]:
            self.x -= PLAYER_SPEED * cos_a
            self.y -= PLAYER_SPEED * sin_a
        if keys[pygame.K_a]:
            self.angle -= PLAYER_VIEW_ANGLE_SPEED
        if keys[pygame.K_d]:
            self.angle += PLAYER_VIEW_ANGLE_SPEED
        if keys[pygame.K_q]:
            self.x += PLAYER_SPEED * sin_a
            self.y -= PLAYER_SPEED * cos_a
        if keys[pygame.K_e]:
            self.x -= PLAYER_SPEED * sin_a
            self.y += PLAYER_SPEED * cos_a
