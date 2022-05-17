# functions w outputs of our own

# vid99, 100
def format_name(first_name, last_name):
    """
    Returns a full name, neatly formatted.
    """
    if first_name == '':
        return "Missing first name!"
    elif last_name == '':
        return "Missing last name!"
    return f"{first_name.title()} {last_name.title()}"

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(format_name(first_name, last_name))
print(format_name(input("Enter your first name: "),
        input("Enter your last name: ")))

