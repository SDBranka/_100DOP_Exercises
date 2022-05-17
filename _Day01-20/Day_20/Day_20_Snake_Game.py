import turtle as t

# build the screen
def build_screen():
    screen = t.Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    # set title bar
    screen.title("Snake Game")
    # turn off tracer to enable screen updates
    screen.tracer(0)
    return screen


# create snake body
def create_snake():
    # # create a list to store the snake body
    # snake_body = []
    # x_pos = 0

    # # create the snake body from three pieces
    # for _ in range(3):
    #     # build snake body piece
    #     snake = t.Turtle()
    #     snake.shape("square")
    #     snake.color("white")
    #     snake.penup()
    #     snake.speed(0)
    #     snake.goto(x = x_pos, y = 0)
    #     # set coordinates for next piece
    #     x_pos -= 20
    #     # add the snake body piece to snake body
    #     snake_body.append(snake)
    # return snake_body
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_body = []
    for position in starting_positions:
        snake = t.Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.speed("slowest")
        snake.goto(position)
        snake_body.append(snake)
    return snake_body

screen = build_screen()
snake = create_snake()


game_on = True
while game_on:
    # screen.update() 
    # move the snake 
    for snake_piece in snake:
        snake_piece.forward(20)
        screen.update() 

    
# create snake food
# detect collision with food
# create scoreboard
# detect collision with wall
# detect collision with tail




screen.exitonclick()