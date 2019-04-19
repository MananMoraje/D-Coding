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

print('When entering a royal, make sure that their names start with a capital letter. The same goes for the suits.')
user_in = input('What card will come up?    ')
ans = deck[random.randint(0, 52)]


if user_in == ans:
    print('The answer is: ' + ans)
    print('You won the jackpot!')
else:
    print('The answer is: ' + ans)
    print('You could win next time')
input('Press ENTER when you have finished.')
