import turtle
timmy=turtle.Turtle()
def move_forward():
    timmy.forward(10)
screen=turtle.Screen()
screen.listen()
screen.onkey(move_forward,"space")
screen.exitonclick()