# create a new scoreboard class that inherits from
# the turtle class. scoreboard will be a turtle that 
# knows how to keep track of the score and how to 
# display it in our program

import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        # set the high_score by reading 
        # the data.txt file
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}",
                    align = "center", 
                    font=("Arial", 24, "normal")
        )


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # save new high score to data.txt
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
