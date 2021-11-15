from menu import MENU, resources

water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]
money = 0

def is_resources_sufficient(coffee):
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

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money} ")
    else:
        coffee = MENU[order]

        if is_resources_sufficient(coffee) is True:
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
            coins_inserted = round(total_coins, 2)
            coins_needed = coffee["cost"]
            if coins_inserted < coins_needed:
                print("Sorry that's not enough money. Money refunded.")
            else:
                coin_change = coins_inserted - coins_needed
                rounded_change = round(coin_change, 2)
                if rounded_change !=0:
                    print(f"Here is ${rounded_change} in change.")
                if order == "espresso":
                    water_level -= 50
                    coffee_level-= 18
                elif order == "latte":
                    water_level -= 200
                    milk_level -= 150
                    coffee_level -= 24
                elif order == "cappucino":
                    water_level -= 250
                    coffee_level -= 100

                money += coins_needed        
                print(f"Here is your {order} Enjoy!")
        else:
            print(is_resources_sufficient(coffee))

    
        

    
