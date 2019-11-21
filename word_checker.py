#!/usr/bin/env python3

import sys
# here are some really bad word like

bad_words = ["like", "very", "really"]

print("Welcome to Word Checker 1.0!")
raw_input = str(input("Enter Words Here: "))
raw_input.lower()
def fix(user_input):
    user_input.strip()
    user_input.lower()
    print("stating char position = " + str(user_input.find("like")))
    x = user_input.find("like")
    delta_char = x
    while user_input[delta_char].isspace() != True:
        delta_char += 1
    fixed_input = user_input.replace(user_input[x:delta_char + 1], "")
    print(fixed_input)
    
def ask():
    val = False
    if bad_words[0] in raw_input:
        val = True
    if bad_words[1] in raw_input:
        val = True
    if bad_words[2] in raw_input:
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

    
