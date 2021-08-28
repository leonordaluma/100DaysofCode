import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

r_password = ""
for letter in range(0, nr_letters):
    random_letters = random.randint(0, len(letters) - 1)
    rl = letters[random_letters]
    r_password += str(rl)

for number in range(0, nr_numbers):
    random_numbers = random.randint(0, len(numbers) - 1)
    rn = numbers[random_numbers]
    r_password += str(rn)

for symbol in range(0, nr_symbols):
    random_symbols = random.randint(0, len(symbols) - 1)
    rs = symbols[random_symbols]
    r_password += str(rs)

random_order = random.sample(r_password, len(r_password))
password = ""
for r in random_order:
    password += r

print(f"EZ: {r_password}")
print(f"HARD: {password}")