from fnmatch import *

def prost(n):
    if n == 1:
        return 0
    for d in range(2,int(n**0.5)+1):
        if n%d==0:
            return 0
    return 1
lst1 = []
for n in range(1,10**5+1):
    if prost(n):
        lst1.append(n)

lst2 = [x for x in lst1 if prost(lst1.index(x)+1)]


for x in range(1,10**5+1):
    if x in lst2:
        if fnmatch(str(x),'1*7?7'):
            print(x,lst1.index(x)+1)
