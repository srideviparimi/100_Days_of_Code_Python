from turtle import Turtle,Screen


def move_forwards():
    timmy.forward(50)

def move_backwards():
    timmy.backward(50)

def clockwise():
    new_heading=timmy.heading()-10
    timmy.setheading(new_heading)

def counter_clockwise():
    new_heading=timmy.heading()+10
    timmy.setheading(new_heading)
def clear_screen():
    timmy.reset()
timmy=Turtle()
screen=Screen()
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(clockwise,"d")
screen.onkey(counter_clockwise,"a")
screen.onkey(clear_screen,"c")
screen.exitonclick()