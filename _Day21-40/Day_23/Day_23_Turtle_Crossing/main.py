import random
import time
import turtle as t
from car import Car
from background import Zone
from player import Player
from scoreboard import Scoreboard


NUM_OF_CARS = 7


t.colormode(255)


# build screen
screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing")
# eliminate animation and allow update method
screen.tracer(0)

# draw screen image
end_zone = Zone("end")
end_zone.draw_zone()
start_zone = Zone("start")
start_zone.draw_zone()

# create scoreboard
lives_scoreboard = Scoreboard("Lives: 3", -234)
points_scoreboard = Scoreboard("Score: 0", 225)

# create player
player = Player()
# create a list of cars
cars = [Car() for i in range(NUM_OF_CARS)]

# create listeners
screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")


# main game cycle
game_on = True
while game_on:

    screen.update()
    time.sleep(0.01)

    for i, car in enumerate(cars):
        car.move()
        # if car is out of screen, eliminate 
        #   it and create a new car
        if car.xcor() < -333:
            cars.pop(i)
            new_car = Car()
            cars.append(new_car)
        # check for collision with player
        if car.distance(player.xcor() + 10, player.ycor()) < 30:
            # print("Turtle hit car")
            player.lives -= 1
            if player.lives <= 0:
                points_scoreboard.game_over("Game Over")
                game_on = False
            else:
                player.respawn()
                lives_scoreboard.update_lives(player.lives)

        # check for player collision with end zone
        if player.ycor() > 163:
            points_scoreboard.update_score()
            player.respawn()


screen.exitonclick()