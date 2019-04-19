# Guess the cards- 1/52
import random
import time

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
lo = 0


def logic(array, num, lo):

    g = 0
    while g < len(royals):
        h = royals[g]
        if h in array[num]:
            lo -= 1
            print(str(lo))
        g += 1
    if '2' or '3' or '4' or '5' or '6' in array[num]:
        lo += 1
        print(str(lo))
    elif '7' or '8' or '9' or '10' in array[num]:
        lo += 0
        print(str(lo))


for i in range(len(deck)):
    time.sleep(0.5)
    print(deck[i])
    logic(deck, i, lo)
    i += 1
print(str(lo))
