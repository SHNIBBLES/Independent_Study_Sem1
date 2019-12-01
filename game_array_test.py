#!/usr/bin/env python3
import sys
import math

def box_gen(input):
    array = []
    max_len = 0
    for line in input.splitlines():
        line = line.strip()
        array.append(line)
        if len(line) > max_len:
            max_len = len(line)
    for x in range(len(array)):
        spaces = math.floor((max_len - len(array[x]))/2)
        array[x] = (" " * spaces) + array[x] + (" " * spaces)
    barriers = "|" + (max_len + 2) * "-" + "|"
    print(barriers)
    for line in array:
        if ((max_len - len(line)) % 2) == 0:
            print("| " + line + " |")
        else:
            print("| " + line + "  |")
    print(barriers)
    
def map_gen(array):
    width = len(array[0]) 
    height = len(array)
    print("|" + "-" * width + "|")
    for j in range(height):
        print("|", end="", flush=True)
        for k in range(width):
            if array[j][k] == 1:
                print(".", end="", flush=True)
            else:
                print("#", end="", flush=True)
        print("|")
    print("|" + "-" * width + "|")
    
###INDEX FOR NUMBERS (First Digit: array #, Last Digits: location in array)
# First Digit:
# 0 - main_array
# 1 - pit_array
# Second Digit:
#
###
def location_direct():
    if current_array == main_array:
        if (p.y == 0) and (p.x == 0): return l.l000
        if (p.y == 1) and (p.x == 0): return l.l010
        if (p.y == 2) and (p.x == 0): return l.l020
        if (p.y == 3) and (p.x == 0): return l.l030
        if (p.y == 0) and (p.x == 1): return l.l001
        if (p.y == 1) and (p.x == 1): return l.l011
        if (p.y == 2) and (p.x == 1): return l.l021
        if (p.y == 3) and (p.x == 1): return l.l031
        if (p.y == 0) and (p.x == 2): return l.l002
        if (p.y == 1) and (p.x == 2): return l.l012
        if (p.y == 2) and (p.x == 2): return l.l022
        if (p.y == 3) and (p.x == 2): return l.l032
        if (p.y == 0) and (p.x == 3): return l.l003
        if (p.y == 1) and (p.x == 3): return l.l013
        if (p.y == 2) and (p.x == 3): return l.l023
        if (p.y == 3) and (p.x == 3): return l.l033
    if current_array == pit_array:
        pass

def look():
    if current_array == main_array:
        if (p.y == 0) and (p.x == 0): print("")
        if (p.y == 1) and (p.x == 0): print("You found a pencil!")
        if (p.y == 2) and (p.x == 0): print("")
        if (p.y == 3) and (p.x == 0): print("")
        if (p.y == 0) and (p.x == 1): print("")
        if (p.y == 1) and (p.x == 1): print("")
        if (p.y == 2) and (p.x == 1): print("")
        if (p.y == 3) and (p.x == 1): print("")
        if (p.y == 0) and (p.x == 2): print("")
        if (p.y == 1) and (p.x == 2): print("")
        if (p.y == 2) and (p.x == 2): print("")
        if (p.y == 3) and (p.x == 2): print("")
        if (p.y == 0) and (p.x == 3): print("")
        if (p.y == 1) and (p.x == 3): print("")
        if (p.y == 2) and (p.x == 3): print("")
        if (p.y == 3) and (p.x == 3): print("")
    if current_array == pit_array:
        pass

    
def input_read(input):
    input = input.strip().lower()
    if input[0] == "n":
        return "north"
    if input[0] == "e":
        return "east"
    if input[0] == "s":
        return "south"
    if input[0] == "w":
        return "west"
    if input[0] == "l":
        return "look"
    if input[0] == "i":
        return "inventory"
       
class Player:
    y = 0
    x = 0
    inventory = []
    def move(self, direction):
        global current_array
        if(direction == "north") and (current_array[self.y-1][self.x] != 0) and (self.y-1 >= 0):
            self.y -= 1
            var = location_direct()
            #print(var)
            var(self.y+1, self.x)
        elif(direction == "east") and (current_array[self.y][self.x+1] != 0):
            self.x += 1
            location_direct()(self.y, self.x-1)
        elif(direction == "south") and (current_array[self.y+1][self.x] != 0):
            self.y += 1
            location_direct()(self.y-1, self.x)
        elif(direction == "west") and (current_array[self.y][self.x-1] != 0):
            self.x -= 1
            location_direct()(self.y, self.x+1)
        else:
            print("You can't go there!")
        
            
class Location:
    l000_visit_count = 0
    l010_visit_count = 0
    l020_visit_count = 0
    l030_visit_count = 0
    l001_visit_count = 0
    l011_visit_count = 0
    l021_visit_count = 0
    l031_visit_count = 0
    l002_visit_count = 0
    l012_visit_count = 0
    l022_visit_count = 0
    l032_visit_count = 0
    l003_visit_count = 0
    l013_visit_count = 0
    l023_visit_count = 0
    l033_visit_count = 0
    def l000(self, lasty, lastx): #direction is where entering the square from
        if self.l000_visit_count == 0:
            print("You slowly open your eyes, you're in the corner of a dimly lit room.")
        if self.l000_visit_count >=1:
            print("You're back to where you woke up")
        self.l000_visit_count += 1
    def l010(self, lasty, lastx):
        print("A nobble says to you: Hello There!!")

            
box_gen("Welcome to The Test Array Game!\n Alpha V1.0 \n    By Elijah Underhill-Miller")
box_gen("Instructions:\nFind your way out.")
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n  If you wish to interact with an object,\ntype its name.") 
#Starting Position: 0, 0
main_array = [[1, 0, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]]
pit_array = [[1, 0],
             [1, 1]]
current_array = main_array
p = Player()
l = Location()
location_direct()(0, 0)
while True:
    #print("Postition: " 
    raw_input = str(input("--> "))
    user_input = input_read(raw_input)
    if (raw_input.strip().lower() == "exit game"):
        break
    elif (raw_input.strip().lower() == "location"):
        print("Location: " + "[" + str(p.y) + "][" + str(p.x) + "]")
    elif user_input == "look":
        look()
    elif user_input == "north" or "east" or "south" or "west":
       p.move(user_input)
    elif user_input == "inventory":
       print("| Inventory: ")
       for x in range(inventory):
           print("| " + inventory[x])
    else:
        print("Command not recognized")
    
              
