from data import MENU, resources


# print report
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# checks if machine has enough resources to make the drink
def check_sufficient_resources(resources, recipe):
    for ingredient, quantity in recipe["ingredients"].items():
        if resources[ingredient] < quantity:
            print(f"Sorry, not enough {ingredient}!\n")
            return False
    return True


def user_choose():
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    user_choice = user_choice.lower()
    if user_choice == "e":
        user_choice = "espresso"
    elif user_choice == "l":
        user_choice = "latte"
    elif user_choice == "c":
        user_choice = "cappuccino"
    elif user_choice == "r":
        user_choice = "report"
    return user_choice


def coffee_machine():
    # user makes selection
    user_choice = ""
    while user_choice != "report" and user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino":
        user_choice = user_choose()
        print(f"You have selected: {user_choice}")

    # perform selection
    if user_choice == "report":
        report()
    # make a drink
    else:
        # check if machine has enough resources to make the drink
        if check_sufficient_resources(resources, MENU[user_choice]):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money = round((quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01), 2)
            print(f"You have inserted ${money}.")
            if money >= MENU[user_choice]["cost"]:
                print("You have inserted enough money.")
                # make drink
                for ingredient, quantity in MENU[user_choice]["ingredients"].items():
                    resources[ingredient] -= quantity
                # add money to resources
                resources["money"] += MENU[user_choice]["cost"]
                # make change
                change_returned = round(money - MENU[user_choice]["cost"], 2)
                print(f"Here is ${change_returned} in change.")
                print(f"Here is your ☕ {user_choice}☕. Enjoy!\n")
            else:
                print("Sorry, that's not enough money. Money refunded.\n")


transaction_successful = True
while transaction_successful:
    coffee_machine()
    transaction_successful = input("Would you like to make another transaction? (y/n): ")
    transaction_successful = transaction_successful.lower()
    if transaction_successful == "y":
        transaction_successful = True
    else:
        transaction_successful = False



