import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# set user and computer choices
shoot = [rock, paper, scissors]
valid_choices = ["0", "1", "2"]

user_choice = input("Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")

# this also catches any non-number characters.
if user_choice not in valid_choices:
    # if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid character. Please try again.")
else:
    user_choice = int(user_choice)
    print(shoot[user_choice])
    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(shoot[comp_choice])

    if comp_choice == user_choice:
        print("It's a DRAW!")
    elif user_choice == 0 and comp_choice == 2:
        print("You WIN!")
    elif comp_choice == 0 and user_choice == 2:
        print("You LOSE!")
    elif comp_choice > user_choice:
        print("You LOSE!")
    elif user_choice > comp_choice:
        print("You WIN!")
