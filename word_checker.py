#!/usr/bin/env python3

import sys

bad_words = ["like", "very", "really"]

print("Welcome to Word Checker 1.0!")
num_bad_words = len(bad_words)
pre_raw_input = str(input("Enter Words Here: "))
raw_input = pre_raw_input.lower()
def fix(user_input):
    user_input.strip()
    user_input.lower()
    #print("stating char position = " + str(user_input.find("like")))
    count = 0
    for rounds in range(3): # Counts how many bad words there are
        #print("Round: " + str(rounds))
        start_char = 0
        while True:
            a = user_input.find(bad_words[rounds],start_char)
            if a == -1: # (if there no more)
                break
            count+=1
            start_char=a+1
        rounds+=1
    for rounds in range(count):
        if "like" in user_input:
            x = user_input.find("like")
        elif "very" in user_input:
            x = user_input.find("very")
        elif "really" in user_input:
            x = user_input.find("really")
        delta_char = x
        while user_input[delta_char].isspace() != True:
            delta_char += 1
        fixed_input = user_input.replace(user_input[x:delta_char + 1], "")
    print(fixed_input)
    
def ask():
    val = False
    for x in range(3):
        if bad_words[x] in raw_input:
            val = True
    if val == True:
        print("Found some bad words!")
        check_input = str(input("Fix words?[y/n]"))
        check_input.strip()
        check_input.lower()
        if "y" in check_input:
            fix(raw_input) 
        elif "n" in check_input:
            print("OK!")
    else:
        print("No bad words!")
ask()

    
