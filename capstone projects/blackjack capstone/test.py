from art import logo
import random
import art, os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10]
    user_cards = []
    computer_cards = []
    is_game_over = False

    def deal_card():
        random_card = random.choice(cards)
        return random_card

    def calculate_score(list_of_cards):
        if sum(list_of_cards) == 21 and len(list_of_cards):
            return 0
        elif 11 in list_of_cards and sum(list_of_cards) > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)

        return sum(list_of_cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "You lose. Opponent has blacjack."
        elif user_score == 0:
            return "You win. Blackjack!"
        elif user_score > 21:
            return "You went over. You lose."
        elif computer_score > 21:
            return "Opponent went over. You win."
        elif user_score > computer_score:
            return "You win."
        else:
            return "You lose."

    def display_score():
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_input == 'y':
        clearConsole()
        print(art.logo[0])
        for n in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        display_score()

        if computer_score == 0 or user_score == 0 or user_score > 21:
            display_score()
            is_game_over = True
        else:
            user_input2 = input("Type 'y' to get another card, type 'n' to pass.: ")
            if user_input2 == 'y':
                user_cards.append(deal_card())
            else:
                display_score()
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

blackjack()

user_input3 = input("Do you want to restart the game? Type 'n' if yes, type 'n' if no: ")
if user_input3 == 'y':
    clearConsole()
    blackjack()