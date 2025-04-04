def to3(n):
    s = ''
    while n != 0:
        last = n%3
        n = n // 3
        s = str(last) + s
    return s
ans = []
for n in range(1, 100000):
    n3 = to3(n)
    if n3.count('1') + (n3.count('2')*2)% 4 == 0:
        n3 = '1' + n3
        n3 = n3[:-2]
    else:
        n3 += to3( n3.count('1') + (n3.count('2')*2) % 4 * 3 )
    r = int(n3, 3)
    if r > 353:
        ans += [r]
print(min(ans))