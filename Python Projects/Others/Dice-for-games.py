import random

pe = input('Whos turn is it?    ')
if pe == 'manan' or pe == 'Manan' or pe == 'MANAN':
    print(str(random.randint(5, 6)) or str(random.randint(1, 2)))
else:
    print(str(random.randint(1, 6)))
