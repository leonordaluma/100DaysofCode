from art import logo
import random
import art, os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
player_cards = []
computer_cards = []
card_owners = {
    "p_card" : player_cards,
    "c_card" : computer_cards
}
def random_cards():
    card = random.choice(cards)
    return card

def add_cards(p_card, c_card):
    player_cards.append(p_card)
    computer_cards.append(c_card)

def score(card_owner):
    card_owner_array = card_owners[card_owner]
    sum = 0
    for n in card_owner_array:
        sum += n
    return sum

def display_cards():
    print(logo[0])
    player_score = score("p_card")
    computer_score = score("c_card")
    print(f"Your cards: {player_cards}, current score: {player_score} ")
    print(f"Computer's first card: {computer_cards} score: {computer_score} ")


def blackjack():    
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == 'y':
        for n in range(2):
            p_card = random_cards()
            c_card = random_cards()
            add_cards(p_card, c_card)
        display_cards()

    get_another_card = True

    while get_another_card:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if add_card == 'y':
            clearConsole()
            np_card = random_cards()
            nc_card = random_cards()
            add_cards(np_card, nc_card)
            display_cards()
        else:
            player_score = score("p_card")
            computer_score = score("c_card")

            get_another_card = False


blackjack()