import random


def var1():
    print('If you get a six(6), you win!')
    rand1 = random.randint(1, 6)
    print(str(rand1))

    if rand1 == 6:
        print('You win!')


def var2():
    print('If both numbers are the same, you win')
    print('If both ar sixes(6) you win double')
    rand2 = random.randint(1, 6)
    print(str(rand2))
    rand3 = random.randint(1, 6)
    print(str(rand3))

"""

def var3():
    print('Two players. Who ever gets highest wins')
    p1 = input('Player one:     ')
    p2 = input('Player two:     ')

    p1rand1 = random.randint(1, 6)
    p1rand2 = random.randint(1, 6)

    p2rand1 = random.randint(1, 6)
    p2rand2 = random.randint(1, 6)

    sum1 = sum(p1rand1, p1rand2)
    
    print(p1 + ' \'s total is: ', str(sum1))
    print(p2 + ' \'s total is: ', str(sum(p1rand1, p1rand2)))
    if sum(p1rand1, p1rand2) > sum(p2rand1, p2rand2):
        print(p1 + ' wins!')
    elif sum(p1rand1, p1rand2) < sum(p2rand1, p2rand2):
        print(p2 + ' wins!')
    else:
        print('It was a tie!')
"""


def var4():
    print('Two players. Both choose 3 numbers. Who ever\'s number is shown, wins')

    p1 = input('Player one:     ')
    p2 = input('Player two:     ')

    print('When entering numbers, NO spaces nor commas. Eg. 564 >> I pick numbers 5, 6, and 4 ')

    p1_nums = input(p1 + '\'s numbers:  ')
    p2_nums = input(p2 + '\'s numbers:  ')

    dice = random.randint(1, 6)
    i = 0
    print(str(dice))

    if len(p1_nums) > 3:
        print('Are you trying to cheat? Only three(3) numbers. You are wasting your money. ')
    elif len(p2_nums) > 3:
        print('Are you trying to cheat? Only three(3) numbers. You are wasting your money. ')

    while i < 3:
        if dice == int(p1_nums[i]):
            print(p1 + ' wins!')
        elif dice == int(p2_nums[i]):
            print(p2 + ' wins!')
        i += 1


print('For variation 1 type\'var 1\'. For variation 2 type\'var 2\'.')
print(' For variation 3 type\'var 3\'.')
gm = input('Which variation would you like to play?')

if gm == 'var 1':
    var1()
elif gm == 'var 2':
    var2()
elif gm == 'var 3':
    var4()
else:
    print('Please enter one of the above options')

"""
elif gm == 'var 3':
    var3()
For variation 4 type\'var 4\'.
"""
