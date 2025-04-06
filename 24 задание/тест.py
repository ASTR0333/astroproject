from re import *

with open('24_21161.txt') as file:
    s = file.readline().strip()

ps = r'(?:[A-Z][a-z]*)'
sl = r'(?:[A-Z]?[a-z]+)'
sh = rf'(?:{ps}(?:[ ]{sl})*[.])'

lst = findall(sh,s)
print(len(max(lst,key=len)))
