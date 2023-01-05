#Step 1:
#Create a deal_card() that uses a list

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of card and return the score calculated from the cards"""

    #Step 4:
    #Inside calculate_score() check for a black jack (a hand with only 2 cards: ace + 10) and return 0 instard if the actual score. 0 will represent a Blackjack in our game.
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Step 5:
    #Inside calculate_score, check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)



#Step 2:
#deal the user and computer 2 cards each using deal_cards()

def compare(user_score, computer_score):
    """This is a function that compare the user score against the computer score"""
    if user_score == computer_score:
        return "Draw 🤗"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win, with a Blackjack 😎"
    elif user_score > 21:
        return "You went over, You Lose! 😱"
    elif computer_score > 21:
        return "Opponent went over, you win 🏆"
    elif user_score > computer_score:
        return " You win! 🏆"
    else:
        return "You Lose! 😱"

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Your final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))

#Step 3:
#Create a function called calculate_score() that takes a list of card as input and returns the score after calculation.

