from art import logo, vs
from game_data import data
from random import choice

def name_generator():
    name = choice(data)
    return name
    
print(logo)
a = name_generator()
name = a["name"]
follower_count = a["follower_count"]
description = a["description"]
country = a["country"]
print(f"Compare A: {name}, a(n) {description}, from {country}.")

print(vs)
print("Against B: ")
answer = input("Who has more followers? Type 'A' or 'B': ").upper()
print(answer)
