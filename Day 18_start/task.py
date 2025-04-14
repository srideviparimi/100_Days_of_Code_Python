import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("circle")
timmy.width(10)

turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
def function():
    """changes random colors and returns random direction"""
    directions=[0,90,180,270]
    color=random_color()
    timmy.pencolor(color)
    return random.choice(directions)
for i in range(100):
    angle=function()
    timmy.forward(30)
    timmy.setheading(angle)

timmy.speed("fastest")



screen=Screen()
screen.exitonclick()