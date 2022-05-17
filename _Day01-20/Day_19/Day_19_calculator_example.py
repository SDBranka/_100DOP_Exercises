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

def calculator(n1, n2, func):
    return func(n1, n2)

result = calculator(2, 3, add)
print(result)