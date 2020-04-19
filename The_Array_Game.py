#!/usr/bin/env python3
import sys
import math
import random

def end_credits():
    box_gen("Thank you for playing \"The Array Game\"!!!\nCreated by Elijah Underhill-Miller\nSpecial thanks to Karl Fogel for helping!")

def box_gen(input):
    """Re-formats text and prints a box around it
    Arguments:
    input - string to be formatted
    """
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
    """Prints a version of the inputted array where "0" -> "#" & "1" -> "."
    Arguments:
    array - array
    """
    width = len(array[0]) 
    height = len(array)
    print("|" + "-" * width + "|")
    for j in range(height):
        print("|", end="", flush=True)
        for k in range(width):
            if array[j][k] == 1:
                print(".", end="", flush=True)
            elif array[j][k] == 2:
                print("*", end="", flush=True)
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

class Game:
    def __init__(self):
        self.main_array = [[1, 0, 1, 0],
                           [1, 1, 1, 1],
                           [0, 1, 1, 0],
                           [1, 1, 0, 0]]
        self.main_item_array = [[["pencil", "drill"], [], ["yarn", "electric_wire"], []],
                                [[], ["roast_turkey"], [], ["rag"]],
                                [[], ["sketched_map", "screwdriver"], ["electric_wire", "dremel_set", "battery"], []],
                                [["black_key"], [], [], []]]
        self.pit_array = [[1, 0],
                          [2, 1]]
        self.pit_item_array = [[[], []],
                               [["rusty_key", "shallow_motivational_card_deck", "pocket_knife"], []]]
        self.current_array = self.main_array
        self.random_motivational_cards = ["Be yourself.", "Put on lipstick.", "You are perfect.", "Be happy.", "Your dreams WILL come true.", "Smile.", "Beat they ass.", "Trust no bitch.", "Take a mindful walk.", "Remember to breath.", "Be creative.", "Try to learn new things, Set goals for yourself.","Be proud of yourself.","You've already accomplished so much!","You can achieve anything.","Only you know what you need.","Celebrate your success.","Create a personal mantra.", "You're growing every day.","Communicate to others around you.","Learn from other perspectives.", "stand up for what you believe in.","It's okay to ask questions.","Consider all the pros and cons.","Go for a long walk.","Balance is key.","Remember to unplug.","Make plans with yourself.","Think positive thoughts.","Do what comes naturally to you.","Follow your heart.","Track your progress with a friend.","Get rid of things that stress you out.","Eliminate distractions.","Make a new friend.","Treat yourself better.","Try aromatherapy.","Listen to a podcast.","Ask for help.","Stand up for yourself.","Don't stray from a challenge.","Think about everything you've overcome.", "Let people you love know it.","Optimism is contagious.","Spread kindness.","Follow your dreams.","Do what you love.","Explore your passions.","You can overcome anything.","Embrace opportunities.","Allow curiosity.","Keep your chin up.","Spend some time outdoors.","Remember to breath.","It's okay to make mistakes."]
        self.floor_open = False
        self.trap_door_open = False
        self.box_open = False
        self.light_broken = False
        self.chest_open = False
        self.ladder_broken = False
        ##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung \
        self.main_static_interactibles_array = [[[], [], ["box"], []],
                                                [[], [], [], ["trap_door"]],
                                                [[], [], [], []],
                                                [["door"], ["door"], [], []]]
        self.pit_static_interactibles_array = [[[], []],
                                               [["chest"], ["trap_door", "ladder"]]]
        self.static_item_list = []
        self.static_interactibles_list = []

        for a in [self.main_item_array, self.pit_item_array]:
            for row in a:
                for col in row:
                    for item in col:
                        if len(item) >= 1:
                            self.static_item_list.append(item)

        for a in [self.main_static_interactibles_array, self.pit_static_interactibles_array]:
            for row in a:
                for col in row:
                    for item in col:
                        if len(item) >= 1:
                            self.static_interactibles_list.append(item)

        self.end = 0
    def use(self, input):
        """Prints messages and changes values of variables based on player's loction and what item they want to use.
        Arguments:
        input - user's string input
        """
        ###############################
        #[0,0] |#######| [0,2] |#######
        #-----------------------------#
        #[1,0] | [1,1] | [1,2] | [1,3]#
        #-----------------------------#
        #######| [2,1] | [2,2] |#######
        #-----------------------------#
        #[3,0] | [3,1] |###############
        ###############################
        ##ITEMS: pencil, yarn, electric_wire, sketched_map, screwdriver, black_key, rusty_key, ladder_rung, rag, pocket_knife, shallow_motivational_card_deck
        if input in self.static_item_list:
            if input in p.inventory:
                if self.current_array is self.main_array:
                    if input == "pencil":
                        if "sketched_map" in p.inventory:
                            print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                        else:
                            print("You write on a wall a help message incase you are in a kidnapping situation and you get transfered to another place and someone finds this one. You write your name and age, as well as a short message.")
                    elif input == "yarn":
                        if (p.y == 1) and (p.x == 1) and (self.light_broken == False):
                            print("Holding the loose end, you throw the ball of yarn up toward the light hanging from the celing. It winds around the wire and then you pull down. The lamp comes crashing down, and now it's much darker.")
                            self.light_broken = True
                            print("light_broken = " + str(self.light_broken))
                            self.main_item_array[p.y][p.x].append("broken_light_bulb")
                            self.static_item_list.append("broken_light_bulb")
                        elif (p.y == 3) and (p.x == 0):
                            print("You feed the yarn through the keyhole, and suddenly someone (or something) grabs it from the other side and pulls. You let out a little squeal of suprise, and a giggle comes from the other side. \"What was that!?!\" You ask yourself. You back away from the door in fear.")
                        else:
                            print("You can't use that here!")
                    elif input == "electric_wire":
                        if (p.y == 0) and (p.x == 2):
                            if (self.box_open == True) and (self.floor_open == False):
                                print("You see that there's a wire that's torn in two, you take the wire you picked up and attach the two loose ends, and see a spark. After a few moments, you hear a motor turn on and suddunly the floor below you opens up! You start falling...")
                                self.floor_open = True
                                self.current_array = self.pit_array
                                p.y = 0
                                p.x = 0
                                l.location_direct(p.y, p.x)(0, 0)
                            else: print("You can't use that here!")
                        elif (p.y == 3) and (p.x == 0):
                            if (p.inventory.count("electric_wire") >= 2) and ("pocket_knife" in p.inventory) and ("moist_rag" in p.inventory):
                                print("You squat down against the wall and think deeply. You take out the two electric wires and turn them around between your fingers. What to do now?? You let your arms fall to your sides as you ponder on what you could possibly do to get out of this utter puzzle of a basement. You probably don't have much time anyway... Soon your probable captors will come back down and knock you out again or drag you out. Is all hope lost??? ... *ZAP!!!* you feel a shock of electricity! You jump up and relaize the wires touched the outlet on the ground and shocked you. The current must have been very strong- there are burn marks on your hands. \"Great, now my hands are in pain and useless.\" However, a moment later an idea pops into your head... You run over to the door handle, and look at the wires. You go back to the outlet, take out the knife, and strip the wires. You stick one wire in at a time, making sure to not touch the metal. After the wires are secured, you go over to the door handle holding the wires and take a deep breath. You stick the negative wire way into the keyhole, and then press the positive end to the handle. The metal begins to heat up. After a few minutes, the metal is getting quite red. You wait a while longer, and take away the wires. You wrap the moist rag around the handle and it sizzles, you start to pull. You pull as hard as you can, bracing yourself against the door frame. The door slowly starts to move, and suddenly the door swings open, sending you tumbling to the floor. The light is blinding...")
                                self.end = 1
                            else:
                                print("You can't use that right now!")
                        else: print("You can't use that here!")
                    elif input == "sketched_map":
                        map_gen(self.main_array)
                    elif input == "screwdriver":
                        if (p.y == 0) and (p.x == 2):
                            if self.box_open == False:
                                print("You look at the box on the corner of the wall, and look at the screwdriver in your hand. You get an idea. Why not? You proceed to wedge the end of the screwdriver in the space between the front panel of the box and itself. After some fiddling, the panel pops open and falls to the ground. The box appears to be some sort of electronic control system.")
                                self.box_open = True
                            else: print("You can't use that here!")
                        elif (p.y == 1) and (p.x == 3):
                            if self.trap_door_open == False:
                                print("You take out the screwdriver and look around the trapdoor to see if there's anything to unscrew. Theres a few flathead screws securing the handle, but you wouldn't want to unscrew those...")
                            else:
                                print("You can't use that now!")
                        elif "drill" in p.inventory:
                            print("You unscrew the drill. Man does it look nasty in there. It probably has been unused for 30 years. You cough.")
                        else: print("You carve into the wall how many hours you've been down in this hell hole- Wait, how many has it been? You realize you have no sense of time.")
                    elif input == "black_key":
                        if (p.y == 3) and (p.x == 0):
                            print("You put the black key in the key hole. Upon attempting to turn it, you hear a snap, and the key is now loose in the keyhole. You take it out, and the end of the key has snapped off. Crappy key.")
                            p.inventory.remove("black_key")
                            p.inventory.append("broken_key")
                            self.static_item_list.append("broken_key")
                        elif (p.y == 3) and (p.x == 1):
                            print("You try to fit the key in the lock, but it doesn't fit in.")
                        else: print("You can't use that here!")
                    elif input == "rusty_key":
                        if (p.y == 3) and (p.x == 0):
                            print("You put the key in the keyhole of the door. After some fiddling, you get it to turn, but it's really sticky. After one whole turn the key is almost impossible to turn. You take it out. Maybe if the rust was grinded up it work work??")
                        elif (p.y == 3) and (p.x == 1):
                            print("You make your way to the closet door and test the key. It doesn't fit.")
                        else:
                            print("You can't use that here!")
                    elif input == "shiny_key":
                        if (p.y == 3) and (p.x == 0):
                            print("You put the key in the keyhole of the door. After some fiddling, you get it to turn. You continue turning it, but it can still turn even after two full roatations. Whats going on here?? You keep turning and turning and turning, but nothing is happening. \"Come ooooonnnnnnn!!!!\" Suddenly the door flings open!!!! ...")
                            self.end = 2                    
                        else: print("You can't use that here!")
                    elif input == "ladder_rung":
                        print("You tap the rung of the ladder on the floor. It sounds sort of like a marimba?")
                    elif input == "drill":
                        if (p.y == 3) and (p.x == 0):
                            print("You try to plug the drill into the wall outlet, thinking you'll drill out the lock in the door. The cord doesnt reach.")
                        elif (p.y == 1) and (p.x == 3):
                            if ("battery" in p.inventory) and ("electric_wire" in p.inventory) and (trap_door_open == False):
                                print("You hold the drill to the trap door, and connect up the battery with the wires. The drill whirs to life, and you press down on the drill. It doesn't have much power, and the drill stalls out. That's some heavy duty trapdoor- maybe there's something important down wherever it leads.")
                            else:
                                print("You can't use that right now!")
                        elif (p.y == 0) and (p.x == 2):
                            if ("battery" in p.inventory) and ("electric_wire" in p.inventory) and (box_open == False):
                                print("You hold the drill to the metal box, and connect up the battery with the wires. The drill whirs to life, and you press down on the drill. The drill isnt sharp enough to penetrate the metal. You press harder, and the drill bit snaps!!! A piece of drill bit flies off of grazes your head. Thank the lord you're alive!")
                            else:
                                print("You can't use that right now!")
                        else: print("You can't use that here!")
                    elif input == "rag":
                        if ((p.y == 1) and (p.x == 0)) or ((p.y == 2) and (p.x == 1)):
                            print("You bend down and mop up some of the dankness with the rag. Why did you do this?? You don't know. But now you have a fairly moist rag.")
                            p.inventory.remove("rag")
                            p.inventory.append("moist_rag")
                            self.static_item_list.append("moist_rag")
                        else: print("You can't use that here!")
                    elif input == "dremel_set":
                        if ("rusty_key" in p.inventory) and ("drill" in p.inventory):
                            print("You take out a sanding bit from the dremel set and put it into the drill, and wire up the drill to the battery with the wire. You slowly go over the key and shave off all the rust. It's all nice and shiny now!")
                            p.inventory.remove("rusty_key")
                            p.inventory.append("shiny_key")
                            self.static_item_list.append("shiny_key")
                        else:
                            print("You can't use that right now!")
                    elif input == "pocket_knife":
                        if ((p.y == 1) and (p.x == 3)) or ((p.y == 0) and (p.x == 0)):
                            print("You carve a little man into the wood.")
                        elif "roast_turkey" in p.inventory:
                            print("You take out your pocket knife and cut into the sauced turkey skin. It's very well cooked. You take a bite and feel instantly refreshed!")
                        else:
                            print("You can't use that right now!")
                    else:
                        print("You can't use that here!") ###### PIT ARRAY ITEM USES ######

                elif self.current_array is self.pit_array:
                    if input == "pencil":
                        if "sketched_map" in p.inventory:
                            print("You draw a picture of a robo turk on the map. Frankly it looks quite creepy. The mustly atmosphere of this place combined with occasional glimpes of the robo turk is not a good combination.")
                        else:
                            print("You can't use that right now!")
                    elif input == "sketched_map":
                        map_gen(self.pit_array)
                    elif input == "screwdriver":
                        if (p.y == 1) and (p.x == 1) and (self.trap_door_open == False):
                            print("You try to pry the trap door open with the screwdriver. The end of the screwdriver gets pulled out of the handle - Oops.")
                            p.inventory.remove("screwdriver")
                            p.inventory.append("broken_screwdriver")
                            self.static_item_list.append("broken_screwdriver")
                        else:
                            print("You can't use that here!")
                    elif input == "black_key":
                        if (p.y == 1) and (p.x == 1) and (self.trap_door_open == False):
                            print("You put the key into the lock in the trap door, and turn it. The lock clicks open!! You proceed to climb through the trap door.")
                            self.trap_door_open = True
                            self.current_array = self.main_array
                            p.y = 1
                            p.x = 3
                            l.location_direct(p.y, p.x)(1, 3)
                    elif input == "rusty_key":
                        if (p.y == 1) and (p.x == 1) and (self.trap_door_open == False):
                            print("You put the rusty key in the trap door lock, and try to turn it. It snaps! Oh Nooooo!")
                            p.inventory.remove("rusty_key")
                            p.inventory.append("broken_key")
                            self.static_item_list.append("broken_key")
                    elif input == "ladder_rung":
                        if (p.y == 1) and (p.x == 1) and (self.trap_door_open == False):
                            print("You wedge the rung of the ladder in between the space between the trap door and the celing. You twist it, and the trap door pops open! You proceed to climb through the trap door...")
                            self.trap_door_open = True
                            self.current_array = self.main_array
                            p.y = 1
                            p.x = 3
                            l.location_direct(p.y, p.x)(1, 3)
                    elif input == "shallow_motivational_card_deck":
                        print(random.choice(self.random_motivational_cards))
                    elif input == "battery":
                        if (p.y == 0) and (p.x == 2) and (box_open == True):
                            print("You connect up the battery to some wires to see what'l happen. Nothing happens.")
                        else:
                            print("You can't use that here!")
                    else:
                        print("You can't use that here!")
            else:
                print("You don't have that!")
        elif input in self.static_interactibles_list:
            if (self.current_array is self.main_array) and (input in self.main_static_interactibles_array[p.y][p.x]):  ### MAIN ARRAY INTERACTIBLES: ##
                if (input == "box") or (input == "metal_box"):
                    if self.box_open == False:
                        print("You touch the outside of the metal box. It's cold.")
                elif input == "trap_door":
                    if self.trap_door_open == False: print("You give the handle a try. It won't budge- it seems it's locked from the other side.")
                    elif self.trap_door_open == True:
                        print("You descend down the ladder...")
                        self.current_array = self.pit_array
                        p.y = 1
                        p.x = 1
                        l.location_direct(p.y, p.x)(1, 1)
                elif input == "door":
                    if (p.y == 3) and (p.x == 0):
                        print("You try the door again - still won't budge.")
                    elif (p.y == 3) and (p.x == 1):
                        print("You try the door- it wiggles a little in its frame, but doesn't open.")
            elif (self.current_array is self.pit_array) and (input in self.pit_static_interactibles_array[p.y][p.x]):  ## PIT ARRAY INTERACTIBLES: ###
                if input == "chest":
                    if self.chest_open == False:
                        print("You slowly open the chest to reveal some miscellaneous things- the sort you'd find in a throwaway box in your old abandoned childhood room. You pull out a card case, and dust it off in your hands. It says \"Motivational Cards\" - \"Whats that?\" you ask yourself.")
                    elif self.chest_open == True:
                        print("You look in the chest again.")
                elif input == "ladder":
                    if self.trap_door_open == False:
                        if self.ladder_broken == False:
                            print("You start climbing the ladder, and one of the rungs snaps off below you! You catch yourself. Maybe this is a bad idea.? Is there another way to get out of here? The trap door above you is locked.")
                            self.ladder_broken = True
                            self.static_item_list.append("ladder_rung")
                            self.pit_item_array[1][1].append("ladder_rung")
                        else:
                            print("You climb the ladder, but to no avail. The trap door above you is locked.")
                    elif self.trap_door_open == True:
                        print("You climb the ladder...")
                        self.current_array = self.main_array
                        p.y = 1
                        p.x = 3
                        l.location_direct(p.y, p.x)(1, 3)
                elif input == "trap_door":
                    if self.trap_door_open == False:
                        print("The trap door is locked. It's a no-go.")
                    elif self.trap_door_open == True:
                        print("You climb up th ladder and exit through the trap door...")
                        self.current_array = self.main_array
                        p.y = 1
                        p.x = 3
                        l.location_direct(p.y, p.x)(1, 3)
            else:
                print("That's not here!")
        else:
            print("That's not here!")


def look():
    """Prints a message based on thge player's location if the player issues the "look" command.
    Arguments:
    p.y & p.x - players location
    """
    ###############################
    #[0,0] |#######| [0,2] |#######
    #-----------------------------#
    #[1,0] | [1,1] | [1,2] | [1,3]#
    #-----------------------------#
    #######| [2,1] | [2,2] |#######
    #-----------------------------#
    #[3,0] | [3,1] |###############
    ###############################    
    if g.current_array is g.main_array:
        items_here = []
        item_str = " You see here"
        if len(g.main_item_array[p.y][p.x]) >= 1:
            for item in g.main_item_array[p.y][p.x]:
                item_str = item_str + " a/an " + item + ","
        else:
            item_str = ""    
        if (p.y == 0) and (p.x == 0): print("You inspect the room further- you find that you eyes have adjusted and it's quite easy to see in the room. There's lots of dust around the edge of the floor." + item_str)
        elif (p.y == 1) and (p.x == 0): print("Upon further inspection, there's not much here." + item_str)        
        elif (p.y == 3) and (p.x == 0): print("You take a closer look at the door. You scan around the edges, but you cant see any light coming from the other side. Either the other side is pitch black or this is really well fitted door - maybe designed not to be able to peek through..." + item_str)
        elif (p.y == 1) and (p.x == 1): print("You look around and think - \"What to do.. What to do..\"" + item_str)
        elif (p.y == 2) and (p.x == 1): print("The floor is ... cold. You look up and see theres liquid dripping from the ceiling. Ewww." + item_str)
        elif (p.y == 3) and (p.x == 1): print("This area seems to be kept up a little more. Theres no nasty goo anywhere and theres also nice little soft piece of rug to stand on." + item_str)
        elif (p.y == 0) and (p.x == 2): print("This area is suspicious. The floor feels uneven - you probably shouldn't stay here for long." + item_str)
        elif (p.y == 1) and (p.x == 2): print("You look around at the ceiling because it seems a little broken up here. You squint and make out that above the ceiling there seem to be some wooden floorboards." + item_str)
        elif (p.y == 2) and (p.x == 2): print("There's a toolbox on the rickity shelf. You open it." + item_str)
        elif (p.y == 1) and (p.x == 3): print("You take a closer look at the trap door. It's fairly small, and made out of thick wooden boards encased in cast iron. This looks like some medieval shit." + item_str)
    elif g.current_array is g.pit_array:
        items_here = []
        item_str = " You see here"
        if len(g.pit_item_array[p.y][p.x]) >= 1:
            for item in g.pit_item_array[p.y][p.x]:
                item_str = item_str + " a/an " + item + ","
        else:
            item_str = ""
        if (p.y == 0) and (p.x == 0): print("There's a lot of dirt in here. It looks like someone started to dig this hole but then forgot to finish it. The onyl thing that seems to be preventing the dirt walls from collapsing in on you are the janky wooden panels nailed to eachother around the edge. The floor is solid compacted dirt - cold to the touch." + item_str)
        elif (p.y == 1) and (p.x == 0): print("You inspect the chest further. It's has the same style as the trapdoor. Thick and medival looking. It has a cast iron latch which doesn't have a lock on it. You open the chest and see some items." + item_str)
        elif (p.y == 1) and (p.x == 1): print("This area is about the size of a very small bathroom - one that would only have enough room for about a sink and a European toilet." + item_str)



class Player:
    def __init__(self): 
        self.y = 0
        self.x = 0
        self.inventory = []
    def move(self, direction):
        """Gives player ability to move.
        Arguments:
        direction - n, e, s, w
        """
        y_limit = len(g.current_array) - 1
        x_limit = len(g.current_array[0]) - 1
        if(direction == "n") and (g.current_array[self.y-1][self.x] != 0) and (self.y-1 >= 0):
            self.y -= 1
            l.location_direct(p.y, p.x)(self.y+1, self.x)
        elif(direction == "e") and (self.x+1 <= x_limit) and (g.current_array[self.y][self.x+1] != 0):
            self.x += 1
            l.location_direct(p.y, p.x)(self.y, self.x-1)
        elif(direction == "s") and (self.y+1 <= y_limit) and (g.current_array[self.y+1][self.x] != 0):
            self.y += 1
            l.location_direct(p.y, p.x)(self.y-1, self.x)
        elif(direction == "w") and (g.current_array[self.y][self.x-1] != 0) and (self.x-1 >= 0):
            self.x -= 1
            l.location_direct(p.y, p.x)(self.y, self.x+1)
        else:
            print("You can't go there!")
    def get(self, input):
        """Gives player ability to pick up items."""
        words = input.split()
        check_len = len(self.inventory) #used to see if it has changed
        if check_len < 6:
            if g.current_array is g.main_array:
                for item in g.static_item_list:
                    if (words[-1] == item) and (item in g.main_item_array[p.y][p.x]):
                        g.main_item_array[p.y][p.x].remove(item)
                        self.inventory.append(item)
                        print("You picked up a/an " + item)
                        break
                if len(self.inventory) == check_len:
                    print("That item isn't here!")
            elif g.current_array is g.pit_array:
                for item in g.static_item_list:
                    if (words[-1] == item) and (item in g.pit_item_array[p.y][p.x]):
                        print("recgonnized item")
                        g.pit_item_array[p.y][p.x].remove(item)
                        self.inventory.append(item)
                        print("You picked up a/an " + item)
                        break
                if len(self.inventory) == check_len:
                    print("That item isn't here!")
        else:
            print("Your inventory is full!")

    def drop(self, input):
        """Gives player ability to drop items."""
        words = input.split()
        if g.current_array is g.main_array:
            if words[-1] in self.inventory:
                self.inventory.remove(words[-1])
                g.main_item_array[p.y][p.x].append(words[-1])
                print("You dropped a/an " + words[-1])
            else:
                print("You don't have that item!")
        if g.current_array is g.pit_array:
            if words[-1] in self.inventory:
                self.inventory.remove(words[-1])
                g.pit_item_array[p.y][p.x].append(words[-1])
                print("You dropped a/an" + words[-1])
            else:
                print("You don't have that item!")
        

        
class Location:
    def __init__(self):
        self.main_array_visit = [[0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0],
                                 [0, 0, 0, 0]]
        self.pit_array_visit = [[0, 0],
                                [0, 0]]
        self.main_array_direct = [[self.l000, 0, self.l002, 0],
                                  [self.l010, self.l011, self.l012, self.l013],
                                  [0, self.l021, self.l022, 0],
                                  [self.l030, self.l031, 0, 0]]
        self.pit_array_direct = [[self.l100, 0],
                                 [self.l110, self.l111]]
    def location_direct(self, y, x):
        if g.current_array is g.main_array:
            return self.main_array_direct[y][x]
        elif g.current_array is g.pit_array:
            return self.pit_array_direct[y][x]
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
            print("You enter into a larger room, about 4 times the size of the one you woke up in. There's a decrepit lamp hanging from the celing, well, more like just a lightbulb hanging from a wire. You hear a noise come from above you. -Oh no- are you not alone? Help!!! You foot comes down on a juicy fat piece of meat. What?")
        elif self.main_array_visit[1][1] >= 1:
            print("There's some animal grease on the floor, and a crappy light fixture hanging from the celing.")
        self.main_array_visit[1][1] += 1
    def l021(self, lasty, lastx):
        if (lasty == 3) and (lastx == 1):
            print("From this direction, you see that theres a slice of paper wedged in between the wall and the pipe")
        else:
            print("There's a large pipe on one side of the room, it looks like it carries fluids.")
        self.main_array_visit[2][1] += 1
    def l031(self, lasty, lastx):
        if self.main_array_visit[3][1] == 0:
            print("Ahead of you you see that this passage is going to come to an end, you squeeze through some empty cardboard boxes to see what else there is here.")
        elif (lasty == 3) and (lastx == 0):
            print("Through the cardboard boxes you see some sort of door in the wall - maybe a closet?")
        elif self.main_array_visit[3][1] >= 1:
            print("Thank god it's not wet here. Why is it so wet in this basement?")
        self.main_array_visit[3][1] += 1
    def l002(self, lasty, lastx):
        if g.floor_open == True:
            print("You fall!!")
            g.current_array = g.pit_array
            p.y = 0
            p.x = 0
            l.location_direct(p.y, p.x)(0, 0)
        else:
            print("You look around the space. Theres some things hanging on the walls, too far up to reach. There's also a mysterious metal box attached to the wall.")
        self.main_array_visit[0][2] += 1
    def l012(self, lasty, lastx):
        if (lasty == 1) and (lastx == 1):
            print("Your head hurts and you feel a little dizzy. If only you could find a little water or tylenol.")
        elif (lasty == 0) and (lastx == 2):
            print("Your back into the big room, but are a little confused as to where how are situated and where you first came from.")
        elif (lasty == 2) and (lastx == 2):
            print("You're still in the the big room, but there's something that goes off to your left.")
        elif (lasty == 1) and (lastx == 3):
            print("You emerge from the area off to the side with the floor door.")
        self.main_array_visit[1][2] += 1
    def l022(self, lasty, lastx):
        print("This area of the big room is quite bare, except for a rickity shelf with a toolbox on it. You go over and look at the toolbox.")
        self.main_array_visit[2][2] += 1
    def l013(self, lasty, lastx):
        if self.main_array_visit[1][3] == 0:
            print("Here theres a slighly small area off to the east side of the big room. There's what looks to be some sort of door in the floor here.")
        elif self.main_array_visit[1][3] >= 1:
            print("You are standing above the trap door.")
        self.main_array_visit[1][3] += 1
################################################################ PIT ARRAY::
    def l100(self, lasty, lastx):
        if self.pit_array_visit[0][0] == 0:
            print("You land hard on your butt, you've fallen about 6 feet. You look around and see that you're in a sort of hidden place underneath where you just were. You get up and dust yourself off.")
        elif self.pit_array_visit[0][0] >= 1:
            print("You're back to where you fell. You look up into the room you fell from.")
        self.pit_array_visit[0][0] += 1
    def l110(self, lasty, lastx):
        if self.pit_array_visit[1][0] == 0:
            print("You proceed to adventure further into this small underground section. You see that it's not that expansive down here. There's a chest on the ground in the corner.")
        elif self.pit_array_visit[0][0] >= 1:
            print("Should you be down here?")
        self.pit_array_visit[1][0] += 1
    def l111(self, lasty, lastx):
        print("The end of this underground hideaway comes to a small section, jusr big enough for a body to fit in it. There's a wooden ladder leading up.")
        self.pit_array_visit[1][1] += 1
            
box_gen("Welcome to The Array Game V1.00! \n  By Elijah Underhill-Miller")
box_gen("Instructions:\nWhere are you???")
box_gen("Commands: \n n, e, s, w, = Movement \n l = Look, i = Inventory\n  If you wish to use an object,\nstationary or carryable, \n type its name with underscores between words or \n as it appears in your inventory.\n If you wish to pick up or drop an item, \n type \"pick up\" or \"get\" or \"take\" or \"drop\" \n  preceding the item.\nType \"exit game\" to exit. Progress is NOT saved.")
box_gen("Have fun!!")
                    

g = Game()
p = Player()
l = Location()
g.current_array = g.main_array ##initialize starting array
l.location_direct(p.y, p.x)(0, 0) ##initizalize position

while g.end == 0:
    raw_input = str(input("--> "))
    raw_input = raw_input.strip().lower()
    if raw_input == "exit game":
        print("Goodbye!!")
        break
    elif ("get" in raw_input) or ("take" in raw_input) or ("pick up" in raw_input):
        p.get(raw_input)
    elif raw_input == "location":
        print("Location: " + "[" + str(p.y) + "][" + str(p.x) + "]")
    elif (raw_input == "l") or (raw_input == "look"):
        look()
    elif raw_input == "i":
        stripped_inv = list(set(p.inventory))
        print("| Inventory: ")
        for item in stripped_inv:
            print("|",p.inventory.count(item),"x", item)
    elif (raw_input == "n") or (raw_input == "e")  or (raw_input == "s") or (raw_input == "w"):
        p.move(raw_input)
    elif "drop" in raw_input:
        p.drop(raw_input)
    elif (raw_input in g.static_item_list) or (raw_input in g.static_interactibles_list):
        g.use(raw_input)
    else: 
        print("Command not recognized")
############ END ########
delay = input("Enter anything to continue --> ")
if g.end == 1:
    print("-------------\nYour eyes are trying to adjust to the light - the whiteness starts to lessen and shapes begin to appear in your field of view. A voice calls out from the white abyss: \"Honey, you look like shit.\" What? Who is this? are you in heaven??? The voice continues: \"Why are you on the floor? Have you gotten the- the.. I don't know the thing I wanted you to get I forgot what it was.\" You answer with a quivering voice: \"Uh... no?\" \"Oh, come on!!\" \"Please don't hurt me!\" A figure starts to emerge from the light... You realize that it's your wife!!! What?!?! What kind of sick game is this?? Where are you?? You say to her: \"What are you doing here!!!\" \"What do you mean... this is our house.\" A switch suddenly get flipped in your brain. You were in your basement the whole time. You must have been knocked out while trying to get things off of the wooden shelf when you woke up. Should you take a concussion test?\n-------------")
    delay = input("Enter anything to continue --> ")
    end_credits()
if g.end == 2:
    print("-------------\nYour eyes are trying to adjust to the light - the whiteness starts to lessen and shapes begin to appear in your field of view. A voice calls out from the white abyss: \"Honey, you look like shit.\" What? Who is this? are you in heaven??? The voice continues: \"Why are you standing so awkwardly? Have you gotten the- the.. I don't know the thing I wanted you to get I forgot what it was.\" You answer with a quivering voice: \"Uh... no?\" \"Oh, come on!!\" \"Please don't hurt me!\" A figure starts to emerge from the light... You realize that it's your wife!!! What?!?! What kind of sick game is this?? Where are you?? You say to her: \"What are you doing here!!!\" \"What do you mean... this is our house.\" A switch suddenly get flipped in your brain. You were in your basement the whole time. You must have been knocked out while trying to get things off of the wooden shelf when you woke up. Should you take a concussion test?\n-------------")
    delay = input("Enter anything to continue --> ")
    end_credits()
    

    
              
