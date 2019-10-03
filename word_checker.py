#!/usr/bin/env python3

import sys
# here are some really bad word like

bad_words = ["like", "very", "really"]

def check(user_input):
    for bad_word in bad_words:
        if bad_word in user_input:
            print("Found!")

sys.stdout.write("Enter Words Here: ")
sys.stdout.flush()
raw_input = sys.stdin.readline()

check(raw_input)
    
