from art import logo, vs
from game_data import data
from random import choice

def name_generator():
    name = choice(data)
    return name

def compare_follower_count(a_followers,b_followers):
    return max(a_followers, b_followers)

def fetch_data(empty_dict):
    empty_dict = name_generator()
    


a = {}
b = {}

print(logo)
is_wrong = False
while is_wrong:
    a = name_generator()
    name = a["name"]
    follower_count = a["follower_count"]
    description = a["description"]
    country = a["country"]
    print(f"Compare A: {name}, a(n) {description}, from {country}.")

    print(vs)
    b = name_generator()
    name = b["name"]
    follower_count = b["follower_count"]
    description = b["description"]
    country = b["country"]
    print(f"Against B: {name}, a(n) {description}, from {country}. ")
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    print(answer)

