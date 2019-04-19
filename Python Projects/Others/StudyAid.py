from random import *
Qs = 0
Q = 5

#  round 1
GR1 = ['Correct.', 'Excellent!', 'Spot on!', 'Fabulous!', 'Exemplary!', 'Superb!' ]
Q1 = input('Enter Q1 here   ')
# <- Enter <- Q1 <- there <-
if 'point 1' and 'point 2' and 'point 3' in Q1:
    Qs += 1
    print(GR1[random.randint(0, len(GR1))])
else:
    print('It seemes that either your answer is wrong or you missed a point')
#  round 2

GR2 = ['Correct.', 'Excellent!', 'Spot on!', 'Fabulous!', 'Exemplary!', 'Superb!']
Q2 = input('Enter Q2 here   ')
#  <- Enter <- Q2 <- there <-
if 'point 1' and 'point 2' and 'point 3' in Q2:
    Qs += 1
    print(GR2[random.randint(0, len(GR2))])
else:
    print('It seemes that either your answer is wrong or you missed a point')

#  round 3
GR3= ['Correct.', 'Excellent!', 'Spot on!', 'Fabulous!', 'Exemplary!', 'Superb!']
Q3 = input('Enter Q3 here   ')
#  <- Enter <- Q2 <- there <-
if 'point 1' and 'point 2' and 'point 3' in Q3:
    Qs += 1
    print(GR3[random.randint(0, len(GR3))])
else:
    print('It seemes that either your answer is wrong or you missed a point')

#  round 4
GR4 = ['Correct.', 'Excellent!', 'Spot on!', 'Fabulous!', 'Exemplary!', 'Superb!']
Q4 = input('Enter Q4 here   ')
#  <- Enter <- Q2 <- there <-
if 'point 1' and 'point 2' and 'point 3' in Q4:
    Qs += 1
    print(GR4[random.randint(0, len(GR4))])
else:
    print('It seemes that either your answer is wrong or you missed a point')

#  round 5
GR5 = ['Correct.', 'Excellent!', 'Spot on!', 'Fabulous!', 'Exemplary!', 'Superb!']
Q5 = input('Enter Q5 here   ')
#  <- Enter <- Q2 <- there <-
if 'point 1' and 'point 2' and 'point 3' in Q5:
    Qs += 1
    print(GR5[random.randint(0, len(GR5))])
else:
    print('It seemes that either your answer is wrong or you missed a point')

# Score & Percentage
p =  Qs/Q * 100
print('         Your score was: ' + str(Qs) + ' out of ' + str(Q))
print('         Your percentage was: ' + str(p) + '%  ')

if p < 45:
    print('I am sorry, you failed')
elif p >= 46 and p < 60:
    print('Alright. Not bad.')
elif p >= 61 and p < 80:
    print('Good, try to improve.')
elif p >= 81 and p < 90:
    print('Very good!')
else:
    print('Fabulous! Excellent!')
input('Press ENTER when you have finished.')
