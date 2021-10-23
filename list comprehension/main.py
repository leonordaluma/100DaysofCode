import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(type(alphabets))

nato_alphabets_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}

user_input = input("Enter a word: ").upper()
# code_words = []
# for index in range(len(user_input)):
#     letter = user_input[index]
#     if letter in nato_alphabets_dict.keys():
#         code_words.append(nato_alphabets_dict[letter])
code_words = [nato_alphabets_dict[letter] for letter in user_input]

print(code_words)