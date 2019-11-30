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
    print(array)
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

def visit_count_setup():
    
###INDEX FOR NUMBERS (First Digit: array #, Last Digits: location in array)
# First Digit:
# 0 - main_array
# 1 - pit_array
# Second Digit:
#
###
def location(y, x):
    if y == 0 and x == 0: return 000
    if y == 1 and x == 0: return 010
    if y == 2 and x == 0: return 020
    if y == 3 and x == 0: return 030
    if y == 0 and x == 1: return 001
    if y == 1 and x == 1: return 011
    if y == 2 and x == 1: return 021
    if y == 3 and x == 1: return 031
    if y == 0 and x == 2: return 002
    if y == 1 and x == 2: return 012
    if y == 2 and x == 2: return 022
    if y == 3 and x == 2: return 032
    if y == 0 and x == 3: return 003
    if y == 1 and x == 3: return 013
    if y == 2 and x == 3: return 023
    if y == 3 and x == 3: return 033


    
def 000(lasty, lastx): ## last y&x is direction is where your entering the square from
    if visit count == 0:
        print("You slowly open your eyes, you're in the corner of a dimly lit room.")
    if visit count >=1:
        print("You're back to where you woke up")
    visit_count += 1

            
box_gen("Welcome to The Test Array Game!\n Alpha V1.0 \n    By Elijah Underhill-Miller")
box_gen("Instructions:\nFind your way out.")
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n If you wish to interact with an object,\ntype its name.") 
#Starting Position:
x = 0
y = 0
inventory = [] 
main_array = [[1, 0, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]]
pit_array = [[1, 0],
             [1, 1]]
current_pos = test_array[x][y]
print(current_pos)
#user_input = str(input("Enter first  move: ")
while True:
    print("Postition: " + "[" + str(x) + "][" + str(y) + "]")
    user_input = str(input("--> "))
### MOVEMENT
    if (user_input == "north"):
        if main_array[y-1][x] != 1:
            print("You can't go there!")
        else:
            y-=1
            location(y, x)(y+1, x)
    elif (user_input == "east"):
        if main_array[y][x+1] != 1:
            print("You can't go there!")
        else:
            x+=1
            location(y, x)(y, x-1)
    elif (user_input == "south"):
        if main_array[y+1][x] != 1:
            print("You can't go there!")
        else:
            y+=1
            location(y, x)(y-1, x)
    elif (main_input == "west"):
        if test_array[y][x-1] != 1:
            print("You can't go there!")
        else:
            x-=1   
            location(y, x)(y, x+1)### OTHER STUFF
    elif (user_input == "look"):
        location
    elif (user_input == "inventory"):
        print("Inventory: ")
        print 
    elif (user_input == "exit game"):
        break
    else:
        print("Command not recognized")

#print(test_array[1])
#print(test_array[1])
    
              
