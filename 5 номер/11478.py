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
    if n%2==0:
        n3 = '1' + n3 + '00'
    else:
        n3 = n3 + to3(n3.count('1') + (n3.count('2')*2))
    r = int(n3,3)
    if r>168:
        ans.append(n)
print(min(ans))

