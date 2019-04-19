# Blackjack
from typing import *
from random import *
# Dealers cards
DC = []
# Players Cards
PC = []
# Deck

# Deal DC


while len(DC) != 2:
    DC.append(randint(1, 11))
    if len(DC) == 2:
        print('Dealer has: ' + str(DC[1]) + ' & HIDDEN')
# Deal PC
while len(PC) != 2:
    PC.append(randint(1, 11))
    if len(PC) == 2:
        print('You have: ', PC[0], ' and ', PC[1])
# Sum of DC
if int(sum(DC)) == 21:
    print('The dealer has a sum of 21, he has won!')
    input('Press ENTER when you have finished.')
elif sum(DC) > 21:
    print('The dealer has a sum of ', str(sum(DC)), ' and has gone bust. You won!')
    input('Press ENTER when you have finished.')
SH = randint(1, 2)

if SH == 1:
    print('The dealer has hit. His total is now: ' + str(sum(DC)))
    DC.append(randint(1, 11))
else:
    print('The dealer has stayed')
    print('His total is: ' + str(sum(DC)))

# Sum of PC
if not (sum(DC) == 21 or not (sum(DC) < 21)):
    while sum(PC) < 21:
        AT = str(input('Do you want to stay or hit?     '))
        if AT == 'hit' or AT == 'HIT' or AT == 'Hit':
            PC.append(randint(1, 11))
            print('You now have a total of ' + str(sum(PC)) + ' from these cards ', PC)
            if sum(DC) < sum(PC) <= 21:
                print('You win!')
                print('You have a sum of: ', str(sum(PC)), ' with ', PC)
                print('The dealer has a sum of: ' + str(sum(DC)) + ' with ', DC)
                input('Press ENTER when you have finished.')
            elif sum(PC) < sum(DC) <= 21:
                print('Dealer wins.')
                print('You have a sum of: ', str(sum(PC)), ' with ', PC)
                print('The dealer has a sum of: ' + str(sum(DC)) + ' with ', DC)
                input('Press ENTER when you have finished.')

        elif AT == 'stay' or AT == 'Stay' or AT == 'STAY':
            print('Dealer has a total of ' + str(sum(DC)) + ' with ', DC)
            print('You have a total of ' + str(sum(PC)) + ' with ', PC)
            if sum(DC) < sum(PC) <= 21:
                print('You win!')
                print('You have a sum of: ', str(sum(PC)), ' with ', PC)
                input('Press ENTER when you have finished.')
            elif sum(PC) < sum(DC) <= 21:
                print('Dealer wins.')
                print('The dealer has a sum of: ' + str(sum(DC)) + ' with ' , DC)
                input('Press ENTER when you have finished.')
        else:
            print(AT + ' was not an option')
        break
else:
    print('You have won!')
    input('Press ENTER when you have finished.')
if sum(PC) == 21:
    print('You won')
    input('Press ENTER when you have finished.')

if 21 < sum(PC):
        print('Your sum is now over 21 with ' + str(sum(PC)) + '. Your numbers are: ' , PC)
        print('Hence, you have gone bust.')
        print('The dealer has won!')
        print('The dealer has a sum of: ' + str(sum(DC)) + ' with ', DC)
if sum(PC) == sum(DC):
    print('A tie it is...')
    print('The dealer has a sum of: ' + str(sum(DC)) + ' with ', DC)
    print('You have a sum of: ', str(sum(PC)), ' with ', PC)
input('Press ENTER when you have finished.')
