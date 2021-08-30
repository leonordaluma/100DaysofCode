import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ").lower()

for letter in range(0, len(chosen_word)):
    if guess == chosen_word[letter]:
        print("Right")
    else:
        print("Wrong")


