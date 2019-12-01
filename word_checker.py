#!/usr/bin/env python3

import sys

bad_words = ["like", "very", "really"]

print("Welcome to Word Checker 1.0!")
#pre_raw_input = str(input("Enter Words Here: "))
file_input = open("test_text.rtf","r")
pre_raw_input = file_input.read().replace('\n', '')
file_input.close()
print("pre raw input = " + pre_raw_input)
raw_input = pre_raw_input.lower().strip()
def fix(user_input):
    for word in bad_words:
        while True:
            start_point = user_input.find(word)
            if start_point == -1: # (if there no more)
                break
            delta_char = start_point
            #print("delta_char = " + str(delta_char))
            #print("len(user_input) = " + str(len(user_input)))            
            while user_input[delta_char].isspace() != True:
                delta_char += 1
                if delta_char >= len(user_input):
                    break
            next_start = min(delta_char + 1, len(user_input))
            user_input = user_input.replace(user_input[start_point:next_start], "")
    print(user_input)
    
def ask():
    has_bad = False
    for x in range(len(bad_words)):
        if bad_words[x] in raw_input:
            has_bad = True
    if has_bad:
        print("Found some bad words!")
        check_input = str(input("Fix words?[y/n]")).strip().lower()
        if "y" in check_input:
            fix(raw_input) 
        elif "n" in check_input:
            print("OK!")
    else:
        print("No bad words!")
ask()

    
