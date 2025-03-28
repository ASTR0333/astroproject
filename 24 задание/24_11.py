from re import *

with open('24-300.txt') as file:
    s = file.readline().strip()

#s = '52*73*81*0+13*0*2*3+0*123+150*150'
#100*0+543*543*0+0

ch = r'(?:[1-9][0-9]*|0)'

#mn = rf'{ch}(?:[*]{ch})*'

mn = rf'(?:{ch}[*])*0(?:[*]{ch})*'

sh = rf'{mn}(?:[+]{mn})*'

lst = findall(sh,s)

lst.sort(reverse=True,key=len)

#print(*lst[:10],sep='\n')
print(len(max(lst,key=len)))