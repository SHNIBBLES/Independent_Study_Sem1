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
hitDis = (ballrect.width / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    rotation = (rotation + 6) % 360
    ball = pygame.transform.rotate(orgigball, rotation)
    
    ballrect = ballrect.move(speed)
    rectCenterX = ballrect.centerx
    rectCenterY = ballrect.centery
    if (rectCenterX <= 0 + hitDis) or (rectCenterX >= width - hitDis):
        speed[0] = -speed[0]
    if (rectCenterY <= 0 + hitDis) or (rectCenterY >= height - hitDis):
        speed[1] = -speed[1]
    screen.fill(black)
    pygame.draw.rect(screen, green, ballrect, 1)
    screen.blit(ball, (ballrect.centerx - int(ball.get_width() / 2), ballrect.centery - int(ball.get_height() / 2)))
    time.sleep(.05)
    pygame.display.flip()

