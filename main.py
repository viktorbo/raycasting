import pygame
from settings import *
from player import Player
import math

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(COLOR_BLACK)

    player.movement()
    pygame.draw.circle(
        surface=screen,
        color=COLOR_GREEN,
        center=player.position,
        radius=PLAYER_CIRCLE_RADIUS
    )
    pygame.draw.line(
        surface=screen,
        color=COLOR_RED,
        start_pos=player.position,
        end_pos=(player.x + PLAYER_RAY_DISTANCE * math.cos(player.angle),
                 player.y + PLAYER_RAY_DISTANCE * math.sin(player.angle))
    )
    pygame.display.flip()
    clock.tick(WINDOW_FPS)
