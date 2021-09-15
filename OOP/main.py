from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


coffee_menu = Menu()
coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()
is_on = True
while is_on:
    order = input(f"What would you like? ({coffee_menu.get_items()}): " )
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_machine.report()
        cash_register.report()
    else:
        drink = coffee_menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink):
            payment = cash_register.process_coins()
            if cash_register.make_payment(cost):
                coffee_machine.make_coffee(drink)