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

#Write your code below this line 👇
import random

user_entry = (input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
if user_entry is not int:
    print("\033[31mYou must only provide a number between 0 and 2. No other input will be accepted.")
else:
    users_choice = int(user_entry)
    outcomes = [rock, paper, scissors]
    computer_choice = random.randint(0, 2)
    if users_choice <= 2 and users_choice > 0:
        if computer_choice == 0:
            print(outcomes[users_choice])
            if users_choice == 0:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nDraw!")
            elif users_choice == 1:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou win!")
            elif users_choice == 2:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou lose!")
        if computer_choice == 1:
            print(outcomes[users_choice])
            if users_choice == 0:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou lose!")
            elif users_choice == 1:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nDraw!")
            elif users_choice == 2:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou win!")
        if computer_choice == 2:
            print(outcomes[users_choice])
            if users_choice == 0:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou win!")
            elif users_choice == 1:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nYou lose!")
            elif users_choice == 2:
                print("Computer chose:\n")
                print(outcomes[computer_choice])
                print("\nDraw!")
    else:
        print("You've provided an invalid input. Exiting.")
