from menu import MENU, resources
from math import ceil
# def check_resources(coffee_type):
#    resources["water"] -= 

def change(coins_inserted, coins_needed):
   if coins_inserted == coins_needed:
      return 0
   elif coins_inserted > coins_needed:
      coin_change = coins_inserted - coins_needed
      return round(coin_change, 2)
   else:
      return "You don't have enough money."

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
   total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
   coins_inserted = round(total_coins, 2)
   print(coins_inserted)
   if order == "espresso":
      water_level -= 50
      coffee_level-= 18
      print(change(coins_inserted, 1.5))
   elif order == "latte":
      water_level -= 200
      milk_level -= 150
      coffee_level -= 24
   elif order == "cappucino":
      water_level -= 250
      coffee_level -= 100
   print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money} ")

   amount = 0
   
