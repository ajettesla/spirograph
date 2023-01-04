import random
import turtle
from turtle import *

timmy = Turtle()
turtle.colormode(255)
k = random.randint(10, 90)
print(timmy.heading())
timmy.speed("fastest")
for i in range(10000):
    timmy.pensize(2)
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    timmy.pencolor(r, g, b)
    timmy.setheading(timmy.heading() + k)
    timmy.circle(50)
