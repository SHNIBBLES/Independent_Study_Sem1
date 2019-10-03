#!/usr/bin/env python3

import turtle

x = int(input("Enter the number of sides: "))
turtle.color("green", "purple")
turtle.begin_fill()
for i in range(x):
    turtle.forward(50)
    turtle.left(360/x)
turtle.end_fill()
turtle.done()
