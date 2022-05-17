from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# build screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# set tracer to 0 to enable using the update method
screen.tracer(0)

# create scoreboard
scoreboard = Scoreboard()
# create snake
snake = Snake()
# create food
food = Food()

# establish key listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# main game loop
game_is_on = True
while game_is_on:
    # print(scoreboard.message + str(scoreboard.score))
    screen.update()
    time.sleep(0.1)

    snake.move()

    # collision with food
    if snake.head.distance(food) < 20:
        # print("Snake ate the food")
        # food respawns to new location
        food.refresh()
        # snake grows
        snake.extend()
        # update scoreboard
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()