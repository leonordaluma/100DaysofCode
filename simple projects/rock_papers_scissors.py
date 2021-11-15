import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
print(images[player_input])

computer = random.randint(0, 2)
print("Computer chose:")
print(images[computer])
if player_input == computer:
    print("Tie.")
elif (player_input == 1 and computer == 0) or (player_input == 2 and computer == 1) or (player_input == 0 and computer == 2):
    print("You win.")
elif (player_input == 0 and computer == 1) or (player_input == 1 and computer == 2) or (player_input == 2 and computer == 0):
    print("You lose.")
else:
    print("You must choose 0, 1 or 2")