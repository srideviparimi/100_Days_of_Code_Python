from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(500,400)
screen.title("Welcome to the turtle Race!...")
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle wins the race?Enter the color:(red/orange/yellow/green/blue/purple")
turtle_list=[]
is_race_on=False
def go_to_starting_point():
    colors=["red","orange","yellow","green","blue","purple"]
    y=-100
    index=0
    for i in range(0,6):
        turtle_obj=Turtle(shape="turtle")
        turtle_obj.penup()
        turtle_obj.color(colors[index])
        turtle_obj.setpos(-220,y)
        y+=40
        index+=1
        turtle_list.append(turtle_obj)

go_to_starting_point()
winner=""
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtle_list:
        random_distance=random.randint(0,10)
        if turtle.xcor()<=200:
            turtle.forward(random_distance)
        else:
            is_race_on=False
            winner=turtle.color()[0]

if user_bet==winner:
    print(f"Yeah, You turtle {winner} won. ")
else:
    print(f"Oh no You lose. The winner is {winner}")

screen.bye()
