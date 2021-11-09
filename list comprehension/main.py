import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabets_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}
print(nato_alphabets_dict)

is_error = True
while is_error:
    try:
        user_input = input("Enter a word: ").upper()
        code_words = [nato_alphabets_dict[letter] for letter in user_input]
        print(code_words)
        is_error = False
    except KeyError:
        is_error = True
        print("Sorry, only letters in the alphabet please.")

# def generate_nato():
#     user_input = input("Enter a word: ").upper()
#     try:
#         code_words = [nato_alphabets_dict[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         generate_nato()
#     else:
#         print(code_words)

# generate_nato()
