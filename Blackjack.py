############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

def deal_card():
  return random.choice(cards)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(list):
  score = sum(list)
  if len(list) == 2 and score == 21:
    score = 0
    return score
  for i in range(0,len(list)):
    if list[i] == 11 and score > 21:
      list[i] = 1
  return score

def compare(us,cs):
  if us == cs:
    print("Draw!")
  elif cs == 0:
    print("Sorry, you lose! Opponent has BlackJack!")
  elif us > 21:
    print("Sorry, you went over!")
  elif us == 0:
    print("Winner with BlackJack!")
  elif cs > 21:
    print("Congrats, your opponent went over. You win by default!")
  else:
    if us > cs:
      print("Winner! Your score is greater!")
    else:
      print("Sorry, you lose! Opponent had highest score!")

user_cards = []
computer_cards = []

for i in range(0,2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

loop = True

utotal = calculate_score(user_cards)
ctotal = calculate_score(computer_cards)
print(f"  Your cards: {user_cards}, current score: {utotal}")
print(f"  Computer's first card: {computer_cards[0]}")

if utotal == 0 or ctotal == 0 or utotal > 21:
  loop = False
  compare(utotal,ctotal)

while ctotal != 0 and ctotal < 17:
  computer_cards.append(deal_card())
  ctotal = calculate_score(computer_cards)

while loop == True:
  cg = input("Would you like to draw another card? Type 'y' if so. Otherwise type 'n'. ").lower()
  if cg == "y":
    user_cards.append(deal_card())
    utotal = calculate_score(user_cards)
    print(f"  Your cards: {user_cards}, current score: {utotal}")
    print(f"  Computer's first card: {computer_cards[0]}")

  if cg == "n" or utotal == 0 or ctotal == 0 or utotal > 21:
    loop = False
    print(f"  Your final hand: {user_cards}, final score: {utotal}")
    print(f"  Computer's final hand: {computer_cards}, final score: {ctotal}")
    compare(utotal,ctotal)

