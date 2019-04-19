# Guess the cards- 1/52
import random

CF = []
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
royals = ['Jack', 'Queen', 'King', 'Ace']
deck = []

for i in range(2, 11):
    CF.append(str(i))
for j in range(4):
    CF.append(royals[j])

for k in range(4):
    for l in range(13):
        cards = (CF[l] + ' of ' + suits[k])
        deck.append(cards)
random.shuffle(deck)
print(deck[random.randint(0, len(deck))])