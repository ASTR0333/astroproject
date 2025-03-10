def to6(n):
    s = ''
    while n !=0:
        last = str(n%6)
        n = n // 6
        s =  last + s 
    return s 
ans = []
for n in range(1,1000):
    n6 = to6(n)
    if len(n6) >=2:
        if n%3 ==0:
            n6= n6 + n6[0] + n6[1]
        else:
            n6 = n6 + to6((n%3)*10) 
        r = int(n6,6)
        if r > 680:
            ans.append(r)
print(min(ans))