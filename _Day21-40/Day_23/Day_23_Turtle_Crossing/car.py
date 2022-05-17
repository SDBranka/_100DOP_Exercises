import random
import turtle as t


t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


class Car(t.Turtle):
    # def __init__(self, color):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = random.randint(310, 405), y = random.randint(-153, 153))
        self.shape("square")
        self.setheading(180)
        self.color(random_color())
        self.speed(0)
        self.shapesize(stretch_wid = 1.5, stretch_len = 2.7)
        self.dx = random.randint(1, 6)


    def move(self):
        self.forward(self.dx)

    # def move_cars(self, cars_list):
    #     for i, car in enumerate(cars_list):
    #         car.move()
    #         if car.xcor() < -333:
    #             cars_list.pop(i)
    #             new_car = Car()
    #             cars_list.append(new_car)

