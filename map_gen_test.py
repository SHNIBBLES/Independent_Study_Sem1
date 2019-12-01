#!/usr/bin/env python3
import sys
import math

#array = [[1, 0, 1, 0, 1],
#        [1, 1, 1, 1, 1],
#        [0, 1, 1, 0, 0]]
#print("<-> Width: " + str(len(array)))
#print("Height: " + str(len(array[0])))
#
#def map_gen(array):
#    width = len(array[0]) 
#    height = len(array)
#    print("|" + "-" * width + "|")
#    for y in range(height):
#        print("|", end="", flush=True)
#        for x in range(width):
#            if array[y][x] == 1:
#                print(".", end="", flush=True)
#            else:
#                print("#", end="", flush=True)
#        print("|")
#    print("|" + "-" * width + "|")
#map_gen(array)

#class Place:
#    def __init__(self):
#        self.visit_count = 0
#    def visit(self):
#        if self.visit_count == 0:
#            print("First Visit")
#        if self.visit_count == 1:
#            print("Second Visit")
#        self.visit_count+=1
#        
#p = Place()
#print("p.visit_count: " + str(p.visit_count))
#while True:
#    user_input = str(input("--> "))
#    if user_input == "move":
#        p.visit()
########
#class Location:
#    def __init__(self, pos):
#        self.pos = pos
#        #self.distance  = 0
#        #self.var = var
#    def move_forward(self):
#        #if self.arg == "forward":
#        self.pos += 1
#        #if self.var == "back":
#           # self.pos -= 1
#    def move_back(self):
#        self.pos -= 1
#
#l = Location(0)
#print(str(l.pos))
#while True:
#    user_input = str(input("--> "))
#    if user_input == "forward":
#        l.move_forward()
#    if user_input == "back":
#        l.move_back()
#    if user_input == ("count"):
#        print(str(l.pos))
#####
class Player:
    inventory = []
    y = 0
    def __init__(self):
        self.inventory.append("pencil")
        ##self.y = 0
    def move(self, direction):
        global thing
        if(direction == "north") and (thing == 0):
            self.y += 1
    def lol(self):
        class lol2:
            print("we made it!")
        

p = Player()
while True:
    user_input = str(input("--> "))
    if user_input == "north" or "east" or "south" or "west":
        p.move(user_input)
    if user_input == "test":
        p.lol.lol2()
    if user_input == ("position"):
        print(str(p.y))
    if user_input == ("inventory"):
        print("Inventory: " + str(p.inventory))
    if user_input == ("exit"):
        break
#r1.name = "Jeff"
#r1.color = "BLUWEE DA BO DIII DA BO DAIE"
#r1.introduce_self()
