import random
from art import logo
print(logo)
print("Welcome to the number guessing game")
print ("Guess a number between 1 to 100")
attempts=0
def difficulty_level(attempts):
    level=input("Choose a difficulty level 'easy' or 'hard': ")
    if level=="easy":
        attempts=10
    else:
        attempts=5
    return attempts


attempts=difficulty_level(attempts)
print(f"You have {attempts} attempts to guess the number")
random_number=random.randint(1,100)
right_guess=False
while attempts>0:
    num=int(input("Make a guess: "))
    if random_number==num:
        print(f"You got it. The answer was {num}")
        right_guess=True
        break
    if random_number>num:
        attempts-=1
        print("Too low")
        print("guess again")
        print(f"You have {attempts} attempts to guess the number")
    else:
        attempts-=1
        print("Too high")
        print("guess again")
        print(f"You have {attempts} attempts to guess the number")

if right_guess==False:
    print("You run out of guesses.Refresh the page again to restart the game")
