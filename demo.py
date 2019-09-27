#!/usr/bin/env python3

import turtle

x = int(input("Enter #:"))
i = 0
turtle.color("green", "purple")
turtle.begin_fill()
while i < x:
    turtle.forward(50)
    turtle.left(360/x)
    i = i+1
turtle.end_fill()
turtle.done()


#  i=0
#  while True:
#      turtle.forward(50)
#      turtle.left(360/x)
#      turtle.end_fill()
#      i + 1
#      if i == x:
#          break
#      turtle.done()
#      turtle.forward(50)
#      turtle.left(360/x)
    
    
