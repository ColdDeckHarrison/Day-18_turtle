import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.speed("fastest")
count = 0
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    my_tuple = (r, b, g)
    return my_tuple

for _ in range(360):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.left(1)
