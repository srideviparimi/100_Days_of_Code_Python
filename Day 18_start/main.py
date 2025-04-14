import turtle

timmy=turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")
color_list=["yellow","orange","red","green","blue","violet","black","cyan1","green"]
index=0
for no_of_sides in range(3,11):
    for i in range(no_of_sides):
        timmy.right(360/no_of_sides)
        timmy.forward(100)
    no_of_sides+=1
    index+=1
    timmy.color(color_list[index])



screen=turtle.Screen()
screen.exitonclick()