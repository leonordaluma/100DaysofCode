from art import logo
import random
import art, os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
players = {
    {
        "card_holder" : human
    }
}