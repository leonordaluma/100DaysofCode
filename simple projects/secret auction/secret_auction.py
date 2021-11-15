import art, os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

bidders = {}
def secret_auction(name, bid):
    bidders[name] = bid


answer = 'yes'
print(art.logo[0])
print("Welcome to the secret auction program.")

while answer == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    secret_auction(name, bid)
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clearConsole()
    if answer == 'no':
        bid_amount = 0
        bid_person = ""
        for person in bidders:
            if bidders[person] > bid_amount:
                bid_amount = bidders[person]
                bid_person = person
        print(f"The winner is {bid_person} with a bid of ${bid_amount}")