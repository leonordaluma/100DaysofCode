with open("./Input/Letters/starting_letter.docx") as letter:
    message = letter.read()

with open("./Input/Names/invited_names.txt", "r") as name:
    names = name.readlines()

for n in names:
    x = n.strip()
    letter = message.replace("[name]", x)
    with open(f"./Output/ReadyToSend/letter_for_{x}.docx", "w") as final_letter:
        final_letter.write(letter)

# print(letter)