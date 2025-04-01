from re import findall

with open('24_19969.txt') as file:
    s = file.readline().strip()

sl = r'(?:[a-z]+)'

sh = rf'(?:{sl}[@]{sl}[.]{sl})+'

lst = findall(sh,s)
print(len(max(lst,key=len)))