# Create a script that rolls dice for a user.
# When the script runs, it should ask a user how many dice they
# want to roll and how many sides each die will have.
# Then it randomly rolls those dice and prints the result.
# Every time a user hits Enter, the dice are rolled again.
# If a user every enter “q”, then the script quits and stops running!

# Bonus: Ensure that a user enters a valid integer between 1 and 20
# and keep prompting a user until they do!
import random

# ask for how many dice you want to roll
dice = input("How many dice are we rolling? ( 1 and 20): ")
while not dice.isdigit() or not (int(dice) >= 1 and int(dice) <= 20):
    dice = input("How many dice are we rolling? ( 1 and 20): ")

dice = int(dice)
# ask for sides of the dice
dice_sides = int(input('How many sides on each die? '))

# roll the dices(s) randomly and print result - |5|1|4|
q = ''
while q != 'q':
    result = '|'
    for d in range(1, dice+1):
        rand = random.randint(1, dice_sides)
        result += f'{rand}|'

    print(result)
    q = input("Roll again? ('q' to quit): ")
    # end while
# prompt for more rolling

# Quit if response is q
