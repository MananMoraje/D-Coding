import time


def convert():
    print('This will re-order your password')
    y = input('Your password? 13 letters, numbers & symbols:    ')
    j = y[0] + y[11] + y[10] + y[9] + y[8] + y[7] + y[6] + y[5] + y[4] + y[3] + y[2] + y[1] + y[12]
    print(j)


def original():
    print('This will re-order your password to its original state')
    z = input('Your muddled password? 13 letters, numbers & symbols:    ')
    t = z[0] + z[11] + z[10] + z[9] + z[8] + z[7] + z[6] + z[5] + z[4] + z[3] + z[2] + z[1] + z[12]
    print(t)


p = input('Convert or Convert to original? For \'Convert\', type \'c\' or \'C\' and for \'Convert to original\', type \'o\' or \'O\':    ')

if p == 'c' or 'C':
    convert()
elif p == 'o' or 'O':
    original()
else:
    print('Invalid')

#  Example Passwords:
#  6539HopePoop
#  And@457654321

time.sleep(10)
