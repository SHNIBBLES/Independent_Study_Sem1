#!/usr/bin/env python3

import pygame
import time
import sys
import random
import math
pygame.init()
    

def intro(screen, background, word_color):
    done = False
    font = pygame.font.Font('slkscreb.ttf', 20) 
    text1 = font.render('WELCOME TO THE BALL BOUNCER', True, word_color)
    textrect1 = text1.get_rect()  
    textrect1.center = (screen.get_width() // 2, (screen.get_height() // 2) - 100)
    text2 = font.render('ENTER A NUMBER OF BALLS', True, word_color)
    textrect2 = text2.get_rect()  
    textrect2.center = (screen.get_width() // 2, (screen.get_height() // 2) - 50)
    accepted_numbers = ['1', '2', '3', '4', '5']
    number = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.unicode in accepted_numbers:
                    number = int(event.unicode)
        screen.fill(background)  
        screen.blit(text1, textrect1)
        screen.blit(text2, textrect2)
        pygame.display.flip()
        if number is not None:
            break
    textnum = font.render(str(number), True, word_color)
    textnumrect = textnum.get_rect()
    textnumrect.center = (screen.get_width() // 2, screen.get_height() // 2)
    screen.blit(textnum, textnumrect)
    pygame.display.update()
    done = False
    start_ticks = pygame.time.get_ticks()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_c:
                    done = True
        if (pygame.time.get_ticks() - start_ticks) > 3000:
            done = True
    return number

class Ball():
    def __init__(self, image_file, screen):
        self.speed = [4, 4]
        self.rotation = 0
        self.orgigball = pygame.image.load(image_file)
        self.orgigball.convert()
        self.ball = self.orgigball
        self.ballrect = self.ball.get_rect()
        self.radius = (self.ballrect.width / 2)
        self.screen = screen
        self.bouncy = True
        print(ball_list)
        self.ballrect.center = [random.randint(0 + (int(self.radius) + 10), self.screen.get_width() - (int(self.radius) + 10)), random.randint(0 + (int(self.radius) + 10), self.screen.get_height() - (int(self.radius) + 10))]
    def step(self):
        self.rotate()
        self.bounce()
        self.wallbounce()
        self.screen.blit(self.ball, (self.ballrect.centerx - int(self.ball.get_width() / 2), self.ballrect.centery - int(self.ball.get_height() / 2)))
    def rotate(self):
        self.rotation = (self.rotation + 6) % 360
        self.ball = pygame.transform.rotate(self.orgigball, -self.rotation)
    def wallbounce(self):
        self.ballrect = self.ballrect.move(self.speed)
        if (self.ballrect.centerx <= 0 + self.radius) or (self.ballrect.centerx >= self.screen.get_width() - self.radius):
            self.speed[0] = -self.speed[0]
        if (self.ballrect.centery <= 0 + self.radius) or (self.ballrect.centery >= self.screen.get_height() - self.radius):
            self.speed[1] = -self.speed[1]
    def reverse(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]
    def bounce(self):
        for ball1 in ball_list:
            for ball2 in ball_list:
                if ball1 != ball2:
                    distance = math.hypot(ball1.ballrect.centerx - ball2.ballrect.centerx, ball1.ballrect.centery - ball2.ballrect.centery)
                    if (distance <= (ball1.radius + ball2.radius)) and (self.bouncy == True):
                        self.bouncy = False
                        print("contact (%s -> %s)" % (id(ball1), id(ball2)))
                        ball1.reverse()
                        ball2.reverse()
                    else:
                        self.bouncy = True
                
ball_list = []

def main():
    size = width, height = 640, 480
    black = 0, 0, 0
    white = 255, 255, 255
    green = 0, 240, 40
    screen = pygame.display.set_mode(size)
    ball_number = intro(screen, black, white)
    for ball in range(ball_number):
        ball_list.append(Ball("intro_ball.gif", screen))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        screen.fill(black)  
        for ball in ball_list:
            ball.step()
        print("yay")
        pygame.display.flip()
        time.sleep(.01)

if __name__ == '__main__':
    main()
