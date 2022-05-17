from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
# change timmy's color
timmy.color("green")
print(timmy)
# move timmy forward by 100 pixels
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
