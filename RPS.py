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
import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

rps = [rock,paper,scissors]
user_input_int = int(user_input)
print(rps[user_input_int])
print("Computer Chose:")
rando = random.randint(0,2)

cpu_input = rps[rando]
print(cpu_input)


if user_input_int == 0 and rando == 1:
  print("You lose.")
elif user_input_int == 1 and rando == 0:
  print("You win.")
elif user_input_int == 1 and rando == 2:
  print("You lose.")
elif user_input_int == 2 and rando == 1:
  print("You win.")
elif user_input_int == 0 and rando == 2:
  print("You win.")
elif user_input_int == 2 and rando == 0:
  print("You lose.")
else:
  print("Tie!")