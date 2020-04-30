#!/usr/bin/env python3

import pygame
import time
import sys
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
green = 240, 40, 70
center = width // 2, height // 2
rotation = 0
screen = pygame.display.set_mode(size)

orgigball = pygame.image.load("intro_ball.gif")
orgigball.convert()
ball = orgigball
ballrect = ball.get_rect()
ballrect.center = center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    rotation = (rotation + 15) % 360
    ball = pygame.transform.rotate(orgigball, rotation)
    #ballrect = ball.get_rect()
    ballrect = ballrect.move(speed)
    rectCenterX = ballrect.centerx
    rectCenterY = ballrect.centery
    #distanceX = width - rectCenterX
    #distanceY = height - rectCenterY
    hitDis = 40
    if (rectCenterX <= 0 + hitDis) or (rectCenterX >= width - hitDis):
        speed[0] = -speed[0]
    if (rectCenterY <= 0 + hitDis) or (rectCenterY >= height - hitDis):
        speed[1] = -speed[1]
    ballrect.center = center
    screen.fill(black)
    pygame.draw.rect(screen, green, ballrect, 1)
    screen.blit(ball, ballrect)
    time.sleep(.05)
    pygame.display.flip()

