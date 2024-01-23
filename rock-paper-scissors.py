# Day 4 exercise of creatng a simple game of rock, paper, scissors

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

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors"))

game_images = [rock,paper,scissors]
if input > 2:
  print("That number is invalid. You lose!")
else:
  print(f"You chose: {game_images[input]}")
  
computer_answer = random.randint(0,2)

print(f"Computer chose: {game_images[computer_answer]}")

if computer_answer == input:
  print("It is a draw")
elif (computer_answer == 0 and input == 1) or (computer_answer == 1 and input == 2) or (computer_answer == 2 and input == 0):
  print("You win")
else:
  print("You lose")
