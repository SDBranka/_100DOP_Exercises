import turtle as t


COLORS = [
    "red", "orange", "yellow", "green",
    "blue", "indigo", "violet", "black"
]

def draw_shape(turtle, length, color, num_sides):
    turtle.color(color)
    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(360/num_sides)


# build tim
tim = t.Turtle()
tim.shape("turtle")
tim.speed(3)
tim.penup()
tim.goto(-50, 100)
tim.pendown()
print(tim.position())

# draw triangle, square, pentagon, hexagon,
# heptagon, octagon, nonagon, and decagon
for i in range(3, 11):
    draw_shape(tim, 100, COLORS[i-3], i)

screen = t.Screen()
screen.exitonclick()