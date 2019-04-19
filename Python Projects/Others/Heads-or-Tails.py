import random
print('For INTERACTIVE type \'i\' and for UN-INTERACTIVE type \'u\'. Thank you.' )
t = input('Would you like interactive or un-interactive?    ' )

def Unint():
    hl = random.randint(0, 1)

    if hl == 1:
        print('HEADS')
    else:
        print('TAILS')

def Inter():
    h = input('Heads or Tails?  ')
    hol = random.randint(0,1)

    if hol == 1:
        print('HEADS' + str(hol))
    elif hol == 0:
        print('TAILS' + str(hol))
    if h == 'heads' or 'Heads' or 'HEADS' and hol == 1:
        print('You won!')
    elif  h == 'tails' or 'Tails' or 'TAILS' and hol == 0:
        print('You won')
    elif h != hol:
        print('You lost')
    if h != 'heads' or 'Heads' or 'HEADS' or 'tails' or 'Tails' or 'TAILS':
        print('Invalid option...')

if t == 'i':
    Inter()
elif t == 'u':
    Unint()
else:
    print('That was an invalid option. Please check the top of the output screen to see your options.')