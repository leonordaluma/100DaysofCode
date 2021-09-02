alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    new_text = ""
    plain_text = ""
    # concatanate the text to remove spaces
    for i in text:
        if i!=" ":
            new_text+=i
            
    for letter in new_text:
        position = alphabet.index(letter)
        if alphabet[position] == letter:
            if direction == "encode":
                key = position + shift
            elif direction == "decode":
                key = position - shift
        plain_text += alphabet[key]
    print(f"The {direction}d text is {plain_text}")        

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: "))
caesar(text = text, shift = shift, direction = direction)
