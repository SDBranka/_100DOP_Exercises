# Modify the add function to take an unlimited 
# number of arguments.
# use a loop to sum all the arguments inside 
# the function
# Test it out by calling add() to calculate the 
# sum of some arguments


def add(*args):
    # print(args) # prints all args as a tuple
    # print(type(args)) # prints "tuple"
    sum = 0
    for n in args:
        sum += n
    return sum


# print(f"1: {add(1, 2, 3)}")     # 6
# print(f"2: {add(1, 2, 3, 4, 5)}")      # 15
# print(f"3: {add(1, 2, 3, 4, 5, 6, 7)}")     # 28


def calculate0(**kwargs):
    # print(kwargs) # prints all kwargs as a dictionary
    # print(type(kwargs)) # prints "dictionary"
    # access keys and values in kwargs
    for key, value in kwargs.items():
        print(f"key: {key} | value: {value}")
    print(kwargs["add"])    # prints 3


# calculate0(add = 3, multiply = 5)


def calculate1(n, **kwargs):
    # print(kwargs) # prints all kwargs as a dictionary
    n += kwargs["add"]
    print(f"n: {n}")    # prints 5
    n *= kwargs["multiply"]
    print(f"n: {n}")    # prints 25


# calculate1(2, add = 3, multiply = 5)  


class Car0:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car0 = Car0(make = "Nissan", model = "GT-8")
# print(my_car0.model)     # prints  "GT-8"

# my_car1 = Car0(make = "Nissan")
# print(my_car1.model)     # will crash



# using .get() 
class Car1:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car2 = Car1(make = "Nissan", model = "GT-8")
# print(my_car2.model)     # prints  "GT-8"

my_car3 = Car1(make = "Nissan")
# print(my_car3.model)     # prints "None" but does not error

















