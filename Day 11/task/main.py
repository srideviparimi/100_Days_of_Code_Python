import random
from art import logo
def deal_card():
    """ returns a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate(card_list):
    """takes a list and add the total of all the elements in the list and
    also checks if the score is black jack or replaces 11 with 1 if score is
     greater than 21"""
    score=sum(card_list)
    if score==21 and len(card_list)==2:
        return 0
    if score>21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif user_score==0:
        return "Use win"
    elif user_score>21:
        return "Computer win"
    elif computer_score>21:
        return "Opponent score exceeded 21 , so user win"
    elif user_score>computer_score:
        return "User win"
    else:
        return "You lose"
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_sum = -1
    user_sum = -1
    is_game_over = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(user_cards)
    print(computer_cards)

    while not is_game_over:
        user_sum = calculate(user_cards)
        computer_sum = calculate(computer_cards)
        if user_sum==0 or user_sum > 21 or computer_sum==0 :
            """if the user score =0 or computer score =0 or user_sum>21 game ends"""
            print("game over")
            is_game_over=True
        else:
            continue_game=input("Do you want to take another card y or n")
            if continue_game=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_sum!=0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum=calculate(computer_cards)

    print(compare(user_sum,computer_sum))

while input("Do you want to play a new game of BlackJack y or n")=="y":
    print("\n"*16)
    play_game()

