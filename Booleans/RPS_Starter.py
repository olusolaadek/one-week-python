from random import randint
from unittest import result
# https://plum-poppy-0ea.notion.site/Rock-Paper-Scissors-Exercise-a695ef1e479e458a840d695130df8cd1
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)
comp_move = ''
computer_ascii = ''
# Turn that random number into the computer's RPS move
if num == 1:
    comp_move = 'rock'
    computer_ascii = rock
elif num == 2:
    comp_move = 'paper'
    computer_ascii = paper
elif num == 3:
    comp_move = 'scissors'
    computer_ascii = scissors

# Ask a user to enter their move
user_move = input('Please enter your move [rock, paper or scissors]: ')

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
user_ascii = ''
if user_move == 'rock':
    user_ascii = rock
elif user_move == 'paper':
    user_ascii = paper
elif user_move == 'scissors':
    user_ascii = scissors
else:
    print(f'Invalid user move - {user_move}. Please try again')
    exit()

print(f'User move - {user_move}', user_ascii)
# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f'Computer move - {comp_move}.', computer_ascii)
# Figure out who wins and print the result!
if user_move == comp_move:
    result = "it's a tie!"
elif user_move == 'rock' and comp_move == 'scissors':
    result = 'You win!'
elif user_move == 'scissors' and comp_move == 'rock':
    result = 'You lose!'
elif user_move == 'scissors' and comp_move == 'paper':
    result = 'You win!'
elif user_move == 'paper' and comp_move == 'scissors':
    result = 'You lose!'
elif user_move == 'paper' and comp_move == 'rock':
    result = 'You win!'
elif user_move == 'rock' and comp_move == 'paper':
    result = 'You lose!'

print(result)
