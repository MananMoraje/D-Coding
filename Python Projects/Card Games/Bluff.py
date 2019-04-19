import random
import time

CF = []
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
royals = ['Jack', 'Queen', 'King', 'Ace']
deck = []
played = []
passed = []

name = input('What is your name?    ')


class CreateDeck:

    for i in range(2, 11):
        CF.append(str(i))
    for j in range(4):
        CF.append(royals[j])

    for k in range(4):
        for l in range(13):
            cards = (CF[l] + ' of ' + suits[k])
            deck.append(cards)
    random.shuffle(deck)


pcards = []
i = 0
while i < int(len(deck) // 2):
    pcards.append(deck[i])
    deck.pop(i)
    i += 1

cpucards = deck


def canplay(card, first):
    j = len(played)
    i = 0
    while i != j:
        if suits[i] in card != suits[i] in first:
            print('You cannot play that card')
        else:
            print('         ')
        i += 1


def game():

    class Player:
        print('Your cards are: ', pcards)
        print('To play a card, type \'a card\' ')
        print('To call a bluff, type \'call\' or \'bluff\' ')
        print('To pass, type \'pass\' ')
        act = input('What would you like to play?   ')
        if act == 'a card':
            card = input('Which one?    ')
            print('If you want to bluff, enter a different cards name in the following question.')
            time.sleep(1.2)
            bluff = input('What would you like the computer to see?     ')
            if played:
                canplay(bluff, played[0])
            played.append(bluff)
            pcards.remove(bluff)
        elif act == 'call' or 'bluff':
            if played:
                print(name + ' calls a bluff! ')
                print('The last card played was ' + played[len(played)])
        elif act == 'pass':
            print(name + 'passes')
            i = 0
            while i < len(played):
                passed.append(played[i])
                played.pop(i)
                i += 1

    class CPU:
        play = random.randint(1, 20)
        num = random.randint(0, len(cpucards))
        bnum = random.randint(0, len(cpucards))
        card = cpucards[num]
        bluff = cpucards[bnum]
        if played:
            if play == 1 or 2 or 3 or 4 or 5 or 6 or 7:
                print('Al has played ' + str(card))
                if played:
                    canplay(card, played[0])
                played.append(card)
                cpucards.pop(num)
            if play == 8 or 9 or 10 or 11 or 12 or 13:
                print('Al has played ' + str(bluff))
                if played:
                    canplay(bluff, played[0])
                played.append(bluff)
                cpucards.pop(num)
                print(card)
            elif play == 14 or 15 or 16 or 17 or 18:
                print('Al is calling a bluff')
                print('The card was ' + played[len(played)])
            else:
                print('Al has passed')
                i = 0
                while i < len(played):
                    passed.append(played[i])
                    played.pop(i)
                    i += 1
        else:
            print('Al has played ' + str(card))
            if played:
                canplay(card, played[0])
            played.append(card)
            cpucards.pop(num)
        time.sleep(2)


while len(pcards) and len(cpucards) != 0:
    game()
