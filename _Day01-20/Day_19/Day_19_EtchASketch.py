from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(3)

def turn_right():
    tim.right(3)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
# "w" = forward
screen.onkey(key="w", fun=move_forwards)
# "s" = backward
screen.onkey(key="s", fun=move_backwards)
# "a" = left
screen.onkey(key="a", fun=turn_left)
# "d" = right
screen.onkey(key="d", fun=turn_right)
# "c" = clear
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
