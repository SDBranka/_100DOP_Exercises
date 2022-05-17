# 10 x 10 dot matrix
# each dot 20 pixels spaced by 50 pixels
import colorgram
import turtle as t
import random 


def make_dot(turtle, rbg_as_tuples):
    turtle.pendown()
    turtle.dot(20, random.choice(rbg_as_tuples))
    turtle.penup()
    turtle.forward(50)


# allows use of RGB values for colors
t.colormode(255)


colors = colorgram.extract('image.jpg', 30)
rbg_as_tuples = []
# to get colors as tuple list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rbg_as_tuples.append((r, g, b))

# build timmy
timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed(0)
timmy.pensize(3)
# set start position
timmy.penup()
ypos = -200

# for each row
for i in range(10):
    timmy.goto(-250, ypos)
    # make row of dots
    for _ in range(10):
        make_dot(timmy, rbg_as_tuples)
    # set y position for next row
    ypos += 50


# build screen
screen = t.Screen()
screen.exitonclick()



# # their solution
# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

# screen = turtle_module.Screen()
# screen.exitonclick()