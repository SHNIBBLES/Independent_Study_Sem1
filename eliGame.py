#!/usr/bin/env python3

import pygame
import time
import sys

pygame.init()

size = width, height = 520, 340

center = width // 2, height // 2

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

screen = pygame.display.set_mode(size)

orig_ball = pygame.image.load("intro_ball.gif")
orig_ball.convert()
ball = orig_ball

degrees = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)
    ballrect = ball.get_rect()
    ballrect.center = center
    # Oddly, commenting out the centering line above and uncommenting
    # this line below leads to *two* rectangles being drawn every
    # time through the loop: one constrained to the ball's dimensions
    # and the other for the (sometimes) larger surface around it
    # ("sometimes" because that surface has to expand and contract to
    # accommodate the corners of the ball's rectangle when the ball is
    # in certain rotations).  We'd like to understand better what's
    # going on with that, at some point.
    # 
    # pygame.draw.rect(ball, GREEN, ballrect, 5)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    degrees = (degrees + 1) % 360
    ball = pygame.transform.rotate(orig_ball, degrees)
    time.sleep(.05)
