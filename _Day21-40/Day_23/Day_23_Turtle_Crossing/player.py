import turtle as t

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = 0, y = -270)
        self.shape("turtle")
        self.color("darkgreen")
        self.setheading(90)
        self.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
        self.speed(0)
        self.dx = 18
        self.dy = 18
        self.lives = 3


    def go_left(self):
        if self.heading() != 180:
            self.setheading(180)
        self.forward(self.dx)


    def go_right(self):
        if self.heading() != 0:
            self.setheading(0)
        self.forward(self.dx)


    def go_up(self):
        if self.heading() != 90:
            self.setheading(90)
        self.forward(self.dy)
        

    def go_down(self):
        if self.heading() != 270:
            self.setheading(270)
        self.forward(self.dy)

    def respawn(self):
        self.goto(x = 0, y = -270)
