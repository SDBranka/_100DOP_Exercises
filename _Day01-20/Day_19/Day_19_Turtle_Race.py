import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green",
        "blue", "indigo", "purple"]

# build screen
screen = t.Screen()
screen.setup(width = 500, height = 400)
# have user enter a bet as to which turtle will win
user_bet = screen.textinput(title = "Make Your Bet", 
                    prompt = "Which turtle will win the race? Enter a color: "
)

# new_turtle = t.Turtle(shape = "turtle")
# new_turtle.goto(x = 225, y = 0)

y_pos = -150
turtles = []
for color in COLORS:
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x = -234, y = y_pos)
    turtles.append(new_turtle)
    y_pos += 50
# print(turtles)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 225:
            # winning_turtle = turtle.color()[0].title()
            winning_turtle = turtle.pencolor()
            print(f"{winning_turtle.title()} Wins!!!")
            if user_bet == winning_turtle:
                print("You win!")
            else:
                print("You lose!")
            race_on = False


screen.exitonclick()