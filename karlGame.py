#!/usr/bin/env python3

# Reference: https://www.pygame.org/docs/genindex.html

import pygame
import time
import sys

dimensions = (800, 800)
screen = pygame.display.set_mode(dimensions)

# TBD: Why isn't this caption displayed anywhere?
pygame.display.set_caption("Karl's ever-growing circle.")

radius = 5
radius_increment = 1

# Choices are "run", "pause", or "stop".
# Any other value may cause undefined behavior.
status = "run" 

while status != "stop":
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.unicode == 'p':
            if status != "pause":
                status = "pause"
            else:
                status = "run"
        if event.type == pygame.KEYDOWN and event.unicode == 'q':
            status = "stop"
        elif event.type == pygame.QUIT:
            status = "stop"
    if status == "run":
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), radius, 5)
        radius += radius_increment
        pygame.draw.circle(screen, (255, 100, 255), (400, 400), radius, 5)
        pygame.display.flip()
        time.sleep(.05)  # argument to time.sleep() is number of seconds
