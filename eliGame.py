#!/usr/bin/env python3

import pygame
import time
import sys
import random
import math
pygame.init()


def intro(screen, background, word_color):
    """Generates Intro Screen, takes user input, and
    returns desired number of balls"""
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
    def __init__(self, image_file, screen, name, ball_list, start_pos):
        """
        image_file - a string - tells class which image file to load
        screen - a pygame object with height and width - allows class to know height and width of game window
        name - an int - tells class the simple id of a ball in the ball_list
        ball_list - a list - used for cycling through all the ball instances
        start_pos - a list - cordinnates for spawning ball upon generation
        """
        self.name = name
        self.ball_list = ball_list
        self.speed = [4, 4]
        self.rotation = 0
        self.orgigball = pygame.image.load(image_file)
        self.orgigball.convert()
        self.ball = self.orgigball
        self.ballrect = self.ball.get_rect()
        self.radius = (self.ballrect.width / 2)
        self.screen = screen
        self.bouncy = True
        self.ballrect.center = start_pos
    def __str__(self):
        """
        For name purposes
        """
        return self.name
    def step(self):
        """
        Executive for all ball movement
        """
        self.rotate()
        self.wallbounce()
        self.bounce()
        self.move()
        self.screen.blit(self.ball, (self.ballrect.centerx - int(self.ball.get_width() / 2), self.ballrect.centery - int(self.ball.get_height() / 2)))
    def move(self):
        """
        Ball  movement in a direction
        """
        self.ballrect = self.ballrect.move(self.speed)
    def rotate(self):
        """
        Rotate the ball
        """
        self.rotation = (self.rotation + 6) % 360
        self.ball = pygame.transform.rotate(self.orgigball, -self.rotation)
    def wallbounce(self):
        """
        Responsible for ball bouncing on walls
        """
        if (self.ballrect.centerx <= 0 + self.radius) or (self.ballrect.centerx >= self.screen.get_width() - self.radius):
            self.speed[0] = -self.speed[0]
        if (self.ballrect.centery <= 0 + self.radius) or (self.ballrect.centery >= self.screen.get_height() - self.radius):
            self.speed[1] = -self.speed[1]
    def reverse(self):
        """
        When the balls need to be reversed
        """
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]
    def bounce(self):
        """
        When two balls hit eachother
        """
        for ball1 in self.ball_list:
            for ball2 in self.ball_list:
                if ball1 != ball2:
                    distance = math.hypot(ball1.ballrect.centerx - ball2.ballrect.centerx, ball1.ballrect.centery - ball2.ballrect.centery)
                    if show_debug == True:
                        print(f"{ball1}  {ball2}  Distance = {distance:.0f}")
                    if (distance <= (ball1.radius + ball2.radius)) and (self.bouncy == True):
                        self.bouncy = False
                        if show_debug == True:
                            print(f"contact ({ball1} -> {ball2}) dis= {distance:.0f}")
                        ball1.reverse()
                        ball2.reverse()
                        ball1.ballrect = ball1.ballrect.move(ball1.speed)
                        ball2.ballrect = ball2.ballrect.move(ball2.speed)
                    else:
                        self.bouncy = True
                
show_debug = False

def main():
    """
    Game setup and main loop
    """
    size = width, height = 640, 480
    ball_list = []
    black = 0, 0, 0
    white = 255, 255, 255
    green = 0, 240, 40
    screen = pygame.display.set_mode(size)
    number_of_balls = intro(screen, black, white)
    start_pos_list = []
    max_radius = int((pygame.image.load("intro_ball.gif").get_rect().width) / 2)
    print(f"Max-Radius = {max_radius}")
    while len(start_pos_list) < number_of_balls:
        print("Randomizing...")
        start_pos = [random.randint(0 + max_radius + 5, screen.get_width() - max_radius + 5), random.randint(0 + max_radius + 5, screen.get_height() - max_radius + 5)]
        start_pos_list.append(start_pos)
        if len(start_pos_list) >= 2:
            for pos_number in range(len(start_pos_list) - 1):
                if (math.hypot(start_pos_list[-1][0] - start_pos_list[(-pos_number - 2)][0], start_pos_list[-1][1] - start_pos_list[(-pos_number - 2)][1])) <= ((max_radius * 2) + 10):
                    del start_pos_list[-1]
                    break
    print(f"Done! - Pos_List = {start_pos_list}")
    for ball_number in range(number_of_balls):
        ball_list.append(Ball("intro_ball.gif", screen, f"{ball_number}", ball_list, start_pos_list[ball_number]))
                
                
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_d:
                    show_debug = True
        screen.fill(black)  
        for ball in ball_list:
            ball.step()
        pygame.display.flip()
        time.sleep(.01)

if __name__ == '__main__':
    main()
