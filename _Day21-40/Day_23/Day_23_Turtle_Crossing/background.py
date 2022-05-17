import turtle as t

END_ZONE_START_X = 306
END_ZONE_START_Y = 171
START_ZONE_START_X = 306
START_ZONE_START_Y = -306


class Zone(t.Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("limegreen")
        self.setheading(180)
        self.position = position

    def draw_zone(self):
        self.penup()
        # determine zone position
        if self.position == "start":
            self.goto(START_ZONE_START_X, START_ZONE_START_Y)
        elif self.position == "end":
            self.goto(END_ZONE_START_X, END_ZONE_START_Y)
        self.pendown()
        self.begin_fill()
        self.forward(612)
        self.right(90)
        self.forward(135)
        self.right(90)
        self.forward(612)
        self.right(90)
        self.forward(135)
        self.end_fill()