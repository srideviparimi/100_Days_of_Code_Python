import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
timmy=Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.circle(100)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
def draw_spirograph(size):
    for i in range(360//size):
        timmy.color(random_color())
        current_heading=timmy.heading()
        timmy.setheading(current_heading+size)
        timmy.circle(100)

draw_spirograph(10)
screen=Screen()
screen.exitonclick()