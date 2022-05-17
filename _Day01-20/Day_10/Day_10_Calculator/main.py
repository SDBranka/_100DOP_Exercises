#Calculator program
from art import logo

# add
def add(x, y):
    return x + y
# subtract
def subtract(x, y): 
    return x - y
# multiply
def multiply(x, y):
    return x * y
# divide
def divide(x, y):
    return x / y

# create a dictionary named opearations that uses the
# keys "+", "-", "*", and "/" to correspond to the functions
operations = {"+": add, "-": subtract,
                "*": multiply, "/": divide}


def calculator():
    print(logo)
    print("\nWelcome to the calculator!")
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    operator = input(f"Select an operator from the above: ")
    num2 = float(input("Enter second number: "))

    first_answer = operations[operator](num1, num2)

    print(f"{num1} {operator} {num2} = {first_answer}")

    # determine if the user wants to continue
    total = first_answer
    calc_continue = input("Do you want to continue? (y/n): ")
    while calc_continue == "y":
        num_running = total
        operator = input(f"Select another operator: ")
        num3 = float(input("Enter a number: "))
        total = operations[operator](num_running, num3)

        print(f"{num_running} {operator} {num3} = {total}")  

        calc_continue = input("Do you want to continue? (y/n): ")
    print(f"\nYour final answer is {total}")



calculator()


