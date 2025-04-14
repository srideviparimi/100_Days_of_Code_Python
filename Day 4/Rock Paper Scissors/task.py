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
moves=[rock,paper,scissors]
index=input("Enter your move 0 for rock, 1 for paper or 2 for scissors")
your_move=moves[int(index)]

computer_move=random.choice(moves)

print(your_move)
print("Computer choice: \n")
print(computer_move)


if (your_move==computer_move):
    print("It is a draw")
elif your_move=="rock" and computer_move=="scissors":
    print("You win")
elif your_move=="scissors" and computer_move=="paper":
    print("You win")
elif your_move=="paper" and computer_move=="rock":
    print("You win")
else:
    print("You lose and Computer won")

