from string import *

file = open('s2 (1).txt')
s = file.readline().strip()
alph = ascii_uppercase
maks = 0
for x in alph:
    k = s.count('Q'+x)
    if k > maks:
        maks  = k
        maksx = x
print(maksx+str(maks))

