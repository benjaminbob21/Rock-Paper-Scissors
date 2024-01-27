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

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
print("Computer chose:")
computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)
if (choice == 2 and computer_choice == 1) or (choice == 0 and computer_choice == 2) or (choice == 1  and computer_choice == 0):
  print("You win!")
elif not(0 <= choice <= 2):
  print("You typed an invalid number, you lose!")
elif choice == computer_choice:
  print("It's a draw!")
else:
  print("You lose!")