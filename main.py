print("welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
count = 10

names = name1 + name2
names = names.lower()

t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t + r + u + e
#count*= true

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l + o + v + e
#count+=love

count = true * 10 + love

if count < 10 or count > 90:
    print(f"Your score is {count}, you go like coke and mentos.")
elif count >=40 and count <= 50:
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}")