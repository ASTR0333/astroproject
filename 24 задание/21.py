from string import *

with open('o7GIvUMYm.txt') as file:
    s = file.readline().strip()

zapret = 'GHIJKLMNOPQRSTUVWXYZ'

for x in zapret:
    s = s.replace(x,'_')
lst = s.split('_')
print(len(max(lst,key=len)))


