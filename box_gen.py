#!/usr/bin/env python3
import math
input = "Welcome to Box Generator!  \n V 2.1\nBy Elijah Underhill-Miller"
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
