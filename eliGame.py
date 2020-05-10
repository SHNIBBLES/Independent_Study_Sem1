#!/usr/bin/env python3

import pygame
import time
import sys
import random
pygame.init()

def intro():
    done = False
    font = pygame.font.Font('slkscreb.ttf', 20) 
    text1 = font.render('WELCOME TO THE BALL BOUNCER', True, white)
    textrect1 = text1.get_rect()  
    textrect1.center = (screen.get_width() // 2, (screen.get_height() // 2) - 100)
    text2 = font.render('ENTER A NUMBER OF BALLS', True, white)
    textrect2 = text2.get_rect()  
    textrect2.center = (screen.get_width() // 2, (screen.get_height() // 2) - 50)
    accepted_numbers = [49, 50, 51, 52, 53]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key in accepted_numbers:
                    return event.key
        screen.fill(black)  
        screen.blit(text1, textrect1)
        screen.blit(text2, textrect2)
        pygame.display.flip()
        if done == True:
            break

class Ball():
    def __init__(self, image_file, screen, start_pos):
        self.start_pos = start_pos
        self.speed = [4, 4]
        self.rotation = 0
        self.orgigball = pygame.image.load(image_file)
        self.orgigball.convert()
        self.ball = self.orgigball
        self.ballrect = self.ball.get_rect()
        self.radius = (self.ballrect.width / 2)
        self.screen = screen
        self.ballrect.center = self.start_pos
    def step(self):
        self.rotate()
        self.bounce()
        self.screen.blit(self.ball, (self.ballrect.centerx - int(self.ball.get_width() / 2), self.ballrect.centery - int(self.ball.get_height() / 2)))
    def rotate(self):
        self.rotation = (self.rotation + 6) % 360
        self.ball = pygame.transform.rotate(self.orgigball, -self.rotation)
    def bounce(self):
        self.ballrect = self.ballrect.move(self.speed)
        if (self.ballrect.centerx <= 0 + self.radius) or (self.ballrect.centerx >= self.screen.get_width() - self.radius):
            self.speed[0] = -self.speed[0]
        if (self.ballrect.centery <= 0 + self.radius) or (self.ballrect.centery >= self.screen.get_height() - self.radius):
            self.speed[1] = -self.speed[1]


size = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
green = 0, 240, 40

screen = pygame.display.set_mode(size)



ball_one = Ball("intro_ball.gif", screen, [60, 60])
ball_two = Ball("intro_ball.gif", screen, [500, 200])
ball_list = [ball_one, ball_two]

ball_number = intro()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    screen.fill(black)  
    ball_one.step()
    ball_two.step()
    pygame.display.flip()
    time.sleep(.01)
