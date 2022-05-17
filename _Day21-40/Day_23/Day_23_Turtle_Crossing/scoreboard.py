import turtle as t  

class Scoreboard(t.Turtle):
    def __init__(self, message, x):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x = x, y = 260)
        self.score = 0
        self.font = ("Arial", 20, "normal")
        self.write(message, align = "center", font = self.font)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align = "center", font = self.font)


    def update_lives(self, lives):
        self.clear()
        self.write(f"Lives: {lives}", align = "center", font = self.font)


    def game_over(self, winner):
        self.goto(0, 0)
        self.color("black")
        self.write(f"      Game Over\nYour Final Score is: {self.score}",
                    align = "center", font = self.font)