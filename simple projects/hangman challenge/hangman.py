import random
import hangman_art
import hangman_words

print(hangman_art.logo[0])


chosen_word = random.choice(hangman_words.word_list)
display = []
for letter in chosen_word:
    display += "_"
print(chosen_word)

lives = 6
end_of_game = False
occurance = ""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess == occurance:
        print(f"{guess} is already guessed. \n")
    # or 
    # if guess in display:
    #     print(f"{guess} is already guessed. \n")
    
    for letter in range(0, len(chosen_word)):
      if guess == chosen_word[letter]:
        display[letter] = guess
        occurance = guess

    print(f"{' '.join(display)}")



    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not the word. You lose a life.")
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")

