from art import logo, vs
from game_data import data
from random import choice

def select_person():
    person = choice(data)
    return person

def printable_format(person):
    name = person["name"]
    follower_count = person["follower_count"]
    description = person["description"]
    country = person["country"]
    

    


print(logo)
print(f"Compare A: {name}, a(n) {description}, from {country}.")
a = select_person()
b = select_person()

