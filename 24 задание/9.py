from string import *
d = {}
alph = ascii_uppercase
s = [x for x in alph]
for i in s:
    d.update({i : 0})

file = open('24-157.txt')
s1 = file.readline()
for i in range(len(s1)-2):
    if s1[i] == s1[i+1]:
        d.update({s1[i+2]:d.get(s1[i+2])+1})

maks = max(d.values())




