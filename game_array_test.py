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
    global current_array
    global main_array
    global pit_array
    # KFF: Use 'is' to test this equality, not '=='.
    # On Saturday, I'll show you a mind-blowing example of why it
    # matters whether you use 'is' instead of '==' :-).
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
    # KFF: Should this be 'elif'?
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == pit_array:
        pass

def look():
    global current_array
    global main_array
    global pit_array
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == main_array:
        if (p.y == 0) and (p.x == 0): print("You inspect the room further- ")
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
    # KFF: Should this be 'elif'?
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == pit_array:
        pass

def use(input):
    global current_array
    global main_array
    global pit_array
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == main_array:
        pass
    # KFF: Should this be 'elif'?
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == pit_array:
        pass

def get(input):
    global item_list
    global main_item_array
    global pit_item_array
    words = input.split()
    # KFF: Same thing: use 'is' to test this equality, not '=='.
    if current_array == main_array:
        # KFF: What's this 'pass' for?
        pass

        if (words[1] == "pencil") and (words[1] in main_item_array[p.y][p.x]):
            main_item_array[p.y][p.x].remove(words[1])
            p.inventory.append(words[1])
            
                

def drop(input):
    # KFF: What's 'drop' supposed to do?
    pass
    
# KFF: Generally it's good to put the classes first in the file, not
# last.  People want to read them first, because from the classes one
# gets a sense of how the program will work.

class Player:
    # KFF: You're using class-static variables here, instead of
    # instance variables.  The way to use instance variables is to
    # have an __init__() method in the class, and initialize these
    # variables as "self.y = 0", "self.x = 0", "self.inventory = []"
    # etc.  The distinction is a bit subtle; we can talk about it more
    # on Saturday.  
    # 
    # For now, I'd just say don't declare variables in a class outside
    # a method.  Basically, in normal class usage, all variable
    # setting happens inside methods, and the way you share a variable
    # *between* methods is by keeping the variable in the object with
    # "self.foo" -- then "foo" is a property of the current object.
    y = 0
    x = 0
    inventory = []
    def move(self, direction):
        global current_array
        y_limit = len(current_array) - 1
        x_limit = len(current_array[0]) - 1
        if(direction == "n") and (current_array[self.y-1][self.x] == 1) and (self.y-1 >= 0):
            self.y -= 1
            location_direct()(self.y+1, self.x)
        elif(direction == "e") and (self.x+1 <= x_limit) and (current_array[self.y][self.x+1] == 1):
            self.x += 1
            location_direct()(self.y, self.x-1)
        elif(direction == "s") and (self.y+1 <= y_limit) and (current_array[self.y+1][self.x] == 1):
            self.y += 1
            location_direct()(self.y-1, self.x)
        elif(direction == "w") and (current_array[self.y][self.x-1] == 1) and (self.x-1 >= 0):
            self.x -= 1
            location_direct()(self.y, self.x+1)
        else:
            print("You can't go there!")
        
class Location:
    # KFF: Same thing here about using an __init__() method and making
    # this be "self.main_array_visit" in that method.
    main_array_visit = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
    def l000(self, lasty, lastx): #direction is where entering the square from
        if self.main_array_visit[0][0] == 0:
            print("You slowly open your eyes, you're in the corner of a dimly lit room.")
        if self.main_array_visit[0][0] >= 1:
            print("You're back to where you woke up")
        self.main_array_visit[0][0] += 1
    def l010(self, lasty, lastx):
        print("Next Space")
        self.main_array_visit[1][0] += 1
    def l020(self, lasty, lastx):
        self.main_array_visit[2][0] += 1
    def l030(self, lasty, lastx):
        self.main_array_visit[3][0] += 1
    def l001(self, lasty, lastx):
        self.main_array_visit[0][1] += 1
    def l011(self, lasty, lastx):
        self.main_array_visit[1][1] += 1
    def l021(self, lasty, lastx):
        self.main_array_visit[2][1] += 1
    def l031(self, lasty, lastx):
        self.main_array_visit[3][1] += 1
    def l002(self, lasty, lastx):
        self.main_array_visit[0][2] += 1
    def l012(self, lasty, lastx):
        self.main_array_visit[1][2] += 1
    def l022(self, lasty, lastx):
        self.main_array_visit[2][2] += 1
    def l032(self, lasty, lastx):
        self.main_array_visit[3][2] += 1
    def l003(self, lasty, lastx):
        self.main_array_visit[0][3] += 1
    def l013(self, lasty, lastx):
        self.main_array_visit[1][3] += 1
    def l023(self, lasty, lastx):
        self.main_array_visit[2][3] += 1
    def l033(self, lasty, lastx):
        self.main_array_visit[3][3] += 1
            
box_gen("Welcome to The Array Game!\n Alpha V1.4 \n  By Elijah Underhill-Miller")
box_gen("Instructions:\nFind your way out.")
# KFF: For the word "proceeding" below I think you mean "preceding".
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n  If you wish to interact with an object,\ntype its name.\n If you wish to pick up or drop an item, \n  type \"pick up\" or \"drop\" proceeding the item.") 
#Starting Position: 0, 0
main_array = [[1, 0, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]]
main_item_array = [[["pencil"], [], ["yarn", "electric wire"], []],
                   [[], [], [], []],
                   [[], ["sketched map", "screwdriver"], ["electric wire"], []],
                   [["black key"], [], [], []]]
pit_array = [[1, 0],
             [1, 1]]
pit_item_array = [[[], []],
                  [["rusty key"], ["ladder rung"]]]
item_list = []
#for x in range(len(main_item_array)*len(main_item_array[0])+(len(pit_item_array)*len(pit_item_array[0]))):
print(main_item_array[0][0][0])
# KFF: What's this for-loop for?  All it seems to do is 'pass'.
for x in range(len(main_item_array)*len(main_item_array[0])):
    pass
current_array = main_array
p = Player()
l = Location()
location_direct()(0, 0)
while True:
    #print("Postition: " 
    raw_input = str(input("--> "))
    #user_input = input_read(raw_input)
    raw_input = raw_input.strip().lower()
    if raw_input == "exit game":
        break
    elif raw_input == "location":
        print("Location: " + "[" + str(p.y) + "][" + str(p.x) + "]")
    elif (raw_input == "l") or (raw_input == "look"):
        look()
    elif raw_input == "i":
        print("| Inventory: ")
        for x in range(len(p.inventory)):
            print("| 1 " + p.inventory[x])
    elif (raw_input == "n" or "north") or (raw_input == "e" or "east")  or (raw_input == "s" or "south") or (raw_input == "w" or "west"):
        p.move(raw_input)
    elif ("get" in raw_input) or ("take" in raw_input) or ("pick up" in raw_input):
        get(raw_input)
    elif "drop" in raw_input:
        drop(raw_input)
    elif (raw_input == "pencil") or (raw_input == "yarn") or (raw_input == "sketched map") or (raw_input == "screwdriver") or (raw_input == "electric wire") or (raw_input == "black key") or (raw_input == "rusty key") or (raw_input == "ladder rung"):
        use(raw_input)
    else: 
        print("Command not recognized")
    
              
