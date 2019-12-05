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
        elif (p.y == 1) and (p.x == 0): return l.l010
        elif (p.y == 2) and (p.x == 0): return l.l020
        elif (p.y == 3) and (p.x == 0): return l.l030
        elif (p.y == 0) and (p.x == 1): return l.l001
        elif (p.y == 1) and (p.x == 1): return l.l011
        elif (p.y == 2) and (p.x == 1): return l.l021
        elif (p.y == 3) and (p.x == 1): return l.l031
        elif (p.y == 0) and (p.x == 2): return l.l002
        elif (p.y == 1) and (p.x == 2): return l.l012
        elif (p.y == 2) and (p.x == 2): return l.l022
        elif (p.y == 3) and (p.x == 2): return l.l032
        elif (p.y == 0) and (p.x == 3): return l.l003
        elif (p.y == 1) and (p.x == 3): return l.l013
        elif (p.y == 2) and (p.x == 3): return l.l023
        elif (p.y == 3) and (p.x == 3): return l.l033
    if current_array == pit_array:
        if (p.y == 0) and (p.x == 0): return l.l100
        elif (p.y == 1) and (p.x == 0): return l.l110
        elif (p.y == 1) and (p.x == 1): return l.l111

def look():
    ###############################
    #[0,0] |#######| [0,2] |#######
    #-----------------------------#
    #[1,0] | [1,1] | [1,2] | [1,3]#
    #-----------------------------#
    #######| [2,1] | [2,2] |#######
    #-----------------------------#
    #[3,0] | [3,1] |###############
    ###############################    
    global current_array
    global main_array
    global pit_array
    global main_item_array
    global pit_item_array
    if current_array == main_array:
        items_here = []
        item_str = " You see here"
        if len(main_item_array[p.y][p.x]) >= 1:
            for item in main_item_array[p.y][p.x]:
                item_str = item_str + " a/an " + item + ","
        else:
            item_str = ""    
        if (p.y == 0) and (p.x == 0): print("You inspect the room further- you find that you eyes have adjusted and it's quite easy to see in the room. There's lots of dust around the edge of the floor." + item_str)
        elif (p.y == 1) and (p.x == 0): print("" + item_str)        
        elif (p.y == 3) and (p.x == 0): print("" + item_str)
        elif (p.y == 0) and (p.x == 1): print("" + item_str)
        elif (p.y == 1) and (p.x == 1): print("" + item_str)
        elif (p.y == 2) and (p.x == 1): print("" + item_str)
        elif (p.y == 3) and (p.x == 1): print("" + item_str)
        elif (p.y == 0) and (p.x == 2): print("" + item_str)
        elif (p.y == 1) and (p.x == 2): print("" + item_str)
        elif (p.y == 2) and (p.x == 2): print("" + item_str)
        elif (p.y == 1) and (p.x == 3): print("" + item_str)
    if current_array == pit_array:
        if (p.y == 0) and (p.x == 0): print("" + item_str)
        elif (p.y == 1) and (p.x == 0): print("" + item_str)
        elif (p.y == 1) and (p.x == 1): print("" + item_str)

def use(input):
    ###############################
    #[0,0] |#######| [0,2] |#######
    #-----------------------------#
    #[1,0] | [1,1] | [1,2] | [1,3]#
    #-----------------------------#
    #######| [2,1] | [2,2] |#######
    #-----------------------------#
    #[3,0] | [3,1] |###############
    ###############################
    global current_array
    global main_array
    global pit_array
    global main_item_array
    global pit_item_array
    ##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung 
    if input in p.inventory:
        if current_array == main_array:
            box_open = False
            if input == "pencil":
                if "sketched_map" in p.inventory:
                    print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                else:
                    print("You can't use that here!")
            elif input == "yarn":
                if (p.y == 1) and (p.x == 1):
                    print("Holding the loose end, you throw the ball of yarn up toward the light hanging from the celing. It winds around the wire and then you pull down. The lamp comes crashing down, and now it's much darker.")
                    main_item_array[p.y][p.x].append(broken_light_bulb)
                else: print("You can't use that here!")
            elif input == "electric_wire":
                if (p.y == 0) and (p.x == 2):
                    if box_open == True:
                        print("You see that there's a wire that's torn in two, you take the wire you picked up and attach the two loose ends, and see a spark. After a few moments, you hear a motor turn on and suddunly the floor below you opens up! You start falling...")
                        current_array = pit_array
                    else: print("You can't use that here!")
                else: print("You can't use that here!")
            elif input == "sketched_map":
                man_gen(main_array)
            elif input == "screwdriver":
                if (p.y == 0) and (p.x == 2):
                    if box_open == False:
                        print("You look at the box on the corner of the wall, and look at the screwdriver in your hand. You get an idea. Why not? You proceed to wedge the end of the screwdriver in the space between the front panel of the box and itself. After some fiddling, the panel pops open and falls to the ground. The box appears to be some sort of electronic control system.")
                        box_open = True
                    else: print("You can't use that here!")
                else: print("You can't use that here!")
            elif input == "black_key": pass
            elif input == "rusty_key": pass
            elif input == "ladder_rung": pass
        if current_array == pit_array:
            if input == "pencil":
                if "sketched_map" in p.inventory:
                    print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                else:
                    print("You can't use that here!")
            elif input == "yarn": pass
            elif input == "electric_wire": pass
            elif input == "sketched_map":
                man_gen(main_array)
            elif input == "screwdriver": pass
            elif input == "black_key": pass
            elif input == "rusty_key": pass
            elif input == "ladder_rung": pass
    else:
        print("You don't have that item!")
        
def get(input):
    global static_item_list
    global main_item_array
    global pit_item_array
    words = input.split()
    check_len = len(p.inventory) #used to see if it has changed
    if current_array == main_array:
        for item in static_item_list:
            if (words[-1] == item) and (item in main_item_array[p.y][p.x]):
                main_item_array[p.y][p.x].remove(item)
                p.inventory.append(item)
                print("You picked up a/an " + item)
                break
        if len(p.inventory) == check_len:
            print("That item isn't here!")

def drop(input):
    global static_item_list
    global main_item_array
    global pit_item_array
    words = input.split()
    if current_array == main_array:
        if words[-1] in p.inventory:
            p.inventory.remove(words[-1])
            main_item_array[p.y][p.x].append(words[-1])
            print("You dropped a/an" + words[-1])
        else:
            print("You don't have that item!")

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
    pit_array_visit = [[0, 0],
                       [0, 0]]
    def l000(self, lasty, lastx): #direction is where entering the square from
        if self.main_array_visit[0][0] == 0:
            print("\"What happened?\" you think in your head before you can speak. You fell very tired. You open your eyes, you're in the corner of a dimly lit room. Across from you you can see there's sort of a hallway leading to the left")
        if self.main_array_visit[0][0] >= 1:
            print("You're back to where you woke up")
        self.main_array_visit[0][0] += 1
    def l010(self, lasty, lastx):
        if self.main_array_visit[1][0] == 0:
            print("The walls are smooth dark grey concrete, like the inside of that bunker in the sci-fi movie you watched. Wait, when did you watch that movie?? It seems like it has been an eternity, yet you also remember just watching it.")
        else:
            print("There's not much here, the ground seems kind of moist. You don't like it.")
        self.main_array_visit[1][0] += 1
                  ###############################
                  #[0,0] |#######| [0,2] |#######
                  #-----------------------------#
                  #[1,0] | [1,1] | [1,2] | [1,3]#
                  #-----------------------------#
                  #######| [2,1] | [2,2] |#######
                  #-----------------------------#
                  #[3,0] | [3,1] |###############
                  ###############################
    def l030(self, lasty, lastx):
        print("There's a big scary door here. You wonder where it goes. Should you try to open it? You try the handle, but it won't budge.")
        self.main_array_visit[3][0] += 1
    def l011(self, lasty, lastx):
        self.main_array_visit[1][1] += 1
    def l021(self, lasty, lastx):
        if (lasty == 3) and (lastx == 1):
            print("From this direction, you see that theres a slice of paper wedged in between the wall and the pipe")
        else:
            print("There's a large pipe on one side of the room, it looks like it carries fluids.")
        self.main_array_visit[2][1] += 1
    def l031(self, lasty, lastx):
        self.main_array_visit[3][1] += 1
    def l002(self, lasty, lastx):
        self.main_array_visit[0][2] += 1
    def l012(self, lasty, lastx):
        self.main_array_visit[1][2] += 1
    def l022(self, lasty, lastx):
        self.main_array_visit[2][2] += 1
    def l013(self, lasty, lastx):
        self.main_array_visit[1][3] += 1
################################################################
    def l100(self, lasty, lastx):
        self.pit_array_visit[0][0] += 1
            
box_gen("Welcome to The Array Game!\n Alpha V1.4 \n  By Elijah Underhill-Miller")
box_gen("Instructions:\nFind your way out.")
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n  If you wish to use an object,\ntype its name.\n If you wish to pick up or drop an item, \n  type \"pick up\" or \"get\" or \"get\" preceding the item.") 
#Starting Position: 0, 0
main_array = [[1, 0, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]]
main_item_array = [[["pencil"], [], ["yarn", "electric_wire"], []],
                   [[], [], [], []],
                   [[], ["sketched_map", "screwdriver"], ["electric_wire"], []],
                   [["black_key"], [], [], []]]
pit_array = [[1, 0],
             [1, 1]]
pit_item_array = [[[], []],
                  [["rusty_key"], ["ladder_rung"]]]

##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung \

static_interactibles_list = []
static_item_list = []

for row in range(len(main_item_array)):
    for col in range(len(main_item_array[0])):
        for item in range(len(main_item_array[row][col])):
            if len(main_item_array[row][col]) >= 1:
                static_item_list.append(main_item_array[row][col][item])
for row in range(len(pit_item_array)):
    for col in range(len(pit_item_array[0])):
        for item in range(len(pit_item_array[row][col])):
            if len(pit_item_array[row][col]) >= 1:
                static_item_list.append(pit_item_array[row][col][item])

current_array = main_array
p = Player()
l = Location()
location_direct()(0, 0)
while True:
    raw_input = str(input("--> "))
    raw_input = raw_input.strip().lower()
    if raw_input == "exit game":
        print("Goodbye!!")
        break
    elif ("get" in raw_input) or ("take" in raw_input) or ("pick up" in raw_input):
        get(raw_input)
    elif raw_input == "location":
        print("Location: " + "[" + str(p.y) + "][" + str(p.x) + "]")
    elif (raw_input == "l") or (raw_input == "look"):
        look()
    elif raw_input == "i":
        print("| Inventory: ")
        for x in range(len(p.inventory)):
            print("| 1 " + p.inventory[x])
    elif (raw_input == "n") or (raw_input == "e")  or (raw_input == "s") or (raw_input == "w"):
        p.move(raw_input)
    elif "drop" in raw_input:
        drop(raw_input)
    elif raw_input in static_item_list:
        use(raw_input)
    else: 
        print("Command not recognized")
    
              
