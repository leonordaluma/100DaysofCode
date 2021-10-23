import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(type(alphabets))

nato_alphabets_dict = {row.letter: row.code for (index, row) in alphabets.iterrows()}
print(nato_alphabets_dict)