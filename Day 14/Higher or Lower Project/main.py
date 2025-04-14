import random
from game_data import data
from art import logo, vs

def guess_an_item():
    guess_index=random.randint(0,len(data))
    guess=data[guess_index]
    return guess

def print_guess(guess):
    return f"{guess["name"]}, a {guess["description"]}, from {guess["country"]}"

def higher_or_lower():
    score=0
    should_continue=True
    guess_a=guess_an_item()
    print(logo)
    while should_continue:

        print("Compare A : "+print_guess(guess_a))
        print(vs)
        guess_b=guess_an_item()
        print(f"Against B : "+print_guess(guess_b))
        #we display both the competitors and get the user to decide one of them
        user_choice=input("Who has more followers A or B :").upper()
        print("\n" * 20)
        if user_choice=="A" and guess_a['follower_count']>guess_b['follower_count']:
            #if user choice is A and A has more followers increase the score
            score+=1
            print(logo)
            print( f"You are right. Your score is {score}")
        elif user_choice=="B" and guess_b['follower_count']>guess_a['follower_count']:
            #if user choice is B and B has more followers increase the score
            score+=1
            print(logo)
            print( f"You are right. Your score is {score}")
        else:
            # for any other condition you lose
            print(logo)
            print(f"You lose. Your current score is {score}")
            should_continue=False
          #break the loop
        guess_a = guess_b
higher_or_lower()