import random

stupids = ['Manil', 'Me']
i = 0
q = input('Who is stupid?   ')

while i != len(stupids):
    if q == stupids[i]:
        print('Correct')
    else:
        print('Wrong')
    i += 1


