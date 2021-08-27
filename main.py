print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill += 5
        print("Pay $5.")
    elif age <= 18:
        bill += 7
        print("Pay $7.")
    elif age <= 55 and age >= 45:
        print("You have a free ride.")
    else:
        print("Pay $12.")
    
    photo = input("Do you want a photo? Y or N. ")
    if photo == "Y":
        bill += 3

    print(f"Your total bill is {bill}")    
else:
    print("Sorry!")