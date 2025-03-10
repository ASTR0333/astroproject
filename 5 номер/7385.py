def to4(n):
    s = ''
    while n != 0:
        last = n%4
        n = n // 4
        s = str(last) + s
    return s
ans = []
for n in range(1,1000):
    n4 = to4(n)
    if n % 4 == 0:
        n4 = n4 + n4[-2] + n4[-1]
    else:
        n4 = n4 + to4((n%4)*5)
    r = int(n4,4)
    if r < 555:
        ans.append(n)
print(max(ans))
