import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("forestgreen")
# build screen
screen = t.Screen()

def move_forward():
    tim.forward(10)



screen.listen()
screen.onkey(key = "space", fun = move_forward)



screen.exitonclick()