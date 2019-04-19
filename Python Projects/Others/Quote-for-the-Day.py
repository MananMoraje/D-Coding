
import random


#  Arrays
KJ = ['\' I will peel you skin and hang your organs of the fan! \' -Kumari Joyce', '\' I will break your head! \' -Kumari Joyce','\' I will chop your head! \' -Kumari Joyce', '\' N\' Thalle! \' -Kumari Joyce']
GS = ['\' I will stab you! \' -General saying','\' I will shoot you! \' -General saying','\' I will kill you! \' -General saying', '\' I will chop your tongue! \' -General saying', '\' I will slap you! \' -General saying']
RT = ['\'Some fellows are truly hopeless! \' -Roshita Thomas']
P = ['\' I will eat your back! \' -Prema', '\ll cop your legs! \' -Prema']
D = ['\' I will squeeze you! \' -Dolly']


Ss = [KJ, RT, GS, D, P]
i = random.randint(-1, len(Ss))


#  Randoms
k = random.randint(0, len(KJ))
g = random.randint(0, len(GS))
r = random.randint(0, len(RT))
p = random.randint(0, len(P))
d = random.randint(0, len(D))


j = 0
if i == 0:
    j = KJ[k]
elif i == 1:
    j = GS[g]
elif i == 2:
    j = RT[r]
elif i == 3:
    j = P[p]
elif i == 4:
    j = D[d]


print('The quote for the day is: ' + j)

input('Please press enter when you are finished.')
