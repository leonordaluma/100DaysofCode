from art import logo
import random

print(logo[0])
number = random.randint(1, 100)
print("Welcome to the number guessing game! \n" + "I'm thinking of a number from 1 to 100.")
print(f"The correct answer is {number}")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if choice == "easy":
    attempts = 10
elif choice == "hard":
    attempts = 5

is_game_continue = True
while is_game_continue:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        is_game_continue = False
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    print("Guess again.")
    attempts -= 1

    if attempts == 0:
        print("Game over! You ran out of life.")
        is_game_continue = False
