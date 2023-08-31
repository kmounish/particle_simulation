import pygame
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
from particle import Particle

# TODO:
# Maybe more: where it slides of to the side like sand or water

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
parts = []
time = 0
id = 0
while running:
    # Set up:
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
        # test = True
        right = True
        left = True
        down = True
        x.update_velocity(current_time-time)
        for y in parts:
            check_left = (x.get_pos()[0]-y.size,
                          x.get_pos()[1]-y.size) == y.get_pos()
            check_right = (x.get_pos()[0]+y.size,
                           x.get_pos()[1]-y.size) == y.get_pos()
            check_down = (x.get_pos()[0],
                          x.get_pos()[1]+y.size) == y.get_pos()

            # test_1 = x.get_pos() == y.get_pos() and x.id is not y.id
            # test_2 = (x.get_pos()[0], x.get_pos()[1]+y.size) == y.get_pos()
            # test_3 = (x.get_pos()[0]+y.size,
            #           x.get_pos()[1]+y.size) != y.get_pos()

            if check_left:
                left = False
            if check_right:
                right = False
            if check_down:
                down = False
            # if x.get_pos() == y.get_pos() and x.id is not y.id:
            #     test = False
            #     x.update_pos(x.get_pos(), y.size)
            #     break
            # elif test_2:
            #     test = False
            #     break
            # elif test_3:
            #     test = False
            #     x.update_pos(x.get_pos(), y.size, "left")
        # if test:
        #     x.update_pos()
        if not check_down and check_left and not check_right:
            x.update_pos(x.get_pos(), x.size, "left")
        elif not check_down and not check_left and check_right:
            x.update_pos(x.get_pos(), x.size, "right")
        else:
            x.update_pos()

        pygame.draw.circle(screen, "green", x.get_pos(), x.size)

    time = pygame.time.get_ticks()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
