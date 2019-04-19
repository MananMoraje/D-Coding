
import time

ms = 0
s = 0
m = 0
while True:
    time.sleep(0.01)
    ms += 1
    if ms > 100:
        s += 1
        ms = 0
    elif s > 60:
        m += 1
        s = 0
    if s > 0:
        print(str(m) + ':' + str(s))

