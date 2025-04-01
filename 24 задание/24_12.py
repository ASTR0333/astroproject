from re import *

with open('24_20813.txt') as file:
    s = file.readline().strip()

ch = r'(?:[1-9][0-9]*|0)'

sh = rf'{ch}(?:[-*]{ch})*'

lst = findall(sh,s)

print(len(max(lst,key=len)))