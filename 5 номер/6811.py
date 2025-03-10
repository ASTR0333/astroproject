def to3(n):
    s = ''
    while n != 0:
        last = n%3
        n = n // 3
        s = str(last) + s
    return s
ans = []
for n in range(1,1000):
    n3 = to3(n)
    if n%3 == 0:
        n3 = '1' + n3 + '02'
    else:
        n3 =  n3 + to3((n%3)*4)
    r =  int(n3,3)
    if r < 199:
        ans.append(n)
print(max(ans))
