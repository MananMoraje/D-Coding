# Guess The Number- 1/50
from random import *

i = input('Pick a number from 1 - 50 ')
sr = randint(0, 50)
print('My number was:')
print(sr)
if int(i) == sr:
    print('You won!')
else:
    s = input('You lost. Do you want to play again? ')
    if s == 'no' or s == 'NO' or s == 'No':
        print('Thank you for playing. We hope to see you soon! Good day.')
        input('Press ENTER when you have finished.')
    elif s == 'yes' or s == 'Yes' or s == 'YES':
        if s == 'yes' or s == 'YES' or s == 'Yes':

            ii = input('Pick a number from 1 - 50 ')
            srsr = randint(0, 50)
            print('My number was:')
            print(srsr)

            if ii == srsr:
                print('You won!')
            elif ii != srsr:
                print('You could win next time.')
            else:
                print('Thank you')
if int(i) == False or i.isalpha() == True:
    print('Invalid.')

input('Press ENTER when you have finished.')