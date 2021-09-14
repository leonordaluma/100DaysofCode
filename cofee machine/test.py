from menu import MENU, resources

water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
money = 0
def is_resources_sufficient(order):
    coffee = MENU[order]
    ingredients = coffee["ingredients"]
    if order == "latte":
        if milk_level >= ingredients["milk"]:
            return True
        else:
            return "Sorry there is not enough milk."
    if water_level >= ingredients["water"]:
        if coffee_level >= ingredients["coffee"]:
            return True
        else:
            return "Sorry there is not enough coffee."
    else:
        return "Sorry there is not enough water."

order = input("What would you like? (espresso/latte/cappuccino): ").lower()
if order == "report":
   print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money} ")
else:
    if is_resources_sufficient(order) is True:
        print("Please insert coins.")

    else:
        print(is_resources_sufficient(order))
    

    
