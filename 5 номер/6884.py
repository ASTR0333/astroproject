def to12(n):
    s = ''
    while n != 0:
        last = n%12
        n = n // 12
        s = str(last) + s
    return s
ans = []
for n in range(12,10000):
    n2 = to12(n)
    if n % 12 == 0:
        n2 = n2 + n2[-2] + n2[-1]
    else:
        n2 = n2 + to12(n%12 * 9)
    r = int(n2,12)
    if r> 300:
        ans.append(r)
print(min(ans))

