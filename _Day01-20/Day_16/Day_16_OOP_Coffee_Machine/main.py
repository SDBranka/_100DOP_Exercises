from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def user_choose():
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino):")
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

# check resources sufficient

# process coins

# check transaction successful

# make coffee


# print(current_menu.get_items())

# access latte
# print(current_menu.find_drink("latte"))
# print(current_menu.find_drink("latte").ingredients)
# print(current_menu.find_drink("latte").ingredients["milk"])

def coffee_machine_run():
    user_choice = ""
    # user makes selection
    while user_choice != "report" and user_choice != "espresso" and user_choice != "latte" and user_choice != "cappuccino":
        user_choice = user_choose()
        print(f"You have selected: {user_choice}")

    # perform selection
    if user_choice == "report":
    # print report
        coffee_machine.report()
        cash_machine.report()
    # make a drink
    else:
        if coffee_machine.is_resource_sufficient(current_menu.find_drink(user_choice)):
            # print("sufficient resources")        
            if cash_machine.make_payment(current_menu.find_drink(user_choice).cost):
                # print("You have inserted enough money.")
                coffee_machine.make_coffee(current_menu.find_drink(user_choice))

# create objects
current_menu = Menu()
cash_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

machine_on = True
while machine_on:
    coffee_machine_run()
    user_choice = input("\nWould you like to make another order? (y/n) ")
    user_choice = user_choice.lower()
    if user_choice != "y":
        machine_on = False