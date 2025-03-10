def to3(n):
    s = ''
    while n !=0:
        last = str(n%3)
        n = n // 3 
        s =  last + s 
    return s 
ans=[]
for n in range(11,1000):
    n3 = to3(n)
    if n3.count('2')+ n3.count('0') > n3.count('1'):
        n3 = '22' + n3
    else:
        n3 = '11' + n3
    r = int(n3,3)
    if r>100:
        ans.append(r)
print(min(ans))
