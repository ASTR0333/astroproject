
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
    if n%2 == 0:
        n3 = '2' + n3
        n3 = n3 + to3(int(n3[-1]) * 2)
    else:
        n3 = n3 + '2'
        n3 = to3(int(n3[0]) * 2) + n3
    r = int(n3, 3)
    if r>100:
        ans.append(r)
print(min(ans))

