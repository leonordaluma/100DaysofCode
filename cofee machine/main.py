from menu import MENU, resources
water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]

money = 0

order = input("What would you like? (espresso/latte/cappuccino): ").lower()
if order == "report":
   print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money} ")
else:
   print("Please insert coins.")
   quarters = float(input("How many quarters?: "))
   dimes = float(input("How many dimes?: "))
   nickels = float(input("How many nickels?: "))
   pennies = float(input("How many pennies?: "))
   coins_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
   print(coins_inserted)
