# draw a random walk
import turtle as t
import random as rand


# COLORS = [
#     "red", "orange", "yellow", "green",
#     "blue", "indigo", "violet", "black"
# ]

DIRECTION = ["right", "left"]


def random_color():
    return (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0, 255))

def random_walk(turtle, steps):
    for i in range(steps):
        # turtle.color(rand.choice(COLORS))
        turtle.color(random_color())
        turtle.forward(rand.randint(1, 100))
        eval("turtle." + rand.choice(DIRECTION) + "(" + str(rand.randint(0, 360)) + ")")

# allows use of RGB values for colors
t.colormode(255)

# build timmy
timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed(3)
timmy.pensize(9)

random_walk(timmy, int(input("How many steps do you want to take? ")))

screen = t.Screen()
screen.exitonclick()