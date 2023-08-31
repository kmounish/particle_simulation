import pygame
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from particle import Particle

# TODO:
# Maybe more: where it slides of to the side like sand or water

# Pre-setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
parts = []
time = 0
id = 0


while running:
    # Set up for simulation:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            tmp = Particle(pos[0], pos[1], size=5, id=id)
            id += 1
            parts.append(tmp)
    screen.fill("white")
    current_time = pygame.time.get_ticks()

    # falling simulation:
    for x in parts:
        right = True
        left = True
        down = True
        notsame = True
        x.update_velocity(current_time-time)
        for y in parts:
            # Checks for particle collision
            # TODO: Might have to make this a range - giving issues with exact values i think
            check_left = (x.get_pos()[0]-y.size,
                          x.get_pos()[1]+y.size) == y.get_pos()
            check_right = (x.get_pos()[0]+y.size,
                           x.get_pos()[1]+y.size) == y.get_pos()
            check_down = (x.get_pos()[0],
                          x.get_pos()[1]+y.size) == y.get_pos()
            same = x.get_pos() == y.get_pos()
            id_test = x.id is not y.id

            if same and id_test:
                notsame = False
            if check_left and id_test:
                left = False
            if check_right and id_test:
                right = False
            if check_down and id_test:
                down = False

        # update particles based on collision
        if not notsame:
            x.update_pos(x.get_pos(), x.size)
        elif not down and left:
            x.update_pos(x.get_pos(), x.size, "left")
        elif not down and not left and right:
            x.update_pos(x.get_pos(), x.size, "right")
        else:
            x.update_pos()

        pygame.draw.circle(screen, "green", x.get_pos(), x.size)

    time = pygame.time.get_ticks()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
