#!/usr/bin/env python3

import pygame
import time
import sys
pygame.init()

class Ball():
    def __init__(self, image_file, screen):
        self.speed = [2, 2]
        self.rotation = 0
        self.orgigball = pygame.image.load(image_file)
        self.orgigball.convert()
        self.ball = self.orgigball
        self.ballrect = self.ball.get_rect()
        self.radius = (self.ballrect.width / 2)
        self.screen = screen
    def step(self):
        self.rotate()
        self.bounce()
        self.screen.blit(self.ball, (self.ballrect.centerx - int(self.ball.get_width() / 2), self.ballrect.centery - int(self.ball.get_height() / 2)))
    def rotate(self):
        self.rotation = (self.rotation + 6) % 360
        self.ball = pygame.transform.rotate(self.orgigball, self.rotation)
    def bounce(self):
        self.ballrect = self.ballrect.move(self.speed)
        if (self.ballrect.centerx <= 0 + self.radius) or (self.ballrect.centerx >= self.screen.get_width() - self.radius):
            self.speed[0] = -self.speed[0]
        if (self.ballrect.centery <= 0 + self.radius) or (self.ballrect.centery >= self.screen.get_height() - self.radius):
            self.speed[1] = -self.speed[1]


size = width, height = 320, 240
black = 0, 0, 0
green = 0, 240, 40

screen = pygame.display.set_mode(size)

ball_one = Ball("intro_ball.gif", screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    ball_one.step()
    pygame.display.flip()
    time.sleep(.05)
