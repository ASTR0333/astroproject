from re import *


with open('24-332.txt') as file:
    s = file.readline().strip()

ps = r'[A-Z][a-z]*'
sl = r'[a-zA-Z][a-z]*'
#ps sl sl sl sl.

sh = rf'{ps}(?: {sl})*[.]'

lst = findall(sh,s)
lst.sort(reverse=True,key=len)

#print(*lst[:10],sep='\n')
print(len(max(lst,key=len)))
