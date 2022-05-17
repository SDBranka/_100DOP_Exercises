from turtle import Turtle, Screen

# build timmy the turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("forestgreen")
timmy.speed(1)

# move timmy forward 100 pixels
timmy.forward(100)
# turn timmy to the right by 90 degrees
timmy.right(90)



my_screen = Screen()
my_screen.exitonclick()