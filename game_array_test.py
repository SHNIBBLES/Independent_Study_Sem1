#!/usr/bin/env python3
import sys
import math
import random

def end_credits():
    box_gen("")

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
def location_direct(p):
    """Take Player object p, return a Location function.
    """
    global current_array
    global main_array
    global pit_array
    # KFF: Use 'is' to test this equality, not '=='.
    # On Saturday, I'll show you a mind-blowing example of why it
    # matters whether you use 'is' instead of '==' :-).
    if current_array is main_array:
        ###(Turn this into an array, each function a call a value in the array.)
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
    elif current_array is pit_array:
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
    if current_array is main_array:
        items_here = []
        item_str = " You see here"
        if len(main_item_array[p.y][p.x]) >= 1:
            for item in main_item_array[p.y][p.x]:
                item_str = item_str + " a/an " + item + ","
        else:
            item_str = ""    
        if (p.y == 0) and (p.x == 0): print("You inspect the room further- you find that you eyes have adjusted and it's quite easy to see in the room. There's lots of dust around the edge of the floor." + item_str)
        elif (p.y == 1) and (p.x == 0): print("Upon further inspection, there's not much here." + item_str)        
        elif (p.y == 3) and (p.x == 0): print("You take a closer look at the door. You scan around the edges, but you cant see any light coming from the other side. Either the other side is pitch black or this is really well fitted door - maybe designed not to be able to peek through..." + item_str)
        elif (p.y == 1) and (p.x == 1): print("You look around and think - \"What to do.. What to do..\"" + item_str)
        elif (p.y == 2) and (p.x == 1): print("The floor is ... cold. You look up and see theres liquid dripping from the ceiling. Ewww." + item_str)
        elif (p.y == 3) and (p.x == 1): print("This area seems to be kept up a little more. Theres no nasty goo anywhere and theres also nice littel soft piece of rug to stand on." + item_str)
        elif (p.y == 0) and (p.x == 2): print("This area is suspicious. The floor feels uneven - you probably shouldn't stay here for long." + item_str)
        elif (p.y == 1) and (p.x == 2): print("You look around at the ceiling because it seems a little broken up here. You squint and make out that above the ceiling there seem to be some wooden floorboards." + item_str)
        elif (p.y == 2) and (p.x == 2): print("There's a toolbox on the rickity shelf. You open it." + item_str)
        elif (p.y == 1) and (p.x == 3): print("You take a closer look at the trap door. It's fairly small, and made out of thick wooden boards encased in cast iron. This looks like some medieval shit." + item_str)
    elif current_array is pit_array:
        if (p.y == 0) and (p.x == 0): print("There's a lot of dirt in here. It looks like someone started to dig this hole but then forgot to finish it. The onyl thing that seems to be preventing the dirt walls from collapsing in on you are the janky wooden panels nailed to eachother around the edge. The floor is solid compacted dirt - cold to the touch." + item_str)
        elif (p.y == 1) and (p.x == 0): print("You inspect the chest further. It's has the same style as the trapdoor. Thick and medival looking. It has a cast iron latch which doesn't have a lock on it. You open the chest and see some items." + item_str)
        elif (p.y == 1) and (p.x == 1): print("This area is about" + item_str)

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
    global main_static_interactibles_array
    global pit_static_interactibles_array
    global floor_open
    global end
    trap_door_open = False
    box_open = False
    light_broken = False
    chest_open = False
    ladder_broken = False
    ##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung, rag, pocket_knife, shallow_motivational_card_deck
    if input in static_item_list:
        if input in p.inventory:
            if current_array is main_array:
                if input == "pencil":
                    if "sketched_map" in p.inventory:
                        print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                    else:
                        print("You can't use that here!")
                elif input == "yarn":
                    if (p.y == 1) and (p.x == 1) and (light_broken == False):
                        print("Holding the loose end, you throw the ball of yarn up toward the light hanging from the celing. It winds around the wire and then you pull down. The lamp comes crashing down, and now it's much darker.")
                        light_broken = True
                        main_item_array[p.y][p.x].append("broken_light_bulb")
                    else: print("You can't use that here!")
                elif input == "electric_wire":
                    if (p.y == 0) and (p.x == 2):
                        print(box_open, floor_open)#######
                        if (box_open == True) and (floor_open == False):
                            print("You see that there's a wire that's torn in two, you take the wire you picked up and attach the two loose ends, and see a spark. After a few moments, you hear a motor turn on and suddunly the floor below you opens up! You start falling...")
                            floor_open = True
                            current_array is pit_array
                            location_direct()(0, 0)
                        else: print("You can't use that here!")
                    elif (p.y == 3) and (p.x == 0):
                        if (p.inventory.count("electric_wire") >= 2) and ("pocket_knife" in p.inventory) and ("moist_rag" in p.inventory):
                            print("You squat down against the wall and think deeply. You take out the two electric wires and turn them around between your fingers. What to do now?? You let your arms fall to your sides as you ponder on what you could possibly do to get out of this utter puzzle of a basement. You probably don't have much time anyway... Soon your probable captors will come back down and knock you out again or drag you out. Is all hope lost??? ... *ZAP!!!* you feel a shock of electricity! You jump up and relaize the wires touched the outlet on the ground and shocked you. The current must have been very strong- there are burn marks on your hands. \"Great, now my hands are in pain and useless.\" However, a moment later an idea pops into your head... You run over to the door handle, and look at the wires. You go back to the outlet, take out the knife, and strip the wires. You stick one wire in at a time, making sure to not touch the metal. After the wires are secured, you go over to the door handle holding the wires and take a deep breath. You stick the negative wire way into the keyhole, and then press the positive end to the handle. The metal begins to heat up. After a few minutes, the metal is getting quite red. You wait a while longer, and take away the wires. You wrap the moist rag around the handle and it sizzles, you start to pull. You pull as hard as you can, bracing yourself against the door frame. The door slowly starts to move, and suddenly the door swings open, sending you tumbling to the floor. The light is blinding...")
                        end = 1
                    else: print("You can't use that here!")
                elif input == "sketched_map":
                    map_gen(main_array)
                elif input == "screwdriver":
                    if (p.y == 0) and (p.x == 2):
                        if box_open == False:
                            print("You look at the box on the corner of the wall, and look at the screwdriver in your hand. You get an idea. Why not? You proceed to wedge the end of the screwdriver in the space between the front panel of the box and itself. After some fiddling, the panel pops open and falls to the ground. The box appears to be some sort of electronic control system.")
                            box_open == True
                        else: print("You can't use that here!")
                    elif "drill" in p.inventory:
                        print("You start unscrewing the drill. Man does it look nasty in there. It probably has been unused for 30 years. You cough.")
                    else: print("You carve into the wall how many hours you've been down in this hell hole- Wait, how many has it been? You realize you have no sense of time.")
                elif input == "black_key":
                    if (p.y == 3) and (p.x == 0):
                        print("You put the black key in the key hole. Upon attempting to turn it, you hear a snap, and the key is now loose in the keyhole. You take it out, and the end of the key has snapped off. Crappy key.")
                        p.inventory.remove("black_key")
                        p.inventory.append("broken_key")
                    else: print("You can't use that here!")
                elif input == "rusty_key":
                    if (p.y == 3) and (p.x == 0):
                        print("You put the key in the keyhole of the door. After some fiddling, you get it to turn, but it's really sticky. After one whole turn the key is almost impossible to turn. You take it out.")
                elif input == "shiny_key":
                    if (p.y == 3) and (p.x == 0):
                        print("You put the key in the keyhole of the door. After some fiddling, you get it to turn. You continue turning it, but it can still turn even after two full roatations. Whats going on here?? You keep turning and turning and turning, but nothing is happening. \"Come ooooonnnnnnn!!!!\" Suddenly the door flings open!!!! ...")
                        end2()                    
                    else: print("You can't use that here!")
                elif input == "ladde_rung":
                    print("You tap the rung of the ladder on the floor. It sounds sort of like a marimba?")
                elif input == "drill":
                    if (p.y == 3) and (p.x == 0):
                        print("You try to plug the drill into the wall outlet, thinking you'll drill out the lock in the door. The cord doesnt reach.")
                    else: print("You can't use that here!")
                elif input == "rag":
                    if ((p.y == 1) and (p.x == 0)) or ((p.y == 2) and (p.x == 1)) :
                        print("You bend down and mop up some of the dankness with the rag. Why did you do this?? You don't know. But now you have a fairly moist rag.")
                        p.inventory.remove("rag")
                        p.inventory.append("moist_rag")
                    else: print("You can't use that here!")
                elif input == "dremel":
                    if (p.y == 3) and (p.x == 0):
                        if ("rusty_key" in p.inventory) and ("drill" in p.inventory):
                            print("You put a sanding but into the drill, and plug the drill into the outlet. You slowly go over the key and shave off all the rust. It's all nice and shiny now!")
                            p.inventory.remove("rusty_key")
                            p.inventory.append("shiny_key")
                        else:
                            print("You can't use that right now!")
                    else:
                        print("You can't use that here!")
                elif input == "pocket_knife":
                    pass
                else:
                    print("You can't use that here!")

            elif current_array is pit_array:
                if input == "pencil":
                    if "sketched_map" in p.inventory:
                        print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                    else:
                        print("You can't use that right now!")
                elif input == "sketched_map":
                    man_gen(pit_array)
                elif input == "screwdriver":
                    if (p.y == 1) and (p.x == 1) and (trap_door_open == False):
                        print("You try to pry the trap door open with the screwdriver. The end of the screwdriver gets pulled out of the handle - Oops.")
                        p.inventory.remove("screwdriver")
                        p.inventory.append("broken_screwdriver")
                    else:
                        print("You can't use that here!")
                elif input == "black_key":
                    if (p.y == 1) and (p.x == 1) and (trap_door_open == False):
                        print("You put the key into the lock in the trap door, and turn it. The lock clicks open!! You proceed to climb through the trap door.")
                        trap_door_open = True
                        current_array is main_array
                        location_direct()(1, 3)
                elif input == "rusty_key":
                    if (p.y == 1) and (p.x == 1) and (trap_door_open == False):
                        print("You put the rusty key in the trap door lock, and try to turn it. It snaps! Oh Nooooo!")
                        p.inventory.remove("rusty_key")
                        p.inventory.append("broken_key")
                elif input == "ladder_rung":
                    if (p.y == 1) and (p.x == 1) and (trap_door_open == False):
                        print("You wedge the rung of the ladder in between the space between the trap door and the celing. You twist it, and the trap door pops open! You proceed to climb through the trap door.")
                        trap_door_open = True
                        current_array is main_array
                        location_direct()(1, 3)
                elif input == "shallow_motivational_card_deck":
                    print(random.choice(random_motivational_cards))
                else:
                    print("You can't use that here!")
        else:
            print("You don't have that!")
    elif input in static_interactibles_list:
        if (current_array is main_array) and (input in main_static_interactibles_array[p.y][p.x]):  ### MAIN ARRAY INTERACTIBLES: ##
            if input == "box":
                if box_open == False:
                    print("You touch the outside of the metal box. It's cold.")
            elif input == "trap_door":
                if trap_door_open == False: print("You give the handle a try. It won't budge- it seems it's locked from the other side.")
            elif trap_door_open == True:
                print("You descend down the ladder...")
                current_array is pit_array
                location_direct()(1, 1)
            elif input == "door": print("You try the door again - still won't budge.")
        elif (current_array is pit_array) and (input in pit_static_interactibles_array[p.y][p.x]):  ## PIT ARRAY INTERACTIBLES: ###
            if input == "chest":
                if chest_open == False:
                    print("You slowly open the chest to reveal some miscellaneous things- the sort you'd find in a throwaway box in your old abandoned childhood room. You pull out a card case, and dust it off in your hands. I")
                elif chest_open == True:
                    print("You look in the chest again.")
            elif input == "ladder":
                if trap_door_open == False:
                    if ladder_broken == False:
                        print("You start climbing the ladder, and one of the rungs snaps off below you! You catch yourself. Maybe this is a bad idea.? Is there another way to get out of here? The trap door above you is locked.")
                        ladder_broken == True
                        pit_item_array[1][1].append("ladder_rung")
                    else:
                        print("You climb the ladder, but to no avail. The trap door above you is locked.")
                elif trap_door_open == True:
                    print("You climb the ladder...")
                    current_array is main_array
                    location_direct()(1, 3)
        else:
            print("That's not here!")
    else:
        print("That's not here!")


                
def get(input):
    global static_item_list
    global main_item_array
    global pit_item_array
    words = input.split()
    check_len = len(p.inventory) #used to see if it has changed
    if current_array is main_array:
        for item in static_item_list:
            if (words[-1] == item) and (item in main_item_array[p.y][p.x]):
                main_item_array[p.y][p.x].remove(item)
                p.inventory.append(item)
                print("You picked up a/an " + item)
                break
        if len(p.inventory) == check_len:
            print("That item isn't here!")
    elif current_array is main_array:
        for item in static_item_list:
            if (words[-1] == item) and (item in pit_item_array[p.y][p.x]):
                pit_item_array[p.y][p.x].remove(item)
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
    if current_array is main_array:
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
            print("\"What happened?\" you think in your head before you can speak. You fell very tired and dehydrated. You open your eyes, you're in the corner of a dimly lit room. Wait, where are you??? You quickly get onto your shaky feet. You look around what seems to be a basement- after looking around you, you notice theres a set of shelves behind you. There's not much on it, but you reliaze your getting distracted. \"Where am I, and how did I get here??\" Across from you you can see there's sort of a hallway leading to the left")
        if self.main_array_visit[0][0] >= 1:
            print("You're back to where you woke up, there are some miscellaneous things on the shelf against the wall.")
        self.main_array_visit[0][0] += 1
    def l010(self, lasty, lastx):
        if self.main_array_visit[1][0] == 0:
            print("The walls are smooth dark grey concrete, like the inside of that bunker in the sci-fi movie you watched. Wait, when did you watch that movie?? It seems like it has been an eternity, yet you also remember just watching it.")
        else:
            print("There's not much here. The ground seems kind of moist. You don't like it.")
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
        if self.main_array_visit[1][1] == 0:
            print("You enter into a larger room, about 4 times the size of the one you woke up in. There's a decrepit lamp hanging from the celing, well, more like just a lightbulb hanging from a wire. You hear a noise come from above you. -Oh no- are you not alone? Help!!!")
        elif self.main_array_visit[1][1] >= 1:
            print("There's a crappy light fixture hanging from the celing.")
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
        if floor_open == True:
            print("You fall!!")
            current_array is pit_array
            location_direct()(0, 0)
        else:
            print("You look around the space. Theres some things hanging on the walls, too far up to reach. There's also a mysterious metal box attached to the wall.")
        self.main_array_visit[0][2] += 1
    def l012(self, lasty, lastx):
        if self.main_array_visit[1][2] == 0:
            print("[[Write something here later]]")
        else:
            print("Your head hurts and you feel a little dizzy. If only you could find a little water or tylenol.")
        self.main_array_visit[1][2] += 1
    def l022(self, lasty, lastx):
        print("This area of the big room is quite bare, except for a rickity shelf with a toolbox on it. You go over and look at the toolbox.")
        self.main_array_visit[2][2] += 1
    def l013(self, lasty, lastx):
        if self.main_array_visit[1][3] == 0:
            print("Here theres a slighly smalle area off to the east side of the big room. There's what looks to be some sort of door in the floor here.")
        elif self.main_array_visit[1][3] >= 1:
            print("You are standing above the trap door.")
        self.main_array_visit[1][3] += 1
################################################################ PIT ARRAY::
    def l100(self, lasty, lastx):
        if self.pit_array_visit[0][0] == 0:
            print("You land hard on your butt, you've fallen about 6 feet. You look around and see that you're in a sort of hidden place underneath where you just were. You get up and dust yourself off.")
        elif self.pit_array_visit[0][0] >= 1:
            print("You're back to where fell. You look up into the room you fell from.")
        self.pit_array_visit[0][0] += 1
    def l110(self, lasty, lastx):
        if self.pit_array_visit[0][0] == 0:
            print("You proceed to adventure further into this small underground section. You see that it's not that expansive down here. There's a chest on the ground in the corner.")
        elif self.pit_array_visit[0][0] >= 1:
            print("Should you be down here?")
        self.pit_array_visit[1][0] += 1
    def l111(self, lasty, lastx):
        print("The end of this underground hideaway comes to a small section, jusr big enough for a body to fit in it. There's a wooden ladder leading up.")
        self.pit_array_visit[1][1] += 1
            
box_gen("Welcome to The Array Game!\n Alpha V1.4 \n  By Elijah Underhill-Miller")
box_gen("Instructions:\nFind your way out.")
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n  If you wish to use an object,\ntype its name.\n If you wish to pick up or drop an item, \n  type \"pick up\" or \"get\" or \"get\" preceding the item.") 
#Starting Position: 0, 0
main_array = [[1, 0, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 1, 0],
              [1, 1, 0, 0]]
main_item_array = [[["pencil", "drill"], [], ["yarn", "electric_wire"], []],
                   [[], [], [], ["rag"]],
                   [[], ["sketched_map", "screwdriver"], ["electric_wire", "dremel"], []],
                   [["black_key"], [], [], []]]
pit_array = [[1, 0],
             [1, 1]]
pit_item_array = [[[], []],
                  [["rusty_key, shallow_motivational_card_deck, pocket_knife"], []]]
random_motivational_cards = ["Be yourself.", "Put on lipstick.", "You are perfect.", "Be happy.", "Your dreams WILL come true.", "Smile.", "Beat they ass.", "Trust no bitch.", "Take a mindful walk.", "Remember to breath.", "Be creative.", "Try to learn new things, Set goals for yourself.","Be proud of yourself.","You've already accomplished so much!","You can achieve anything.","Only you know what you need.","Celebrate your success.","Create a personal mantra.", "You're growing every day.","Communicate to others around you.","Learn from other perspectives.", "stand up for what you believe in.","It's okay to ask questions.","Consider all the pros and cons.","Go for a long walk.","Balance is key.","Remember to unplug.","Make plans with yourself.","Think positive thoughts.","Do what comes naturally to you.","Follow your heart.","Track your progress with a friend.","Get rid of things that stress you out.","Eliminate distractions.","Make a new friend.","Treat yourself better.","Try aromatherapy.","Listen to a podcast.","Ask for help.","Stand up for yourself.","Don't stray from a challenge.","Think about everything you've overcome.", "Let people you love know it.","Optimism is contagious.","Spread kindness.","Follow your dreams.","Do what you love.","Explore your passions.","You can overcome anything.","Embrace opportunities.","Allow curiosity.","Keep your chin up.","Spend some time outdoors.","Remember to breath.","It's okay to make mistakes."]

floor_open = False
##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung \

main_static_interactibles_array = [[[], [], ["box"], []],
                             [[], [], [], ["trap_door"]],
                             [[], [], [], []],
                             [["door"], [], [], []]]
pit_static_interactibles_array = [[[], []],
                                  [["chest"], ["trap_door"]]]

static_item_list = []
static_interactibles_list = []

for a in [main_item_array, pit_item_array]:
    for row in a:
        for col in row:
            for item in col:
                if len(item) >= 1:
                    static_item_list.append(item)

for a in [main_static_interactibles_array, pit_static_interactibles_array]:
    for row in a:
        for col in row:
            for item in col:
                if len(item) >= 1:
                    static_interactibles_list.append(item)
                    
current_array = main_array
p = Player()
l = Location()
location_direct()(0, 0)
end = 0
while end == 0:
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
        stripped_inv = list(set(p.inventory))
        print("| Inventory: ")
        for item in stripped_inv: #Question: How do I make it list duplicate items as "| 2 pencils" or something like that?
            print("|",p.inventory.count(item),"x", item)
    elif (raw_input == "n") or (raw_input == "e")  or (raw_input == "s") or (raw_input == "w"):
        p.move(raw_input)
    elif "drop" in raw_input:
        drop(raw_input)
    elif (raw_input in static_item_list) or (raw_input in static_interactibles_list):
        use(raw_input)
    elif raw_input == "array":
        print(str(current_array))
    else: 
        print("Command not recognized")
############ END ########
if end == 1:
    print("Your eyes blink in the light of the ")
    end_credits()
if end == 2: pass

    
              
