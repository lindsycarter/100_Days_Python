from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Print Reports
# 1.a - Create objects from classes in coffee_maker.py and money_machine.py
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

# Create variable to "turn on" the machine
machine_on = True

# 1.b - Print reports
# moved to the while function below
# coffee_maker.report()
# money_machine.report()

# Set up machine functions

while machine_on:
    options = menu.get_items()
    usr_choice = input(f"Which coffee would you like? ({options})")
    # There are 3 choices when the machine is turned on
    # 1. Type in "off" to turn the machine off
    if usr_choice == "off":
        machine_on = False
    # 2. Type in "report" to run reports
    elif usr_choice == "report":
        coffee_maker.report()
        money_machine.report()
    # 3. Check for enough resources to make a coffee
    else:
        # From the menu OBJECT, using the find drink METHOD, add the drink VARIABLE the user entered
        drink = menu.find_drink(usr_choice)

        # Check if sufficient resources
        # AND
        # Process coins
        # using money_machine object, use the make payment method and pass in cost of users drink
        # Check if transaction is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # check if coffee maker object method of is resource sufficient and pass in the drink variable
            # Make coffee
            coffee_maker.make_coffee(drink)
