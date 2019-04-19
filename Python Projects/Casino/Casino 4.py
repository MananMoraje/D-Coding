# Slot Machine- 1/100
import random

num1 = random.randint(1, 33)
num2 = random.randint(1, 33)
num3 = random.randint(1, 33)

print('If all three numbers are equal to 10, you win.')
print(str(num1), ' ' + str(num2), ' ' + str(num3))

if num1 == num2 == num3 == 10:
    print('You won!')
else:
    print('You could win next time.')
input('Press ENTER when you have finished.')
