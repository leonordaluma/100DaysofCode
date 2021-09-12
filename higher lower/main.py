from art import logo, vs
from game_data import data
from random import choice

def name_generator():
    name = choice(data)
    return name

def compare_follower_count(a_followers,b_followers):
    result = max(a_followers, b_followers)
    if result == a_followers:
        return 'A'
    elif result == b_followers:
        return 'B'

def fetch_data():
    data = name_generator()
    # name = data["name"]
    # follower_count = data["follower_count"]
    # description = data["description"]
    # country = data["country"]
    
    


a = {}
b = {}
player_score = 0

print(logo)
a = name_generator()
name = a["name"]
follower_count = a["follower_count"]
description = a["description"]
country = a["country"]
print(f"Compare A: {name}, a(n) {description}, from {country}.")

print(vs)
b = name_generator()
name2 = b["name"]
follower_count2 = b["follower_count"]
description2 = b["description"]
country2 = b["country"]
print(f"Against B: {name2}, a(n) {description2}, from {country2}. ")
higher = compare_follower_count(a_followers = follower_count, b_followers = follower_count2)
answer = input("Who has more followers? Type 'A' or 'B': ").upper()

if answer == higher:
    player_score += 1
    print(player_score)
else:
    print("Game Over!")

