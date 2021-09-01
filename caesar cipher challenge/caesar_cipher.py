alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    new_text = ""
    cipher_text =""
    length = len(alphabet)
    for i in text:
        if i!=" ":
            new_text+=i
    for letter in new_text:
        position = alphabet.index(letter)
        if alphabet[position] == letter:
            key = position+shift
            cipher_text += alphabet[key]
    print(f"The encoded text is {cipher_text}")


        

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: "))
encrypt(text, shift)
