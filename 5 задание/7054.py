def to6(n):
    s = ''
    while n != 0:
        last = n%6
        n = n // 6
        s = str(last) + s
    return s
ans = []
for n in range(10,1000):
    n6 = to6(n)
    if n % 3 == 0:
        n6 = n6 + n6[0] + n6[1]
    else:
        n6 = n6 + to6((n%3)*10)
    r = int(n6,6)
    if r > 680:
        ans.append(r)
print(min(ans))


