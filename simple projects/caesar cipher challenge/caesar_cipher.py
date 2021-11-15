import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    plain_text = ""
    for letter in text:
        if letter not in alphabet:
            plain_text += letter
        else:
            position = alphabet.index(letter)
            if alphabet[position] == letter:
                if direction == "encode":
                    key = position + shift
                elif direction == "decode":
                    key = position - shift
            plain_text += alphabet[key]
        

    print(f"The {direction}d text is {plain_text}")        

answer = "yes"

while answer == "yes":
    print(art.logo[0])
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))
    print(shift)
    shift = shift % 25
    print(shift)
    caesar(text = text, shift = shift, direction = direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
