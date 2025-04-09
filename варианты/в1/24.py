from re import *
with open('24.txt') as file:
    s = file.readline().strip()

sh = r'(?:DBAC)+(?:DBA|BAC|DB|AC|D|B|A|C)?'

lst = findall(sh,s)
print(len(max(lst,key=len)))