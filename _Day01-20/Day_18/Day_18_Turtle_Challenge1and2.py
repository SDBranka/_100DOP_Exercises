#####Turtle Intro######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
timmy_the_turtle.forward(100)
timmy_the_turtle.backward(200)
timmy_the_turtle.right(90)
timmy_the_turtle.left(180)
timmy_the_turtle.setheading(0)


def draw_square(turtle, length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)


######## Challenge 1 - Draw a Square ############
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("forestgreen")
timmy.speed(1)

draw_square(timmy, 100)


# Challenge 2 - draw a dashed line
tommy = t.Turtle()
tommy.shape("turtle")
tommy.color("blue")
tommy.speed(1)
tommy.left(90)

def dashed_line(turtle, length, dash_length):
    total_length = 0
    while total_length < length:
        turtle.forward(dash_length)
        if turtle.isdown():
            turtle.penup()
        else:
            turtle.pendown()
        total_length += dash_length

dashed_line(tommy, 100, 10)

# # their solution
# for _ in range(15):
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
#     tommy.pendown()

screen = t.Screen()
screen.exitonclick()
